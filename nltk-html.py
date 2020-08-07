import urllib.request
import urllib.error
import re
import chardet
import nltk
from bs4 import BeautifulSoup

response = urllib.request.urlopen('http://python.org/')

html = response.read()
encode_type = chardet.detect(html)
html = html.decode(encode_type['encoding'])

soup = BeautifulSoup(html, 'html.parser', from_encoding="utf-8")


# cleaned_html = nltk.clean_html(html)
cleaned_html = soup.get_text()
tokens = [tok for tok in cleaned_html.split()]
print(tokens[:100])
print()

freq_dist_nltk = nltk.FreqDist(tokens)
print(freq_dist_nltk)

for k, v in freq_dist_nltk.items():
  print(str(k) + ": " + str(v))

freq_dist_nltk.plot(50, cumulative=False)
