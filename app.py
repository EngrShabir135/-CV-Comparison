import streamlit as st
import pdfplumber
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
st.title("hi")
# Load NLP model
nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(pdf_file):
    with pdfplumber.open(pdf_file) as pdf:
        text = "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])
    return text

def preprocess_text(text):
    doc = nlp(text.lower())
    return " ".join([token.lemma_ for token in doc if not token.is_stop and token.is_alpha])

def calculate_similarity(cv_texts, job_desc):
    vectorizer = TfidfVectorizer()
    documents = cv_texts + [job_desc]
    tfidf_matrix = vectorizer.fit_transform(documents)
    similarities = cosine_similarity(tfidf_matrix[:-1], tfidf_matrix[-1])
    return similarities.flatten()

# Streamlit UI
st.title("CV Matching System")
st.write("Upload two CVs and provide a job description to find the best match.")

cv1 = st.file_uploader("Upload First CV (PDF)", type=["pdf"])
cv2 = st.file_uploader("Upload Second CV (PDF)", type=["pdf"])
job_desc = st.text_area("Enter Job Description")

if st.button("Compare CVs"):
    if cv1 and cv2 and job_desc:
        cv1_text = extract_text_from_pdf(cv1)
        cv2_text = extract_text_from_pdf(cv2)
        
        # Preprocess text
        processed_cv1 = preprocess_text(cv1_text)
        processed_cv2 = preprocess_text(cv2_text)
        processed_job_desc = preprocess_text(job_desc)
        
        # Compute similarity
        scores = calculate_similarity([processed_cv1, processed_cv2], processed_job_desc)
        
        # Display results
        st.subheader("Results")
        st.write(f"**CV 1 Similarity Score:** {scores[0]:.2f}")
        st.write(f"**CV 2 Similarity Score:** {scores[1]:.2f}")
        
        best_match = "CV 1" if scores[0] > scores[1] else "CV 2"
        st.success(f"The best-matching CV is: **{best_match}**")
    else:
        st.error("Please upload both CVs and provide a job description.")
