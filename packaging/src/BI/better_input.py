def better_input (prompt: str, type: type = str):
  print(prompt)
  temp = input('>')
  while isinstance(temp, type):
    print('Invalid input')
    print(prompt)
    temp = input('>')
  return temp
