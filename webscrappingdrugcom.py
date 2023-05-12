import requests
from bs4 import BeautifulSoup
from urllib.parse import quote
url = "https://www.drugs.com/alpha/condition/"
response = requests.get(url)
html_content = response.text
soup = BeautifulSoup(html_content, 'html.parser')
ul_tag_of_condition = soup.find('ul', {'class': 'ddc-list-column-4'})
li_of_conditions = ul_tag_of_condition.find_all('li')

lst_of_all_condition = []
lst_of_all_link_of_conditions = []
for li in li_of_conditions:
    a_tag_text = li.find('a').text
    lst_of_all_condition.append(a_tag_text)
    lst_of_all_link_of_conditions.append(li.find('a').get('href'))
i=0
for condition in lst_of_all_link_of_conditions:
    condition_url_for_drugs = str(f"https://www.drugs.com{condition}?page_all=1")
    encoded_url = quote(condition_url_for_drugs, safe=':/?=&')
    # print(condition_url_for_drugs)
    condition_response = requests.get(encoded_url)
    #print(condition_response.status_code)
    html_content = condition_response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    drug_table = soup.find('table')
    #print(drug_table)
    filename = str(f'{lst_of_all_condition[i]}_drugs.txt')
    filename = filename.replace("/"," ")
    file = open(filename, 'a+')
    i+=1
    if(drug_table==None):
        continue
    rows = drug_table.find_all('tr')[1:]
    for row in rows:
        drug_cells = row.find('td')
        print(drug_cells)
        drug_name = drug_cells.find('a',{'class':'condition-table__drug-name__link'})
        if(drug_name!=None):
            drug_name=drug_name.text
            print(drug_name)
            file.write(drug_name+"\n")