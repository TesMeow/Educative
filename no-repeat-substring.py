def non_repeat_substring(str):
  left = 0
  char_count = {}
  result = 0

  for i in range(len(str)):
    if str[i] not in char_count or char_count[str[i]] < left :
      char_count[str[i]] = i
    else:
      left = char_count[str[i]]+1
    result = max(result, i - left + 1)
  return result


