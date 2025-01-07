import openai

openai.api_key = 'sk-0HSd-ecNRhC5Gn7vXqjLFuvWQ4nJRVHVkYEOy7oFLoT3BlbkFJoRmgcLTgTlpIVsHqrnFCR_88nsv7z2TLjwvBBFZkwA'

def summarize_text(text: str) -> str:
    if not text.strip():
        return "No text provided for summarization."
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Summarize the data."},
                {"role": "user", "content": f"Summarize the following text:\n{text}"}
            ],
            max_tokens=200
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"Error in summarizing text: {str(e)}"

