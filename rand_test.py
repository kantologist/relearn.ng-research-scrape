from selenium import webdriver
import os
import requests
from bs4 import BeautifulSoup
import logging
import csv
from settings import *

#chromedriver = r'C:\Users\Oluwafemi\Downloads\chromedriver_win32\chromedriver'
#os.environ["webdriver.chrome.driver"] = chromedriver
#browser = webdriver.Chrome(chromedriver)

# for escaping urllib3 warnings about insecure platform
logging.captureWarnings(True)

def write_and_request(f,fieldnames,url):
    writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
    writer.writeheader()
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    return writer,soup

def test_un(url, filepath):
    #f = open('test/un_data.csv','wb')
    f = open(filepath, 'ab')
    fieldnames = ['Header', 'Link']
    writer,soup = write_and_request(f,fieldnames,url)

    # test header
    header = soup.select('.Result > h2')
    #print(header[0].getText())

    # test link
    url_link = 'http://data.un.org/'
    link = soup.select('.Result > h2 > a')
    #print (link[0].get('href'))

    for i in range(len(header)):
        writer.writerow({'Header': header[i].getText().encode('utf-8'),
                         'Link':'=HYPERLINK("%s","more details")' %(url_link+link[i].get('href'))})
        print(i)
    f.close()

#test_un(un_data_url)
def test_undp(url, filepath):
    #f = open('test/undp_data.csv', 'wb')
    f = open(filepath, 'ab')
    fieldnames = ['Header','Description','Link']
    writer, soup = write_and_request(f, fieldnames, url)

    # test header
    header = soup.select('.overlay-wrap > a')
    #print(header[0].getText())

    # test description
    desc = soup.select('.overlay-wrap > p')
    #print(desc[0].getText())

    # test Link
    link = soup.select('.overlay-wrap > a')
    #print(link[0].get('href'))

    for i in range(len(header)):
        writer.writerow({'Header': header[i].getText().encode('utf-8'),
                         'Description': desc[i].getText().encode('utf-8'),
                         'Link':'=HYPERLINK("%s","more details")' %(url+link[i].get('href'))})
        print(i)
    f.close()

#test_undp(undp_data_url)

def test_sdkp(url,filepath):
    #f = open('test/sdkp_data.csv', 'wb')
    f = open(filepath, 'ab')
    fieldnames = ['Header','Date','Description', 'Link']
    writer, soup = write_and_request(f, fieldnames, url)

    # test header
    header = soup.select('.hboxTitle')
    #print(header[0].getText())
    #print(len(header))

    # test description
    desc = soup.select('.hboxText')
    #print(desc[0].getText())
    #print(len(desc))

    # test Date
    date = soup.select('.hboxText > span')
    # print(len(date))
    # print(date[0].getText())

    # test Link
    url_link = 'https://sustainabledevelopment.un.org'
    link = soup.select('#contentArea > a')
    #print(link[0].get('href'))
    #print(len(link))

    for i in range(len(header)):
        writer.writerow({'Header': header[i].getText().encode('utf-8'),
                         'Date': date[i].getText().encode('utf-8'),
                         'Description': desc[i].getText().encode('utf-8'),
                         'Link': '=HYPERLINK("%s","more details")' % (url_link + link[i].get('href'))})
        print(i)
    f.close()

#test_sdkp(sdkp_data_url)

def test_world_bank(url, filepath):
    f = open(filepath, 'ab')
    fieldnames = ['Header', 'Date', 'Description', 'Link']
    writer, soup = write_and_request(f, fieldnames, url)

    url_link = 'https://openknowledge.worldbank.org'


    # Test The heading
    header = soup.select('.item-metadata > .content > h4')
    #print(header[9].getText())

    #  Test body
    description = soup.select('.item-metadata > .artifact-info .hidden-xs')
    #print(description[9].getText())

    #  test date
    date = soup.select('.item-metadata > .date-info')
    # print(date[9].getText())

    #  test link
    link = soup.select('.item-metadata > .content > h4 > a')
    #test_link = link[9].get('href')
    #print (url_link+test_link)

    #  test writing into csv

    for i in range(len(header)):
        test_link = link[i].get('href').strip()
        real_link = url_link + test_link
        writer.writerow({'Header':header[i].getText().encode('utf-8'),
                     'Description':description[i].getText().encode('utf-8'),
                     'Date':date[i].getText().encode('utf-8').strip(),
                     'Link':'=HYPERLINK("%s","more details")'%(real_link)
                     })
        print (i)
    f.close()

