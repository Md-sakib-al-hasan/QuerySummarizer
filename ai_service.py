import os
from google import genai
from google.genai import types
from dotenv import load_dotenv



# import the api_key
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")



client = genai.Client(api_key=api_key)

def generate_ai_response (images, difficulty):
     contents = []
     contents.append(
    f"Task: Analyze the provided notes/images carefully and generate structured output in this exact order:\n\n"
    
    f"1. SUMMARY:\n"
    f"- Write a short clear summary of the content.\n\n"
    
    f"2. KEY POINTS:\n"
    f"- Provide important points as a bullet list.\n\n"
    
    f"3. USEFUL INFORMATION:\n"
    f"- If any factual references or concepts exist, list them as bullet points.\n"
    f"- If no external references exist, skip this section.\n\n"
    
    f"4. QUIZ ({difficulty} level):\n"
    f"- Create ONLY 3 multiple-choice questions.\n"
    f"- Each question must have 4 options (A, B, C, D).\n"
    f"- Do NOT show answers here.\n\n"
    
    f"5. ANSWERS:\n"
    f"- After all questions, provide the correct answers in order (1, 2, 3).\n\n"
    
    f"STRICT RULES:\n"
    f"- Do not add extra questions.\n"
    f"- Do not mix answers with questions.\n"
    f"- Follow format exactly."
)

     for img in images:
        contents.append(
            types.Part.from_bytes(
             data = img.getvalue(),
             mime_type = img.type

            )
        )


     response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents =contents
    )
     return response.text

