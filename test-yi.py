import requests

API_URL = "https://zbcr1xtvyhjfqg93.us-east-1.aws.endpoints.huggingface.cloud"
headers = {
	"Authorization": "Bearer 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",
	"Content-Type": "application/json"
}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": "Please summarize the following: Erikson’s Stages of Psychosocial Development is a theory introduced in the 1950s by the psychologist and psychoanalyst Erik Erikson. It built upon Freud’s theory of psychosexual development by drawing parallels in childhood stages while expanding it to include the influence of social dynamics as well as the extension of psychosocial development into adulthood. It posits eight sequential stages of individual human development influenced by biological, psychological, and social factors throughout the lifespan. This bio-psychosocial approach has influenced several fields of study, including gerontology, personality development, identity formation, life cycle development, and more.",
})

print(output)