def test_uk(url, filepath):
    #f = open('test/uk_data.csv', 'wb')
    f = open(filepath, 'ab')
    fieldnames = ['Header', 'Date', 'Description', 'Link']
    writer, soup = write_and_request(f, fieldnames, url)

    # test header
    header = soup.select('.results-list > li > h3')
    #print(header[0].getText())
    #print(len(header))

    # test description

    desc = soup.select('.results-list > li > p')
    #print(desc[0].getText())
    #print(len(desc))

    # test Date
    attr = soup.select('.results-list > li')
    print(len(attr))
    date_list=[]
    for att in attr:
        try:
            date = att.select('.attributes > li')
            date_list.append(date[0].getText().encode('utf-8'))
            #print(date[0].getText())
        except:
            date_list.append('none')
            #print('none')
    # test Link
    url_link = 'https://www.gov.uk'
    link = soup.select('.results-list > li > h3 > a')
    #print(url_link+link[0].get('href'))
    #print(len(link))

    for i in range(len(header)):
        writer.writerow({'Header': header[i].getText().encode('utf-8'),
                         'Date': date_list[i],
                         'Description': desc[i].getText().encode('utf-8'),
                         'Link': '=HYPERLINK("%s","more details")' % (url_link + link[i].get('href'))})
        print(i)
    f.close()

#test_uk('https://www.gov.uk/search?q=Nigeria+education&show_organisations_filter=true')

def test_ilo(url, filepath):
    #f = open('test/ilo_data.csv', 'wb')
    f = open(filepath, 'ab')
    fieldnames = ['Header', 'Date', 'Description', 'Link']
    writer, soup = write_and_request(f, fieldnames, url)

    # test header
    header = soup.select('.doc > h2')
    #print(header[0].getText().encode('utf-8').strip())
    #print(len(header))

    # test description
    desc = soup.select('.doc > .teaser')
    #print(desc[0].getText().encode('utf-8'))
    #print(len(desc))

    # test Date
    dates = soup.select('.doc > .link')
    date = []
    for dat in dates:
        date.append(dat.select('span')[0].getText().encode('utf-8'))
    #print(len(date))
    #print(date[0])

    # test Link
    link = soup.select('.doc > h2 > a')
    print(link[0].get('href'))
    print(len(link))

    for i in range(len(header)):
        writer.writerow({'Header': header[i].getText().encode('utf-8'),
                         'Date': date[i],
                         'Description': desc[i].getText().encode('utf-8'),
                         'Link': '=HYPERLINK("%s","more details")' % (link[i].get('href'))})
        print(i)
    f.close()

#test_ilo(ilo_data_url)

def test_oecd(url, filepath):
    #f = open('test/oecd_data.csv', 'wb')
    f = open(filepath, 'ab')
    fieldnames = ['Header', 'Date', 'Description', 'Link']
    writer, soup = write_and_request(f, fieldnames, url)

    # test header
    header = soup.select('.block > h4')
    #print(header[0].getText())
    #print(len(header))

    # test description
    desc = []
    describe = soup.select('.block')
    for des in describe:
        desc.append(des.select('p')[0].getText().encode('utf-8'))
    #print(len(desc))

    # test Date
    date = soup.select('.date')
    #print(len(date))
    #print(date[0].getText())

    # test Link
    url_link = 'https://www.oecd.org'
    link = soup.select('.block > h4 > a')
    #print(link[0].get('href'))
    #print(len(link))

    for i in range(len(header)):
        writer.writerow({'Header': header[i].getText().encode('utf-8'),
                         'Date': date[i].getText().encode('utf-8'),
                         'Description': desc[i],
                         'Link': '=HYPERLINK("%s","more details")' % (url_link + link[i].get('href'))})
        print(i)
    f.close()

#test_oecd(oecd_data_url)

def test_nigerian_stat(url):
    f = open('test/ng_stat_data.csv', 'wb')
    fieldnames = ['Header','Link']
    writer, soup = write_and_request(f, fieldnames, url)

    # test header
    header = soup.select('#report > .col-md-4')
    #print(header[0].getText())
    print(len(header))

    # test Link
    #url_link = 'https://sustainabledevelopment.un.org'
    #link = soup.select('#contentArea > a')
    # print(link[0].get('href'))
    # print(len(link))

    #for i in range(len(header)):
    #    writer.writerow({'Header': header[i].getText().encode('utf-8'),
    #                     'Link': '=HYPERLINK("%s","more details")' % (url_link + link[i].get('href'))})
    #    print(i)
    f.close()

#test_nigerian_stat(nigerian_stat_data_url)

