import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Add the website link at the top
st.markdown("""
<div style='text-align: right; font-size: 14px;'>
    <br>
    Visit our website: <a href='https://www.gqci.ca' target='_blank'>www.gqci.ca</a>
</div>
""", unsafe_allow_html=True)

# Add logo 
st.image("logo.png", width=200)  # Adjust width as needed
# Streamlit app title
st.title("AI Data Analyzer")
st.subheader("Enter any data file and make data driven decisions!")
# Sidebar for file upload and settings
st.sidebar.header("Upload your file")
uploaded_file = st.sidebar.file_uploader("Choose a file (CSV, Excel, or TXT)", type=["csv", "xlsx", "xls", "txt"])

# Sidebar: File preview option
show_preview = st.sidebar.checkbox("Show File Preview", value=True)

# Sidebar: Checkbox for graph selection
show_histogram = st.sidebar.checkbox("Show Histogram", value=True)
show_correlation = st.sidebar.checkbox("Show Correlation Heatmap", value=True)
show_pairplot = st.sidebar.checkbox("Show Pairplot", value=False)

# Display file preview and graphs if a file is uploaded
if uploaded_file is not None:
    # File type detection and reading
    file_extension = uploaded_file.name.split('.')[-1]
    if file_extension in ['csv', 'txt']:
        df = pd.read_csv(uploaded_file)
    elif file_extension in ['xlsx', 'xls']:
        df = pd.read_excel(uploaded_file)
    else:
        st.error("Unsupported file format!")

    # Display file preview if checkbox is checked
    if show_preview:
        st.subheader("File Preview")
        st.dataframe(df.head(10))

    # Generate graphs based on checkbox options
    if show_histogram:
        st.subheader("Histogram")
        selected_column = st.selectbox("Select a column for Histogram", df.columns)
        plt.figure(figsize=(10, 5))
        plt.hist(df[selected_column].dropna(), bins=20, color='skyblue', edgecolor='black')
        plt.title(f"Histogram of {selected_column}")
        st.pyplot(plt)

    if show_correlation:
        st.subheader("Correlation Heatmap")
        plt.figure(figsize=(12, 8))
        sns.heatmap(df.corr(), annot=True, cmap='coolwarm', linewidths=0.5)
        plt.title("Correlation Heatmap")
        st.pyplot(plt)

    if show_pairplot:
        st.subheader("Pairplot")
        sns.pairplot(df.dropna(), diag_kind='kde')
        st.pyplot(plt)

else:
    st.write("Upload a file to begin analysis.")

# Add the website link at the bottom
st.markdown("""
<div style='text-align: center; font-size: 14px;'>
    <br>
    Visit our website: <a href='https://www.gqci.ca' target='_blank'>www.gqci.ca</a>
</div>
""", unsafe_allow_html=True)
