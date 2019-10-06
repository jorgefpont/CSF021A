# grabs 3 dictionaries containing shopping lists and merges them into one shopping list

# original dictionaries, modified to have 'apples' in 2 dictionaries
# to test an additional case (duplicate values)
roommate1Shopping = {'fruit': 'apples', 'meat': 'chicken', 'vegetables': 'potatoes', 'drinks': ['beer','wine','vodka'],\
                    'dessert': 'ice cream'}
roommate2Shopping = {'fruit': 'lemons', 'meat': 'hamburger', 'drinks': ['apple juice', 'orange juice', 'vodka']}
roommate3Shopping = {'fruit': ['apples','oranges', 'bananas'], 'vegetables': ['lettuce', 'carrots'], 'drinks': 'milk'}


rs1 = {'fruit': 'apples', 'meat': 'chicken', 'vegetables': 'potatoes', 'drinks': ['beer','wine','vodka'],\
                    'dessert': 'ice cream'}
rs2 = {'fruit': 'lemons', 'meat': 'hamburger', 'drinks': ['apple juice', 'orange juice', 'vodka']}
rs3 = {'fruit': ['apples','oranges', 'bananas'], 'vegetables': ['lettuce', 'carrots'], 'drinks': 'milk'}

# create a list of shopping lists
inputLists = [roommate1Shopping, roommate2Shopping, roommate3Shopping]
inputLists2 = [rs1, rs2, rs3]

# for each list,
# turn all values that are not lists into lists
# ie 'fruit': 'apples' ==> 'fruit': ['apples']
for l in inputLists:
    for key in l:
        if type(l[key]) != list:
            l[key] = [l[key]]

mergedList = {}  # new list to merge the individual lists

for l in inputLists:  # loop thru the individual lists
    for k in l:  # loop thru keys in list
        # if the key is already in the merged list,
        # extent (a list method) the value
        if (k in mergedList) == True:
            mergedList[k].extend(l[k])
        # if the key not in the merged list
        # add the key-value
        else:
            mergedList[k] = l[k]

print('===== MERGED LIST:')
print(mergedList)

### SECOND VERSION WITHOUT CONVERTING TO LISTS

#for l in inputLists2:  # loop thru the individual lists
#    print(l)

mergedList2 = {}  # new list to merge the individual lists
for l in inputLists2:  # loop thru the individual lists
    for k in l:  # loop thru keys in list

        # if the key is already in the merged list,

        if (k in mergedList2) == True:

            # if value for k in input list is a list
            # and value for k in merged list is a list
            if type(l[k]) == list and type(mergedList2[k]) == list:
                mergedList2[k].extend(l[k])
#                print('a',mergedList2[k])

            # if value for  k in input list is a list
            # and value for k in merged list is not a list
            elif type(l[k]) == list and type(mergedList2[k]) != list:
 #               print('l[k] =', l[k])
#              print('mergedList2[k] = ', mergedList2[k])
                mergedList2[k] = [mergedList2[k]]
                mergedList2[k].extend(l[k])
#                print('b',mergedList2[k])
            # if value for k in input list is not a list
            # and value for k in merged list is a list
            elif type(l[k]) != list and type(mergedList2[k]) == list:
                l[k] = [l[k]]
                mergedList2[k].extend(l[k])
#               print('c',mergedList2[k])
            # if value for k in input list is not a list
            # and value for k in merged list is not a list
            elif type(l[k]) != list and type(mergedList2[k]) != list:
                mergedList2[k] = [mergedList2[k], l[k]]
#                print('d',mergedList2[k])
        # if the key not in the merged list
        # does not matter if the value is a list or not

        else:
            mergedList2[k] = l[k]

print('===== MERGED LIST:')
print(mergedList2)





