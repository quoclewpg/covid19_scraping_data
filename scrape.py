import requests
import re

from twilio.rest import Client
from bs4 import BeautifulSoup

# Your Account SID from twilio.com/console
account_sid = "AC8672ae56238820de18b0bdc80dfee2ee"
# Your Auth Token from twilio.com/console
auth_token  = "819613a2de357c4da7cea746fee381e2"
client = Client(account_sid, auth_token)

response = requests.get('https://www.gov.mb.ca/health/')
soup = BeautifulSoup(response.text, 'html.parser');
news = soup.findAll('p')

for i in reversed(range(len(news)-2)):
	link_news = news[i]
	covid_cases = link_news.contents[0].text
	date = link_news.em.text
	if("COVID-19 Bulletin" in covid_cases):
		link = requests.get(link_news.a['href'])
		soup_link = BeautifulSoup(link.text, 'html.parser')
		for paragraph in soup_link.select('.content-section'):
			announcement = paragraph.div.text
			match = re.search(r'(\S+) new', announcement)
			if match:
				cases = match.group(1)
sms_body = date + ", Manitoba has " + cases + " new case(s)."

message = client.messages.create(
    to="+12049156184", 
    from_="+12058989300",
    body="Hello, on " + sms_body)
