import requests
from bs4 import BeautifulSoup
import csv

page = requests.get('http://eatwild.com/products/washington.html').text
soup = BeautifulSoup(page, 'lxml')

# name = soup.find_all(class_ = 'bodyMargin')

pageList = page.split()
print(pageList)


num = 1
count = 1
flag = False
for element in pageList:
    # if flag == True:
    #     count += 1
    if 'href="mailto:' in element:
        print(element.split(':')[1].split('"')[0], num)
        num += 1
    # if 'noshade>' in element:
    #     count += 1
    #     flag = True
    # if count == 4:
    #     print(element)
    #     count == 1
    #     flag = False



# localhens.com
# goforager.com
# localharvest.org/csa
