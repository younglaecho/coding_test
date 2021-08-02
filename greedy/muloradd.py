data = input()

result = 0
for i in data:
    if result == 0:
        result += int(i)

    else:
        if int(i) == 0:
            result += int(i)
        else:
            result *= int(i)

print(result)
