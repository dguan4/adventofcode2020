f = open('input.txt')

count = 0

for x in f:
    passwordList = x.split()
    times_char = passwordList[0].split("-")
    lookup_char = passwordList[1].split(":")[0]
    count_char = passwordList[2].count(lookup_char)
    if count_char >= int(times_char[0]) and count_char <= int(times_char[1]):
        count+=1

print(count)