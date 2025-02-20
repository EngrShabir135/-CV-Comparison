# -CV-Comparison
# CV Comparison Using Streamlit

## 📌 Project Overview
This project allows companies to compare two CVs against a given job description (e.g., Data Analyst) and determine which candidate is a better match. The system highlights the most relevant CV based on skills and experience.

## 🚀 Features
- Upload and compare two CVs in PDF format.
- Analyze CVs based on job requirements.
- Highlight which CV is a better match.
- Built with **Streamlit**, **spaCy**, and **Scikit-learn**.

## 🛠️ Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/your-username/CV-Comparison.git
cd CV-Comparison
Step 2: Create a Virtual Environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Step 3: Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
Step 4: Download spaCy Model
bash
Copy
Edit
python -m spacy download en_core_web_sm
🎯 How to Run the Project
Run the Streamlit app with:

bash
Copy
Edit
streamlit run app.py
This will open the app in your default web browser.

📂 Project Structure
bash
Copy
Edit
📂 CV-Comparison
│-- 📄 app.py           # Main Streamlit application
│-- 📂 venv/            # Virtual environment (not included in GitHub)
│-- 📂 data/            # Sample CVs (optional)
│-- 📄 requirements.txt  # List of dependencies
│-- 📄 .gitignore        # Git ignored files
│-- 📄 README.md         # Project documentation
📌 How It Works
Upload CVs: The user uploads two CVs in PDF format.
Process CVs: The system extracts text and matches it with job requirements.
Compare Scores: It highlights which CV is a better fit.
Display Results: The best-matched CV is shown in the UI.
🤖 Technologies Used
Python
Streamlit
spaCy (for NLP processing)
Scikit-learn (for text similarity)
PyMuPDF (for PDF processing)
💡 Future Improvements
Support for more job roles.
Integration with an ATS (Applicant Tracking System).
AI-based resume ranking.
📜 License
This project is licensed under the MIT License.
