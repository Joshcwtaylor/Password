user_information = {
    "Joe": 200,
    "Bob": 100,
    "Sam": 300,

}

user_information = dict(sorted(user_information.items(), key=lambda x: x[1], reverse=True))

print(user_information)

def sorting(filename):
  infile = open(filename)
  words = []
  for line in infile:
    temp = line.split()
    for i in temp:
      words.append(i)
  infile.close()
  words.sort()
  outfile = open("result.txt", "w")
  for i in words:
    outfile.writelines(i)
    outfile.writelines(" ")
  outfile.close()
sorting("sample.txt")