def test_nigerian_portal(url):
    f = open('test/ng_portal_data.csv', 'wb')
    fieldnames = ['Header', 'Date', 'Description', 'Link']
    writer, soup = write_and_request(f, fieldnames, url)

    # test header
    header = soup.select('#home-content > ')
    #print(header[0].getText())
    print(len(header))

    # test description
    #desc = soup.select('.hboxText')
    # print(desc[0].getText())
    # print(len(desc))

    # test Date
    #date = soup.select('.hboxText > span')
    # print(len(date))
    # print(date[0].getText())

    # test Link
    #url_link = 'https://sustainabledevelopment.un.org'
    #link = soup.select('#contentArea > a')
    # print(link[0].get('href'))
    # print(len(link))

    #for i in range(len(header)):
    #    writer.writerow({'Header': header[i].getText().encode('utf-8'),
    #                     'Date': date[i].getText().encode('utf-8'),
    #                     'Description': desc[i].getText().encode('utf-8'),
    #                     'Link': '=HYPERLINK("%s","more details")' % (url_link + link[i].get('href'))})
    #    print(i)
    #f.close()
#test_nigerian_portal(nigeria_dataportal_url)

def test_en_unesco(url, filepath):
    f = open('test/en_unesco_data.csv', 'wb')
    f = open (filepath, 'ab')
    fieldnames = ['Header', 'More Info', 'Description', 'Link']
    writer, soup = write_and_request(f, fieldnames, url)

    # test header
    header = soup.select('.search-result > h3')
    #print(header[0].getText())
    #print(len(header))

    # test description
    describe = soup.select('.search-result > div')
    desc=[]
    for des in describe:
        desc.append(des.select('p')[0].getText().encode('utf-8'))
    #print(desc[9])
    #print(len(desc))

    # test Date
    describe = soup.select('.search-result > div')
    date = []
    for des in describe:
        date.append(des.select('p')[1].getText().encode('utf-8'))
    #print(len(date))
    #print(date[0])

    # test Link
    link = soup.select('.search-result > h3 > a')
    #print(link[0].get('href'))
    #print(len(link))

    for i in range(len(header)):
        writer.writerow({'Header': header[i].getText().encode('utf-8'),
                         'More Info': date[i],
                         'Description': desc[i],
                         'Link': '=HYPERLINK("%s","more details")' % (link[i].get('href'))})
        print(i)
    f.close()
#test_en_unesco(en_unesco_data_url+'?page=1')
def test_uis_unesco(url, filepath):
    #f = open('test/uis_unesco_data.csv', 'wb')
    f = open(filepath, 'ab')
    fieldnames = ['Header','Description', 'Link']
    writer, soup = write_and_request(f, fieldnames, url)

    # test header
    header = soup.select('.unesco-srch-Title > a')
    #print(header[0].getText())
    #print(len(header))

    # test description
    desc = soup.select('.unesco-srch-Description')
    #print(desc[0].getText().encode('utf-8'))
    #print(len(desc))

    # test Link
    link = soup.select('.unesco-srch-Title > a')
    #print(link[0].get('href'))
    #print(len(link))

    for i in range(len(header)):
        writer.writerow({'Header': header[i].getText().encode('utf-8'),
                         'Description': desc[i].getText().encode('utf-8'),
                         'Link': '=HYPERLINK("%s","more details")' % (link[i].get('href'))})
        print(i)
    f.close()
#test_uis_unesco(uis_unesco_data_url)
def test_unesco(url, filepath):
    #f = open('test/unesco_data.csv', 'wb')
    f = open(filepath, 'ab')
    fieldnames = ['Header', 'Date','Link']
    writer, soup = write_and_request(f, fieldnames, url)

    # test header
    headers = soup.select('.newsList')
    head = headers[0].select('li')
    header = []
    for hed in head:
        header.append(hed.select('p')[1].getText().encode('utf-8'))
    #print(header[31])
    #print(len(header))

    # test Date
    date = []
    for hed in head:
        date.append(hed.select('p')[0].getText().encode('utf-8'))
    #print(len(date))
    #print(date[0])

    # test Link
    url_link = 'http://www.unesco.org/new/'
    link = []
    for hed in head:
        link.append(hed.select('p')[1].select('a')[0].get('href'))
    #print(link[31])
    #print(len(link))

    for i in range(len(header)):
        writer.writerow({'Header': header[i],
                         'Date': date[i],
                         'Link': '=HYPERLINK("%s","more details")' % (url_link + link[i])})
        print(i)
    f.close()
#test_unesco(unesco_data_url)