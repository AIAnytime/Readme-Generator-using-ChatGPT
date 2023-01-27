import streamlit as st 
import readme_generator as rg 

st.title = "Readme Generator with the help of ChatGPT"

uploaded_file = st.file_uploader("Upload Code File")

if uploaded_file is not None:
    content = uploaded_file.read().decode()
    response = rg.ask(f"{content}\n\nRead the code and generate a README.md for it in markdown format.")
    st.markdown("""----""")
    st.subheader("Response")
    st.text(response)
    st.markdown("""----""")
    st.subheader("Preview")
    st.markdown(response)