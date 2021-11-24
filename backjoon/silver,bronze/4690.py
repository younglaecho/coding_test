
for a in range(1, 101):
  # breaked = False
  for i in range(2, 101):
    for j in range(i+1, 101):
      for k in range(j+1, 101):
        if a**3 == i**3 +j**3 +k**3:
          print(f'Cube = {a}, Triple = ({i},{j},{k})')
          # breaked = True
    #       break
    #   if breaked:
    #     break
    # if breaked:
    #   break