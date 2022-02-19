import re
import collections

filename = input("Enter the name of the txt file that is located in the same directory as this file: ")
f = open(filename, "r")
tmp = f.read()
y = re.sub("[^a-zA-Z]+", " ", tmp) 
og_list = y.split()
lilen = len(og_list)-1
srt_li = sorted(og_list, key=len)
srt_li1 =srt_li
i = 0
z = 0
num_li = []
for i in srt_li:
	num_li.append(len(i))

final = []
(low, high) = (0, len(num_li) - 1)
while low < high:
	
	if num_li[low] + num_li[high] < 20:
		final.append(num_li[low])
		low = low + 1
	else:
		high = high - 1

occurrences = collections.Counter(final)
i = 1
for i in occurrences:
	print("There are", occurrences[i], i, "letter words left")