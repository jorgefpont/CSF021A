# grabs 3 dictionaries containing shopping lists and merges them into one shopping list/dictionary

# NOTE: I have added vodka to dict 2 to test the case of repeated values, both in lists
# NOTE: I have added apples to dict 3 to test the case of repeated values, one in list an one not

rs1 = {'fruit': 'apples', 'meat': 'chicken', 'vegetables': 'potatoes', 'drinks': ['beer','wine','vodka'],\
        'dessert': 'ice cream'}
rs2 = {'fruit': 'lemons', 'meat': 'hamburger', 'drinks': ['apple juice', 'orange juice', 'vodka']}
rs3 = {'fruit': ['apples','oranges', 'bananas'], 'vegetables': ['lettuce', 'carrots'], 'drinks': 'milk'}

# create a list of shopping lists/dicts
inputLists2 = [rs1, rs2, rs3]

mergedList2 = {}  # new dict to merge the individual dicts
for l in inputLists2:  # loop thru the individual lists
    for k in l:  # loop thru keys in dict

        # if the key is already in the merged list,
        if (k in mergedList2) == True:

            # if value for k in input list is a list
            # and value for k in merged list is a list
            if type(l[k]) == list and type(mergedList2[k]) == list:
                mergedList2[k].extend(l[k])

            # if value for  k in input list is a list
            # and value for k in merged list is not a list
            elif type(l[k]) == list and type(mergedList2[k]) != list:
                mergedList2[k] = [mergedList2[k]]
                mergedList2[k].extend(l[k])

            # if value for k in input list is not a list
            # and value for k in merged list is a list
            elif type(l[k]) != list and type(mergedList2[k]) == list:
                l[k] = [l[k]]
                mergedList2[k].extend(l[k])

            # if value for k in input list is not a list
            # and value for k in merged list is not a list
            elif type(l[k]) != list and type(mergedList2[k]) != list:
                mergedList2[k] = [mergedList2[k], l[k]]

        # if the key not in the merged list
        # does not matter if the value is a list or not

        else:
            mergedList2[k] = l[k]

print('===== MERGED LIST/DICT:')
print(mergedList2)


'''/home/jorge/module3exercise/bin/python /home/jorge/csf021a/module3exercise/hwk3b.py
===== MERGED LIST/DICT:
{'fruit': ['apples', 'lemons', 'apples', 'oranges', 'bananas'], 'meat': ['chicken', 'hamburger'], 'vegetables': ['potatoes', 'lettuce', 'carrots'], 'drinks': ['beer', 'wine', 'vodka', 'apple juice', 'orange juice', 'vodka', 'milk'], 'dessert': 'ice cream'}

Process finished with exit code 0'''


