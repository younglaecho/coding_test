string = input()
string = string.upper()
dict = {}
for alpha in string:
    if alpha in dict.keys():
        dict[alpha] = dict[alpha] + 1
    else:
        dict[alpha] = 1

max_value_keys = [k for k, v in dict.items() if max(dict.values()) == v]
if len(max_value_keys) == 1:
    print(max_value_keys[0])
else:
    print('?')
