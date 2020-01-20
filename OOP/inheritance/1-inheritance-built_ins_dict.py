#!/usr/bin/python3
#this clas will extend from dict class andd get all th methods of a dict and create a new dict to fill

class LongNameDict(dict):
    def longest_key(self):
        longest = None
        for key in self:
            if not longest or len(key) > len(longest):
                longest = key
        return longest

longkeys = LongNameDict()

longkeys['hello'] = 1
longkeys['longest yet'] = 5
longkeys['hello2'] = 'world'

print(longkeys.longest_key())
print(longkeys)
