import requests
import hashlib
import difflib
from bs4 import BeautifulSoup
import re


from requests import Response

s = requests.Session()

r1 = s.get('https://example.com/')

soup = BeautifulSoup(r1.text, 'html.parser')
clean = re.compile('<.*?>')
regex_topics = [re.sub(clean,'', str(x)) for x in soup.find_all("p")]


re1 = r1.text
first_page = []
second_page = []

#s.post('https://spgi.wd5.myworkdayjobs.com/en-US/SPGI_Careers/login', login_detail)
r = s.get('https://example.com/')
soup2 = BeautifulSoup(r.text, 'html.parser')
regex_topics2 = [re.sub(clean,'', str(x)) for x in soup2.find_all("p")]
#print(r) # bytes of data
re2 = r.text # string ( bytes are decoded to unicode strings and vice versa)
#print(r.text)


print(hashlib.md5(re1.encode('utf-8')).hexdigest()) # hash function need unicode objects to be encoded prior and except str, r object doesnt support buffer API (error)
print(hashlib.md5(re2.encode('utf-8')).hexdigest())
# printing diff:

for line in r1:
    first_page.append(line)

for line in r:
    second_page.append(line)

#print(first_page)
print(regex_topics)
print(regex_topics2)
difference = difflib.HtmlDiff().make_file(regex_topics, regex_topics2, r, r1)
diff_report = open('policy_diff.html', 'w')
diff_report.write(difference)
diff_report.close()


