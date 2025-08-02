<<<<<<< HEAD
# Azure PDF to ServiceNow Pipeline

## Overview
This project extracts data from software agreement PDFs uploaded to Azure Blob Storage and populates a ServiceNow `cust` table using Azure OpenAI.

## Prerequisites
- Azure Blob Storage and connection string
- Azure OpenAI (GPT-4) access and endpoint
- ServiceNow API access with `cust` table
- Jenkins with Python and `pip` installed

## Setup
1. Replace placeholders (`<...>`) in Python files with your actual credentials.
2. Upload PDF to Azure Blob Storage:
```bash
az storage blob upload --account-name <account> --container-name agreement-pdfs --name test_agreement.pdf --file ./test_agreement.pdf
```
3. Run `main_pipeline.py` locally or via Jenkins pipeline.

## Files
- `blob_download.py`: Download PDF from Azure Blob
- `extract_text.py`: Extract text using PyMuPDF
- `extract_info_from_text.py`: Use Azure OpenAI to extract required fields
- `push_to_servicenow.py`: Call ServiceNow REST API
- `main_pipeline.py`: Orchestrates entire flow
- `Jenkinsfile`: Jenkins CI/CD pipeline
=======
# Azure_PDF_to_ServiceNow_Pipeline
Small POC
>>>>>>> d108b212797067ab0b7b1c54993e5d9d26a213e7
