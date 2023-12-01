import requests

url = "https://gpu-server.onrender.com/" #'http://localhost:8000/' #

prompt = """BACKGROUND: Rapamycin, an inhibitor of the serine/threonine protein kinase mTOR, is an immunosuppressant used to treat renal transplant recipients, but it can cause endothelial and mitochondrial dysfunction. Metformin is used for the treatment of type 2 diabetes and was reported to exert therapeutic effects against rheumatoid arthritis and obesity by improving mitochondrial dysfunction via the activation of fibroblast growth factor 21. We investigated the therapeutic effects of rapamycin-metformin combination therapy in obese mice with collagen-induced arthritis (CIA).  METHODS: Mouse embryonic fibroblasts were treated with rapamycin, metformin, or rapamycin-metformin, and their respiratory level and mitochondrial gene expression were assayed. Mice were fed a high-fat diet, immunized with type II collagen, and subsequently treated with rapamycin-metformin daily for 10 weeks.  RESULTS: Rapamycin-treated cells exhibited dysfunction of mitochondrial respiration and decreased mitochondrial gene expression compared with rapamycin-metformin-treated cells. Moreover, rapamycin-metformin reduced the clinical arthritis score and the extent of histological inflammation and improved the metabolic profile in obese mice with CIA. Rapamycin-metformin enhanced the balance between T helper 17 and regulatory T cells in vitro and in vivo.  CONCLUSIONS: These results suggest that rapamycin-metformin is a potential therapeutic option for autoimmune arthritis.

"""

model2 = "TheBloke/Yi-34B-Chat-AWQ"
response2 = requests.post(url + "llm_prompt", 
                         json={"prompt":prompt, 
                               "model":model2,
                               "system_message":"Describe this for a layperson interested in life extension"})
print(response2.text)
