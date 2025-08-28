import streamlit as st
import pandas as pd


st.title("this os title00")
names=st.text_input("entrer your naeme")


age=st.slider("skect your age",0,100,15 )
st.write(f"ypur age ois {age}")

options=['python','java','c++','javscript']
choices=st.selectbox("choose your favourite choices ",options)
st.write(f'toy have selected {choices}')

if names:
    st.write(f"hello {names}")



    import pandas as pd

# Create a dummy dataframe with 4 rows and 5 columns
data = {
    "Name": ["Alice", "Bob", "Charlie", "Diana"],
    "Age": [25, 32, 29, 41],
    "City": ["New York", "London", "Paris", "Tokyo"],
    "Profession": ["Data Scientist", "Engineer", "Designer", "Manager"],
    "Salary ($)": [85000, 92000, 78000, 105000]
}

df = pd.DataFrame(data)
df.to_csv("sameple.csv ")
st.write(df)


uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    # Read the uploaded CSV file into a pandas DataFrame
    df = pd.read_csv(uploaded_file)
    
    st.success("✅ File uploaded successfully!")
    st.write("Here’s a preview of your data:")
    st.dataframe(df.head())  # Show first 5 rows
else:
    st.info("Please upload a CSV file to proceed.")

