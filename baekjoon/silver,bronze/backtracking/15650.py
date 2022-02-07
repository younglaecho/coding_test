n, m = map(int, input().split())

result = []
def dfs():
  if len(result)==m:
    for ele in result:
      print(ele, end = ' ')
    print()
    return

  for i in range(1, n+1):
    if len(result)==0:
      result.append(i)
      dfs()
      result.pop()
    elif i >result[-1]:
      result.append(i)
      dfs()
      result.pop()

dfs()