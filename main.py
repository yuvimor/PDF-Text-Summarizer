import streamlit as st
import pdfplumber
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def summarize_pdf(pdf_file):
  """Summarizes the content of a PDF file using NLP.

  Args:
    pdf_file: The path to the PDF file to summarize.

  Returns:
    A summary of the PDF file, as a string.
  """

  pdf_reader = pdfplumber.open(pdf_file)

  # Get all the text in the PDF file.
  text = ""
  for page in pdf_reader.pages:
    text += page.extract_text()

  # Remove stop words from the text.
  stop_words = set(stopwords.words("english"))
  words = word_tokenize(text)
  filtered_words = [word for word in words if word not in stop_words]

  # Generate a summary of the text.
  summary = " ".join(filtered_words[:500])

  return summary

def main():
  """The main function of the Streamlit app."""

  st.title("PDF Text Summarization")

  pdf_file = st.file_uploader("Upload a PDF file:")

  if pdf_file is not None:
    summary = summarize_pdf(pdf_file)
    st.write("Summary:")
    st.write(summary)

if __name__ == "__main__":
  main()
