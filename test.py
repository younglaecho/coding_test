import time
start = time.time()
for i in range(100000000):
  int(8/5)
end = time.time()
print(end-start)

start = time.time()
for i in range(100000000):
  8//5
end = time.time()
print(end-start)
