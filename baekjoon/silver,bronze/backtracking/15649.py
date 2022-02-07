n, m = map(int, input().split())

result = []
def dfs():
  if len(result)==m:
    for ele in result:
      print(ele, end = ' ')
    print()
  for i in range(1, n+1):
    if i not in result:
      result.append(i)
      dfs()
      result.pop()

dfs()