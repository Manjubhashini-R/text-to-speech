import streamlit as st
from PyPDF2 import PdfReader
import pyttsx3

def read_from_pdf():
    st.subheader("Read from PDF")
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
    if uploaded_file is not None:
        pdf_reader = PdfReader(uploaded_file)
        from_page = pdf_reader.pages[0]
        text = "\n".join(page.extract_text() for page in pdf_reader.pages)
        st.write("Text extracted from PDF:")
        st.write(text)
        speak_text(text)

def speak_text(text):
    st.subheader("Speak Text")
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def read_from_text():
    st.subheader("Read from Text")
    text = st.text_area("Enter the text you want to read aloud:")
    if st.button("Read Aloud"):
        speak_text(text)

def main():
    st.title("Text-to-Speech App")
    st.write("This app allows you to convert text to speech and read from PDF.")
    choice = st.radio("Select an option:", ("Read from Text", "Read from PDF"))
    
    if choice == "Read from Text":
        read_from_text()
    elif choice == "Read from PDF":
        read_from_pdf()

if __name__ == "__main__":
    main()
