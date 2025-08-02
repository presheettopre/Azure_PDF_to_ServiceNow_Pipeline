import requests

def push_to_servicenow(data):
    url = "https://<your_instance>.service-now.com/api/now/table/cust"
    auth = ('username', 'password_or_token')
    headers = {"Content-Type": "application/json", "Accept": "application/json"}

    response = requests.post(url, json=data, headers=headers, auth=auth)
    return response.status_code, response.json()