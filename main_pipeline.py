from blob_download import download_blob
from extract_text import extract_text_from_pdf
from extract_info_from_text import extract_info
from push_to_servicenow import push_to_servicenow
import json

def run_pipeline():
    blob_name = "test_agreement.pdf"
    local_path = "./downloaded.pdf"
    download_blob("agreement-pdfs", blob_name, local_path)

    text = extract_text_from_pdf(local_path)
    extracted_json = extract_info(text)
    data = json.loads(extracted_json)

    status, response = push_to_servicenow(data)
    print(f"ServiceNow Response: {status} → {response}")

if __name__ == "__main__":
    run_pipeline()