# from queue import Queue

f = open('sample.txt')

prev_length = 5
# q = Queue(maxsize = prev_length)
prev_nums = []
count = 0

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
            print(x, count, prev_nums)
            break
    prev_nums.append(int(x))
    count += 1 

