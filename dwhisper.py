# import requests
# from bs4 import BeautifulSoup
#
# base_url = 'https://www.digitalwhisper.co.il/Issues'
#
# response = requests.get(base_url)
#
# soup = BeautifulSoup(response.content,features='html.parser')
# input_list = soup.findAll('a',attrs={'href':'issues'})
# print(soup.prettify())

import requests


urls = []

for i in range(1, 20):
    myhexa = hex(i)
    url = f"https://www.digitalwhisper.co.il/files/Zines/{myhexa}/DigitalWhisper{i}.pdf"
    urls.append(url)

# for url in urls:
#     print(url)

with open('urls.txt', 'w') as file:
    # Write each URL to the file
    for url in urls:
        file.write(url + '\n')

with open('urlscontent.txt', 'wb') as file:
    for url in urls:
        response = requests.get(url)
        content = response.content
        file.write(content)
        file.write(b'\n---\n')

