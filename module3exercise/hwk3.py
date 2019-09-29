# grabs 3 dictionaries containing shopping lists and merges them into one shopping list

# original dictionaries, modified to have 'apples' in 2 dictionaries
# to test an additional case (duplicate values)
roommate1Shopping = {'fruit': 'apples', 'meat': 'chicken', 'vegetables': 'potatoes', 'drinks': ['beer','wine'],\
                    'dessert': 'ice cream'}
roommate2Shopping = {'fruit': 'lemons', 'meat': 'hamburger', 'drinks': ['apple juice', 'orange juice', 'vodka']}
roommate3Shopping = {'fruit': ['apples','oranges', 'bananas'], 'vegetables': ['lettuce', 'carrots'], 'drinks': 'milk'}

# create a list of shopping lists
inputLists = [roommate1Shopping, roommate2Shopping, roommate3Shopping]

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







