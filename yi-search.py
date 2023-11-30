import cohere

import os
import codecs

directory_path = 'edirect0'

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



co = cohere.Client('KEY_HERE')
response = co.chat(
    message="Evaluate tebentafusp for efficacy",
    documents=documents,
    prompt_truncation="AUTO"
)
print(response)
