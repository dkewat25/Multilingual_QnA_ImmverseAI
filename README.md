MULTILINGUAL QUESTION–ANSWER GENERATION SYSTEM

Overview
This project is an AI-powered system that automatically generates Question–Answer (QnA) pairs from documents and translates them into multiple languages. The system processes documents in .pdf, .docx, and .txt formats, extracts text, generates meaningful questions and answers using a transformer-based model, translates them into English, Hindi, and Marathi, and exports the results into a structured Excel file.

The goal of this project is to automate knowledge extraction from documents and make the information accessible across multiple languages.

------------------------------------------------------------

Features

- Supports PDF, DOCX, and TXT document formats
- Extracts text automatically from uploaded documents
- Generates Question–Answer pairs using NLP models
- Translates generated QnA into Hindi and Marathi
- Exports results to an Excel file with separate language sheets
- Simple Streamlit UI for easy interaction

------------------------------------------------------------

System Architecture

The system is divided into four main modules:

1. Text Extraction
   Extracts text from PDF, DOCX, and TXT files.

2. QnA Generation
   Uses a transformer-based model to generate questions from the extracted text.

3. Translation
   Translates QnA pairs into Hindi and Marathi.

4. Excel Generation
   Saves the multilingual QnA pairs into an Excel file.

------------------------------------------------------------

Project Structure

Multilingual_QnA_ImmverseAI

app.py
requirements.txt
README.txt

modules/
    text_extractor.py
    qna_generator.py
    translator.py
    excel_generator.py

------------------------------------------------------------

Installation

1. Clone the repository

git clone https://github.com/dkewat25/Multilingual_QnA_ImmverseAI.git

2. Navigate to the project folder

cd multilingual_qna_immverseai

3. Create virtual environment

python -m venv venv

4. Activate environment

Windows:
venv\Scripts\activate

5. Install dependencies

pip install -r requirements.txt

------------------------------------------------------------

Running the Application

Run the Streamlit app using:

streamlit run app.py

The application will open automatically in your browser.

------------------------------------------------------------

Usage Workflow

1. Upload a document (PDF / DOCX / TXT)
2. The system extracts text from the document
3. The AI model generates Question–Answer pairs
4. QnA pairs are translated into Hindi and Marathi
5. Download the generated Excel file (QnA.xlsx)

------------------------------------------------------------

Output Format

The generated Excel file contains three sheets:

English
Hindi
Marathi

Each sheet contains two columns:

Questions
Answers

------------------------------------------------------------

Technologies Used

Python
Streamlit
Hugging Face Transformers
PyTorch
Pandas
OpenPyXL
PyPDF2
python-docx
Deep Translator

------------------------------------------------------------

Future Improvements

- Support for additional languages
- Improved QnA generation using larger language models
- Deployment as a cloud-based web application
- Improved UI for batch document processing

------------------------------------------------------------

Author

Dishant Kewat
B.Tech Computer Engineering