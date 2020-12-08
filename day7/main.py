def getBagContains(dict, bag_color):
    current_bags = []
    if bag_color in dict:
        print(current_bags)
        for color in [x for x in dict[bag_color] if x not in current_bags]:
            current_bags += getBagContains(dict, color)
        current_bags += dict[bag_color]
        return current_bags
    return current_bags

f = open('input.txt')
looking_for = "shiny gold"

dict = {}

for x in f:
    replaced_string = x.replace(" bags contain ", "|").replace("\n", "").replace(".", "")
    split_string = replaced_string.split("|")
    contains = []
    dict_contains = []
    for comma_separated in split_string[1].split(", "):
        # print(comma_separated)
        contains.append(comma_separated)
    for word in contains:
        # print(word, contains)
        word_split = word.split(" ")
        if word_split[0] == "no":
            break
        dict_contains.append(word_split[1] + " " + word_split[2])
        # dict_contains.append(word_split[2])
    # contains = [(words.split(" ")[1] words.split(" ")[2]) for words in contains]
    for color in dict_contains:
        if color in dict:
            dict[color].append(split_string[0])
        else:
            dict[color] = [split_string[0]]
    # contains = []
    # dict_contains = []

print(dict)
starting_point = dict["shiny gold"]
contains_bag_list = getBagContains(dict, looking_for)
# count = 0
# for bagcolor in starting_point:
#     count += getBagCount(dict, bagcolor)

print(len(set(contains_bag_list)))

