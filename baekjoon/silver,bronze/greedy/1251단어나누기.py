word = input()
words = []

for i in range(len(word)-2):
    for j in range(i + 1, len(word)-1):
        words.append(word[i::-1] + word[j:i:-1] + word[:j:-1])

print(min(words))
