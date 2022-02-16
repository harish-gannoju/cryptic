import requests

import re

from bs4 import BeautifulSoup

modified_news=[]
main_url="https://thehackernews.com/"

web_page = requests.get(main_url)

soup = BeautifulSoup(web_page.text, 'html.parser')

clean = re.compile('<.*?>')

#print(soup.prettify()[:1000]) ## this is to make html page look better pretty():

#print(soup.find("h2", class_ = "home-title" )) ##to find only first matching html part

#print(soup.find_all("h2", class_ ="home-title")) ## prints list of matching parts/contents

topics = [x for x in soup.find_all("h2", class_ = "home-title")] ## saves list as topics list
# topics vs regex_topics: best way of maipulating items in list and creating new list
regex_topics = [re.sub(clean,'', str(x)) for x in soup.find_all("h2", class_ = "home-title")]

print("Today\'s headlines:")

for news in topics:
    modified_news.append(re.sub(clean,'', str(news))) # to remove html tags with regex on each string object of list
print("\n".join(modified_news))
# both works: regex_topics is better way of doing:
#print("\n".join(regex_topics))



