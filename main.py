import streamlit as st
import pdfplumber
from transformers import BartTokenizer, BartForConditionalGeneration

# Title
st.title("PDF Text Summarizer using NLP")

# Upload PDF
pdf_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if pdf_file:
    with pdfplumber.open(pdf_file) as pdf:
        # Extract text from the PDF
        pdf_text = ""
        for page in pdf.pages:
            pdf_text += page.extract_text()

        # Initialize BART model and tokenizer
        model = BartForConditionalGeneration.from_pretrained('sshleifer/distilbart-cnn-12-6')
        tokenizer = BartTokenizer.from_pretrained('sshleifer/distilbart-cnn-12-6')

        # Tokenize and generate summary
        inputs = tokenizer([pdf_text], truncation=True, return_tensors='pt')
        summary_ids = model.generate(inputs['input_ids'], num_beams=4, early_stopping=True, max_length=500)
        summarized_text = tokenizer.decode(summary_ids[0], skip_special_tokens=True, clean_up_tokenization_spaces=True)
        
        st.subheader("Summary")
        st.write(summarized_text)
