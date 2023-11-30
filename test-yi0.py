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
	"inputs": "Please summarize the following for a layman who has not taken medical training.  Imidazoline receptors historically referred to a family of nonadrenergic binding sites that recognize compounds with an imidazoline moiety, although this has proven to be an oversimplification. For example, none of the proposed endogenous ligands for imidazoline receptors contain an imidazoline moiety but they are diverse in their chemical structure. Three receptor subtypes (I1, I2, and I3) have been proposed and the understanding of each has seen differing progress over the decades. I1 receptors partially mediate the central hypotensive effects of clonidine-like drugs. Moxonidine and rilmenidine have better therapeutic profiles (fewer side effects) than clonidine as antihypertensive drugs, thought to be due to their higher I1/α 2-adrenoceptor selectivity. Newer I1 receptor agonists such as LNP599 [3-chloro-2-methyl-phenyl)-(4-methyl-4,5-dihydro-3H-pyrrol-2-yl)-am ne hydrochloride] have little to no activity on α 2-adrenoceptors and demonstrate promising therapeutic potential for hypertension and metabolic syndrome. I2 receptors associate with several distinct proteins, but the identities of these proteins remain elusive. I2 receptor agonists have demonstrated various centrally mediated effects including antinociception and neuroprotection. A new I2 receptor agonist, CR4056 [2-phenyl-6-(1H-imidazol-1yl) quinazoline], demonstrated clear analgesic activity in a recently completed phase II clinical trial and holds great promise as a novel I2 receptor-based first-in-class nonopioid analgesic. The understanding of I3 receptors is relatively limited. Existing data suggest that I3 receptors may represent a binding site at the Kir6.2-subtype ATP-sensitive potassium channels in pancreatic β-cells and may be involved in insulin secretion. Despite the elusive nature of their molecular identities, recent progress on drug discovery targeting imidazoline receptors (I1 and I2) demonstrates the exciting potential of these compounds to elicit neuroprotection and to treat various disorders such as hypertension, metabolic syndrome, and chronic pain.",
})

print(output)

