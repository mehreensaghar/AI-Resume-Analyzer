import streamlit as st
from src.text_extraction import extract_text_from_pdf
from src.preprocess import clean_text
from src.match_score import get_match_score
from src.suggestions import ai_resume_suggestions

st.markdown("""
    <style>
    .stApp {
        background-color: #f8f9fa;
        font-family: 'Segoe UI', sans-serif;
    }
    .box {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
        box-shadow: 0px 2px 5px rgba(0,0,0,0.1);
    }
    div.stButton > button {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        border-radius: 8px;
        padding: 10px 20px;
        border: none;
    }
    .stProgress > div > div > div {
        background-color: #4CAF50;
    }
    </style>
""", unsafe_allow_html=True)


st.set_page_config(page_title="AI Resume Analyzer", layout="wide")

st.title("🧠 AI Resume Analyzer")
st.write("Upload your resume and fill out job details to see your match score.")

col1, col2 = st.columns([1, 1.5])

# --- LEFT PANEL: Resume Upload ---
with col1:
    
    st.subheader("📄 Upload Resume")
    uploaded_resume = st.file_uploader("Choose a PDF file", type=["pdf"])
    resume_text = ""
    if uploaded_resume:
        resume_text = extract_text_from_pdf(uploaded_resume)
        st.markdown("### ✅ Text Extracted")
        st.text_area("Resume Preview", resume_text[:1000] + "...", height=300)
    
# --- RIGHT PANEL: Job Details ---
with col2:
    st.subheader("📝 Job Description")
    job_title = st.text_input("Job Title")
    required_skills = st.text_area("Required Skills (comma separated)")
    experience = st.number_input("Minimum Experience (Years)", 0, 20)
    job_desc = st.text_area("Full Job Description")

# --- RESULT SECTION ---
if uploaded_resume and job_desc:
    clean_resume = clean_text(resume_text)
    clean_jd = clean_text(job_desc + " " + required_skills + " " + job_title)
    score = get_match_score(clean_resume, clean_jd)

    st.markdown("---")
    st.markdown(f"<h2 style='color:#4CAF50;'>✅ Match Score:{round(score)}%</h2>", unsafe_allow_html=True)

    if score < 60:
        st.error("⚠️ Your resume is not a strong match. Consider adding more relevant skills.")
        
    elif score < 80:
        st.warning("🟡 Decent match, but can be improved.")
        
    else:
        st.success("🟢 Excellent match! Your resume fits this job well.")
    
    st.markdown("### 💡 AI Recommendations")
    ai_tips = ai_resume_suggestions(clean_resume, clean_jd)
    st.write(ai_tips)