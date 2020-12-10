f = open('input.txt')

input = [int(x.replace("\n", "")) for x in f]
input.sort()
current = 0
volt_1 = 0
volt_3 = 0
for x in input:
    print(x, current+1, current+3)
    if x <= current+3:
        if x == current+1:
            volt_1 += 1
        elif x == current+3:
            volt_3 += 1
    current = x

volt_3 += 1 # device adapter is always 3+
print(volt_1, volt_3, volt_1*volt_3)