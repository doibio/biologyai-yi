import requests

API_URL = "https://uxx4vovn7n7xqrd0.us-east-1.aws.endpoints.huggingface.cloud"
headers = {
	"Authorization": "Bearer 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",
	"Content-Type": "application/json"
}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
        "parameters": {"min_length": 10000},
	"inputs": "Can you please let us know more details about your ",
})

print(output)
