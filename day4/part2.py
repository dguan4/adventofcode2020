import re

f = open('input.txt')

dict = {}
listKey = []
count = 0
keys = ["byr", "ecl", "eyr", "hcl", "hgt", "iyr", "pid"]
keyDef = {
    "byr": lambda x: re.match('^\d{4}$', x) and 1920 <= int(x) <= 2002,
    'iyr': lambda x: re.match('^\d{4}$', x) and 2010 <= int(x) <= 2020,
    'eyr': lambda x: re.match('^\d{4}$', x) and 2020 <= int(x) <= 2030,
    'hgt': lambda x: (re.match('^\d{3}cm$', x) and 150 <= int(x.replace('cm', '')) <= 193) or (re.match('^\d{2}in$', x) and 59 <= int(x.replace('in', '')) <= 76),
    'hcl': lambda x: re.match('^#[0-9a-f]{6}$', x),
    'ecl': lambda x: x in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'),
    'pid': lambda x: re.match('^\d{9}$', x)
}
keys2 = ["byr", "cid", "ecl", "eyr", "hcl", "hgt", "iyr", "pid"]

for x in f:
    if x == "\n":
        listKey.sort()
        print(listKey, listKey == keys or listKey == keys2)
        if listKey == keys or listKey == keys2:
            count+=1
        listKey = []
    else:
        split_list = x.split(" ")
        for item in split_list:
            split_item = item.replace("\n", "").split(":")
            if split_item[0] != "cid" and keyDef[split_item[0]](split_item[1]):
                listKey.append(split_item[0])

if len(listKey) > 0:
    listKey.sort()
    if listKey == keys or listKey == keys2:
        count+=1

print(count)