import streamlit as st
import pdftotext

def summarize_pdf(pdf_file):
  """Summarizes the content of a PDF file.

  Args:
    pdf_file: The path to the PDF file to summarize.

  Returns:
    A summary of the PDF file, as a string.
  """

  with open(pdf_file, "rb") as f:
    pdf_text = pdftotext.PDF(f)

  summary = ""
  for sentence in pdf_text:
    summary += sentence + " "

  return summary[:500]

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
