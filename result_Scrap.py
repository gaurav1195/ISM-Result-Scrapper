try:
    import selenium
except:
    print('Unable to import Selenium, please install selenium')
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
try:
    from bs4 import BeautifulSoup
except:
    print('Unable to import BeautifulSoup, please install beautifulsoup')
    
author = 'Author:**************GAURAV AGARWAL gauravagarwal.110695@gmail.com**********'
des = 'ISM WEBSITE Result Scrapper between any two admission numbers'
adm = input('Enter starting adm no')
adm2 = input('Enter ending adm no')

m = int(adm[6:10])
n = int(adm2[6:10])
total = n-m

if adm[3] == '1':
    z = 8
elif adm[3] == '2':
    z = 6
elif adm[3] == '3':
    z = 4
else:
    print('Result not available, Sorry')
    quit()
i=0
file_name = 'result.txt'
file = open(file_name, 'w')
file.write(author)
file.write('\n')
file.close()
print('Printing results to the file result.txt..........')
b = webdriver.Firefox()
for i in range(0, total):
    try: 
        b.get('http://www.ismdhanbad.ac.in/result/admin/result.php')
    except:
        print('Check your internet connection')
        quit()
    s = adm[6:10]
    x = int(s)
    x = x + 1;
    x = str(x)
    if len(x)!=4:
        x = '0' + x
    adm = adm[0:6] + x
    e = b.find_element_by_id('appno')
    e.clear()
    e.send_keys(adm + Keys.RETURN)
    html = b.page_source
    soup = BeautifulSoup(html, 'html.parser')
    file_name = 'result.txt'
    file = open(file_name, 'a')
    tr = soup.find_all('tr')[7]
    tds = tr.find_all('td')
    name = tds[0].find_all('table')[2]
    names = name.find_all('td')[2:5]
    for n in names:
        file.write(n.string + ' ')
        file.write('\n')
    
    if soup.body.findAll(text='Sorry, Result Not Found'):
        file.write(adm + ' ' + ' ' + ' ')
        file.write('NOt found')
        file.write('\n')
    else :
        for tr in soup.find_all('tr')[20:20+z]:
            tds = tr.find_all('td')
            file.write(tds[0].text + ' ' + tds[1].string + ' ' + tds[2].string + ' ' + tds[3].string + ' ' + tds[4].string + ' ' +  tds[5].string)
            file.write('\n')
    file.write('\n')
    file.close()
file.close()

    
