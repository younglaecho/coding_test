word = input()

if len(word)%2==1:
  print(1 if word[:int(len(word)/2)] == word[int(len(word)/2)+1:][::-1] else 0)
elif len(word)%2==0:
  print(1 if word[:int(len(word)/2)] == word[int(len(word)/2):][::-1] else 0)
