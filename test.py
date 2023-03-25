def find_next_value(lst):
    for i in range(len(lst)-1):
        if len(lst[i]) > 12 and lst[i][12] == "usdot":
            return lst[i+1][12]
    return None

my_list = [["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n"],
           ["o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "usdot", "12th index value"],
           ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "m", "n"]]

result = find_next_value(my_list)

if result:
    print("Value of the 12th index of the next element in the list: ", result)
else:
    print("usdot not found in any sublist")