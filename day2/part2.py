f = open('input.txt')

count = 0

for x in f:
    passwordList = x.split()
    times_char = passwordList[0].split("-")
    lookup_char = passwordList[1].split(":")[0]
    count_char = 0
    print(passwordList)
    if passwordList[2][int(times_char[0])-1] == lookup_char:
        count_char += 1
    if passwordList[2][int(times_char[1])-1] == lookup_char:
        count_char += 1
    if count_char == 1:
        count+=1

print(count)