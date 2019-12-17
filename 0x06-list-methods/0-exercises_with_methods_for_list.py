#!/usr/bin/python3

cat = ['Hello', 'world', 'Soda', 'mountain']
sorting = [1, 5, -19, 65, 92]

#get the index of a specific element with his value
print(cat)
print('new index at: {}'.format( str(cat.index('world'))))
print(cat)
print()


#set a new value at the end of the list-value
print(cat)
cat.append('Mouse')
print('append: [-1] ' + cat[-1])
print()

#Insert a new value in a specific key in list-value
print(cat)
cat.insert(1, 'Techno')
print('insert: [1] ' + cat[1])
print()

#remove a value froma list-value
print(cat)
cat.remove('Mouse')
print('remove: Mouse')
print()

#sort values from a list, with numbers the less to top, and with 
#string values in alpha order
print(cat)
cat.sort()
print(cat)
print()

print(sorting)
sorting.sort()
print(sorting)
print()

#also can sort in reverse order useing the 'reverse' keyword
print(cat)
cat.sort(reverse=True)
print(cat)
print()

#to sort alphabetic using order of lower-case first
print(cat)
cat.sort(key=str.lower)
print(cat)
print()
