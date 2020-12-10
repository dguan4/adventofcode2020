# from queue import Queue

f = open('input.txt')

prev_length = 25
# q = Queue(maxsize = prev_length)
prev_nums = []
count = 0
invalid = 0

for x in f:
    if count >= prev_length:
        start_index = -prev_length
        start_index_plus_one = start_index+1
        # print(count, prev_length, start_index)
        prev_length_nums = prev_nums[start_index_plus_one:]
        test = prev_nums[start_index:]
        print(test, prev_length_nums)
        found = False
        for item in prev_nums[start_index:]:
            if int(x) - item in prev_length_nums:
                found = True
        if found == False:
            invalid = int(x)
            print(x)
            break
    prev_nums.append(int(x))
    count += 1 

start = 0
end = count-1

def checkSum(list, start, end, check_num):
    return sum(list[start:end]) == check_num

# perform sliding window calc
while start < count-1:
    if checkSum(prev_nums, start, end, invalid):
        print(start, end, max(prev_nums[start:end]))
        break
    while end > start:
        end -= 1
        if checkSum(prev_nums, start, end, invalid):
            print(start, end, min(prev_nums[start:end]) + max(prev_nums[start:end]))
            break
    end = count-1
    start += 1