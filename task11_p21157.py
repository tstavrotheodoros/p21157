import requests
from scipy.stats import entropy
import pandas as pd

r = requests.get('https://drand.cloudflare.com/public/latest', headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = r.json()
tmp_round = data["round"]
random = ""
for i in range(20):
	step = tmp_round-i
	add =str(step)
	b = requests.get('https://drand.cloudflare.com/public/' + add, headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
	datatmp = b.json()
	f = datatmp["randomness"]
	random += f
num = int(random, 16)
conv = hex(num)
li = list(conv)

series = pd.Series(li)
counts = series.value_counts()
ent = entropy(counts)

print("The entropy is:",ent)