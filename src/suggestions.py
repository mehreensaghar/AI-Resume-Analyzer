import openai
import os

# Load API key
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

def ai_resume_suggestions(resume_text, job_desc):
    if not api_key:
        return "⚠️ No API key found. Please set OPENAI_API_KEY."

    prompt = f"""
    I have this resume:
    {resume_text}

    And this job description:
    {job_desc}

    Suggest 3-5 specific improvements to make this resume a stronger match for the job.
    Keep suggestions short and actionable, in bullet points.
    """

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=200,
            temperature=0.7
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"⚠️ AI suggestions could not be generated. Error: {str(e)}"
