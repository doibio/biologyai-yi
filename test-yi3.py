import requests

url = "https://gpu-server.onrender.com/" #'http://localhost:8000/' #

prompt = """Metformin is considered a safe anti-hyperglycemic drug for patients with type 2 
diabetes (T2D); however, information on its impact on heart failure-related 
outcomes remains inconclusive. The current systematic review explored evidence 
from randomized clinical trials (RCTs) reporting on the impact of metformin in 
modulating heart failure-related markers in patients with or without T2D. 
Electronic databases such as MEDLINE, Cochrane Library, and EMBASE were searched 
for eligible studies. Included studies were those assessing the use of metformin 
as an intervention, and also containing the comparison group on placebo, and all 
articles had to report on measurable heart failure-related indices in 
individuals with or without T2D. The modified Downs and Black checklist was used 
to evaluate the risk of bias. Overall, nine studies met the inclusion criteria, 
enrolling a total of 2486 patients. Although summarized evidence showed that 
metformin did not affect left ventricular function, this antidiabetic drug could 
improve myocardial oxygen consumption concomitant to reducing prominent markers 
of heart failure such as n-terminal pro-brain natriuretic peptide and 
low-density lipoprotein levels, inconsistently between diabetic and nondiabetic 
patients. Effective modulation of some heart failure-related outcomes with 
metformin treatment was related to its beneficial effects in ameliorating 
insulin resistance and blocking pro-inflammatory markers such as the 
aging-associated cytokine CCL11 (C-C motif chemokine ligand 11). Overall, 
although such beneficial effects were observed with metformin treatment, 
additional RCTs are necessary to improve our understanding on its modulatory 
effects on heart failure-related outcomes especially in diabetic patients.
"""

model2 = "TheBloke/Yi-34B-Chat-AWQ"
response2 = requests.post(url + "llm_prompt", 
                         json={"prompt":prompt, 
                               "model":model2,
                               "system_message":"Describe this for a layperson interested in life extension"})
print(response2.text)
