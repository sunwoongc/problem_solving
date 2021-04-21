def LongestWord(sen):
    words = ""
    for char in sen:
      if char.isalpha() or char.isnumeric():
        words += char
      else :
        words += " "
    return max(words.split(),key=len)
print(LongestWord(input()))

## 정규식 표현으로 풀어보자.
