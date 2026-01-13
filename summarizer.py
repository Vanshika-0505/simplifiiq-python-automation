import google.genai as genai
import os
from dotenv import load_dotenv


def summarize_content(web_data):
    load_dotenv()

    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        return "Gemini API key not found."

    client = genai.Client(api_key=api_key)

    combined_text = ""
    for item in web_data:
        if isinstance(item, dict) and item.get("content"):
            combined_text += item["content"] + "\n"

    if not combined_text.strip():
        return "No valid content available for summarization."

    response = client.models.generate_content(
        model="models/gemini-flash-latest",  
        contents=f"Summarize the following information clearly:\n{combined_text}"
    )

    return response.text
