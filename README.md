# biologyai-yi
Yi Hackathon for biologyAI team

for PMID in $(esearch -db pubmed -query "life extension AND 2023/01/01:3000[Date - Publication]" | efetch -format uid); do echo $PMID && \n    efetch -db pubmed -id $PMID -format abstract > "$PMID.txt"\ndone\n


esearch -db pubmed -query "life extension" | efetch -format abstract > life_extension.txt\n

