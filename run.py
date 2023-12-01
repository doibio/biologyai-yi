import requests
import os
import codecs

url = "https://gpu-server.onrender.com/" #'http://localhost:8000/' #

directory_path = 'edirect10'

documents = []

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
    prompt = document["snippet"]
    model2 = "TheBloke/Yi-34B-Chat-AWQ"
    response2 = requests.post(url + "llm_prompt", 
                              json={"prompt":prompt, 
                                    "model":model2,
                                    "system_message":"Describe this for a person interested in life extension who is well educated about life extension methods."})
    print(response2.text)
    print("----------------------------------------")
 
