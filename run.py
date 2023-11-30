import requests
import os
import codecs


# API_URL = "https://zbcr1xtvyhjfqg93.us-east-1.aws.endpoints.huggingface.cloud"
# headers = {
# 	"Authorization": "Bearer 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",
# 	"Content-Type": "application/json"
# }
API_URL = "https://cyk532m7zhkpqslt.us-east-1.aws.endpoints.huggingface.cloud"
headers = {
	"Authorization": "Bearer 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",
	"Content-Type": "application/json"
}

directory_path = 'edirect2'

documents = []

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()
    
for filename in os.listdir(directory_path):
    if filename.endswith(".txt"):  
        filepath = os.path.join(directory_path, filename)
        try:
            with codecs.open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
                
                document = {
                    "title": filename.replace('.txt', ''),  
                    "snippet": content
                }
                documents.append(document)
        except Exception as e:
            print(f"Error reading {filename}: {e}")


for document in documents:
    output = query({
	"inputs": "Evaluate this treatment for efficacy: " + document["snippet"],
    })
    print("----------------------------------------")
    print(output)
