import openai

openai.api_key = "<AZURE_OPENAI_KEY>"
openai.api_base = "<AZURE_OPENAI_ENDPOINT>"
openai.api_type = "azure"
openai.api_version = "2023-05-15"

def extract_info(text):
    prompt = f"""
    Extract these fields from the agreement:
    - Vendor Name
    - License Protocol
    - Expiry Date
    - Cost
    - Support Details

    Text:
    {text}

    Return in JSON.
    """
    response = openai.ChatCompletion.create(
        engine="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']