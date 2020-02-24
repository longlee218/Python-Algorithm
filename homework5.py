
string = 'abcbbabca'
k = 3
index = int(len(string) / k)
for i in range(index):
   current = string[k * i:(i + 1) * k]
   print("".join(list(set(current))))
