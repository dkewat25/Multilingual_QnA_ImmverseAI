import streamlit as st
import tempfile
import os

from modules.text_extractor import extract_text
from modules.qna_generator import generate_qna
from modules.translator import translate_qna
from modules.excel_generator import save_to_excel


st.set_page_config(page_title="Multilingual QnA Generator")

st.title("Multilingual QnA Generation System")

st.write(
"""
Upload a document (.pdf, .docx, .txt).  
The system will generate Question–Answer pairs and translate them into:

• English  
• Hindi  
• Marathi  

Then export the results as **QnA.xlsx**.
"""
)

uploaded_file = st.file_uploader(
    "Upload a document",
    type=["pdf", "docx", "txt"]
)

if uploaded_file:

    st.success("File uploaded successfully")

    file_extension = uploaded_file.name.split(".")[-1]

    with tempfile.NamedTemporaryFile(delete=False, suffix=f".{file_extension}") as tmp:

        tmp.write(uploaded_file.read())
        file_path = tmp.name

    if st.button("Generate QnA"):

        with st.spinner("Processing document..."):

            # Step 1
            text = extract_text(file_path)

            # Step 2
            qna_pairs = generate_qna(text)

            # Step 3
            translated_qna = translate_qna(qna_pairs)

            # Step 4
            save_to_excel(translated_qna)

        st.success("QnA generated successfully!")

        st.subheader("Preview (English)")

        for qna in translated_qna:

            st.write("**Q:**", qna["question_en"])
            st.write("**A:**", qna["answer_en"])
            st.write("---")

        if os.path.exists("QnA.xlsx"):

            with open("QnA.xlsx", "rb") as f:

                st.download_button(
                    label="Download Excel File",
                    data=f,
                    file_name="QnA.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )