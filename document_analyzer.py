with open('document.txt') as f:
	read_data = f.read()

list1 = read_data.split()
words = {}
for x in list1:
	if x in words:
		words[x] = words[x] + 1
	else:
		words[x] = 1
sorted_dict = {}
sorted_keys = sorted(words, key=words.get)
counter = 0
counter1 = 0
final = {}
n = len(words)
for i in sorted_keys:
	sorted_dict[i] = words[i]
	counter1 = counter1 + 1
	if counter1 == n-4:
		final[i] = sorted_dict[i]
		n = n + 1
keys_list = list(final.keys())
values_list = list(final.values())

for w in range(5):
	for p in range(w+1, 5):
		if (values_list[w]==values_list[p]):
			if (keys_list[w]<keys_list[p]):
				temp = keys_list[w]
				keys_list[w] = keys_list[p]
				keys_list[p] = temp

print("\r")
print(f"{keys_list[4]}: {values_list[4]}")
print(f"{keys_list[3]}: {values_list[3]}")
print(f"{keys_list[2]}: {values_list[2]}")
print(f"{keys_list[1]}: {values_list[1]}")
print(f"{keys_list[0]}: {values_list[0]}")

