state = input()

List = state.split("-")

result = 0

for number in List[0].split("+"):
    result += int(number)

for i in range(1, len(List)):
    List2 = List[i].split("+")

    Sum = 0
    for number in List2:
        Sum += int(number)

    result -= Sum

print(result)
