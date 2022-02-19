import requests


r = requests.get('https://drand.cloudflare.com/public/latest', headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = r.json()
tmp_round = data["round"]
random = ""
for i in range(100):
	step = tmp_round-i
	add =str(step)
	b = requests.get('https://drand.cloudflare.com/public/' + add, headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
	datatmp = b.json()
	f = datatmp["randomness"]
	random += f
num = int(random, 16)
conv = bin(num)
conv1 = conv[2:]
conv0 = conv1
max1 = max(map(len, conv1.split('0')))
max0 = max(map(len, conv1.split('1')))
print("The maximum number of consecutive 1's is", max1)
print("The maximum number of consecutive 0's is", max0)