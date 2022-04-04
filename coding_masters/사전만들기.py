n = int(input())
Set = set()

for _ in range(n):
    Set.add(input())

words = list(Set)
words.sort(key=lambda x: (len(x), x))

for word in words:
    print(word)
