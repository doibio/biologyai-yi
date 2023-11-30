import requests

API_URL = "https://bnpyrgkwkz258f4h.us-east-1.aws.endpoints.huggingface.cloud"
headers = {
	"Authorization": "Bearer XXXXXX",
	"Content-Type": "application/json"
}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": "What is the immune system?",
})
import requests

API_URL = "https://bnpyrgkwkz258f4h.us-east-1.aws.endpoints.huggingface.cloud"
headers = {
	"Authorization": "Bearer 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",
	"Content-Type": "application/json"
}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": "What is the human immune system?",
})

print(output)

