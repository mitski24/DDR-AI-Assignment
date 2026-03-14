from openai import OpenAI
from prompts import DDR_PROMPT
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_ddr(inspection_text, thermal_text):

    prompt = DDR_PROMPT.format(
        inspection=inspection_text,
        thermal=thermal_text
    )

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are a property diagnostic expert."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    return response.choices[0].message.content