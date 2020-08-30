left = 0
char_count = {}
result = 0

for i in range(len(str)):
	if str[i] not in char_count:
		char_count[str[i]] = 1
	else:
		char_count[str[i]] += 1

	while len(char_count) > k:
		char_count[arr[left]] -= 1
		if char_count[arr[left]] == 0: #removes the leftest char from dict
			char_count.pop(arr[left])
		left += 1
	result = max(result, i-left+1)



