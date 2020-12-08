getBagContainsDict = {}

def getBagContains(dict, dict_count, bag_color):
    current_bags = []
    count = 0
    if bag_color in dict:
        for color in dict[bag_color]:
            getBagsReturn = {}
            if color in getBagContainsDict:
                getBagsReturn = getBagContainsDict[color]
            else:
                getBagsReturn = getBagContains(dict, dict_count, color)
                getBagContainsDict[color] = getBagsReturn
            current_bags += getBagsReturn[0]
            count += getBagsReturn[1]
        current_bags += dict[bag_color]
        if bag_color in dict_count:
            count += dict_count[bag_color]
        return (current_bags, count)
    return (current_bags, count)

f = open('sample.txt')
looking_for = "shiny gold"

dict = {}
dict_count = {}

for x in f:
    replaced_string = x.replace(" bags contain ", "|").replace("\n", "").replace(".", "")
    split_string = replaced_string.split("|")
    contains = []
    dict_contains = []
    for comma_separated in split_string[1].split(", "):
        contains.append(comma_separated)
    for word in contains:
        word_split = word.split(" ")
        if word_split[0] == "no":
            break
        word_split_join = word_split[1] + " " + word_split[2]
        dict_contains += [word_split_join]*int(word_split[0])
        print(dict_contains)
        if split_string[0] in dict_count:
            dict_count[split_string[0]] += int(word_split[0])
        else:
            dict_count[split_string[0]] = int(word_split[0])
    dict[split_string[0]] = dict_contains

contains_bag_list = getBagContains(dict, dict_count, looking_for)
print(contains_bag_list[1])

