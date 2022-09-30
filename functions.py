with open('demo.txt') as myFile:
  text = myFile.read()
result = text.split('$')
for i in range(len(result)):
  print(result[i])
