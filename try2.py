import requests
from bs4 import BeautifulSoup
condition_url_for_drugs = "https://www.drugs.com/condition/bipolar-disorder.html?page_all=1"
#print(condition_url_for_drugs)
condition_response = requests.get(condition_url_for_drugs)
#print(condition_response.status_code)
html_content = condition_response.text
soup = BeautifulSoup(html_content, 'html.parser')
drug_table = soup.find('table')
#print(drug_table)
filename = 'try2.txt'
rows = drug_table.find_all('tr')[1:]
for row in rows:
    drug_cells = row.find('td')
    # print(drug_cells)
    drug_name = drug_cells.find('a',{'class':'condition-table__drug-name__link'})
    if(drug_name!=None):
        drug_name=drug_name.text
        print(drug_name)
    # file.write(drug_name+"\n")
    #print(drug_name)