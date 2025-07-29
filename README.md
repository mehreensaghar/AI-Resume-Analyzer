

# 📄 AI Resume Analyzer – Smart Job Match & Resume Optimizer

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://ai-resume-analyzer-nyk7hfgvbz38ycqoxrstyd.streamlit.app/)

---

## 🔹 Introduction

The **AI Resume Analyzer** is an intelligent web application that helps job seekers and recruiters instantly evaluate how well a resume matches a given job description. Using **Natural Language Processing (NLP)** and **OpenAI GPT**, the app provides:

* ✅ A **Match Score (%)** showing how well a resume aligns with the job.
* ✅ A list of **Missing Skills** that could improve the match.
* ✅ **AI-powered recommendations** to help tailor the resume for better results.

Built with **Streamlit**, this project demonstrates **real-world AI deployment**, combining text extraction, embeddings, and GPT-based suggestions into an easy-to-use tool.

---

## 🚀 Features

* 📂 **Upload Resume** – Extracts text from PDF files automatically.
* 📝 **Input Job Description** – Structured input for accurate matching.
* 📊 **Match Score (%)** – Calculates resume-to-job similarity using NLP embeddings.
* 🔹 **Missing Skills Detector** – Highlights required skills not in the resume.
* 🤖 **AI-Powered Suggestions** – Provides improvement tips via OpenAI GPT.
* 🌐 **Live Demo** – Try it online instantly, no installation required.

---

## 🛠️ Tech Stack

* **Frontend/UI:** Streamlit
* **Backend:** Python 3.12
* **NLP Model:** SentenceTransformers (MiniLM)
* **AI Suggestions:** OpenAI GPT-3.5
* **PDF Processing:** pdfplumber

---

## ⚙️ How to Run Locally

```bash
# 1️⃣ Clone the repository
git clone https://github.com/mehreensaghar/AI-Resume-Analyzer.git
cd AI-Resume-Analyzer

# 2️⃣ Create & activate virtual environment
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate # Mac/Linux

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Set OpenAI API key
setx OPENAI_API_KEY "your_api_key_here"    # Windows
export OPENAI_API_KEY="your_api_key_here"  # Mac/Linux

# 5️⃣ Run the app
streamlit run app.py
```

---

## 🌐 Live Demo

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://ai-resume-analyzer-nyk7hfgvbz38ycqoxrstyd.streamlit.app/)


## ✅ Future Enhancements

* PDF Resume Match Report Download
* Multi-resume comparison feature
* Weighted scoring for critical vs. optional skills
* Advanced UI with custom themes and dashboard view

---

## 🤝 Contributions

Pull requests are welcome. For major changes, please open an issue first to discuss your ideas.

