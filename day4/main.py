f = open('input.txt')

dict = {}
listKey = []
count = 0
keys = ["byr", "ecl", "eyr", "hcl", "hgt", "iyr", "pid"]
keys2 = ["byr", "cid", "ecl", "eyr", "hcl", "hgt", "iyr", "pid"]
# keys.sort()
# keys2.sort()

for x in f:
    if x == "\n":
        print()
        listKey.sort()
        print(listKey, listKey == keys or listKey == keys2)
        if listKey == keys or listKey == keys2:
            count+=1
        listKey = []
    else:
        split_list = x.split(" ")
        for item in split_list:
            split_item = item.split(":")
            listKey.append(split_item[0])

if len(listKey) > 0:
    listKey.sort()
    if listKey == keys or listKey == keys2:
        count+=1

print(count)