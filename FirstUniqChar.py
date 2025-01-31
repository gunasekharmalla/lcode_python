
class Solution(object):
    def firstUniqChar(self, name):
     dictionary = {char :0 for char in name}
     for char in name:
        if char in dictionary:
            dictionary[char] += 1
     for element in name:
        if dictionary[element] ==1:
            return name.find(element)
     return -1
