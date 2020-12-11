f = open('input.txt')

input = [int(x.replace("\n", "")) for x in f]
input.append(0)
input.append(max(input)+3)
input.sort()

found = {}

# watched dp vid from jonathan paulson
# https://www.youtube.com/watch?v=cE88K2kFZn0&feature=youtu.be
# I understand this conceptually but
# still can't really wrap my head around it
def dp(i):
    # we're at the end, only one way left
    if i == len(input)-1:
        return 1
    if i in found:
        return found[i]
    ans = 0
    for j in range(i+1, len(input)):
        if input[j]-input[i] <= 3:
            ans += dp(j)
    found[i] = ans
    return ans

print(dp(0))
# current = 0
# volt_1 = 0
# volt_3 = 0

# def checkIfValid(input_list):
#     current = 0
#     for x in input_list:
#         print(x, current+1, current+3)
#         if x <= current+3:
#             if x == current+1:
#                 volt_1 += 1
#             elif x == current+3:
#                 volt_3 += 1
#         else:
#             return False
#         current = x
#     return True

# combo_count = 0
# loop_count = 0
# if checkIfValid(input_list):

# while combo_count < len(input_list):
#     new_arr = input_list
#     new_arr.pop()
#     if checkIfValid(new_arr):
#         combo_count+=1
#     checkIfValid()
    
# volt_3 += 1 # device adapter is always 3+
# print(volt_1, volt_3, volt_1*volt_3)