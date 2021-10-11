binaries = []

def generate(n, arr, i):
  global binaries
  if n == i:
    arr= map(str, arr)
    string = ''.join(arr)
    binaries.append(string)
    return

  else:
    arr[i]=0
    generate(n, arr, i+1)
    arr[i]=1
    generate(n, arr, i+1)

n = int(input())
arr = [None]*n
generate(n, arr, 0)
for i in binaries:
  print(i)
