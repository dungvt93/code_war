# What is an anagram? Well, two words are anagrams of each other if they both contain the same letters. For example:
#
# 'abba' & 'baab' == true
#
# 'abba' & 'bbaa' == true
#
# 'abba' & 'abbba' == false
#
# 'abba' & 'abca' == false
# Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word and an array with words. You should return an array of all the anagrams or an empty array if there are none. For example:
#
# anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']
#
# anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']
#
# anagrams('laser', ['lazing', 'lazy',  'lacer']) => []

def anagrams(word, words): return [item for item in words if sorted(item)==sorted(word)]

def anagrams(word, words):
    result = []
    temp_dict = {}
    for character in "".join(set(word)):
        temp_dict[character] = word.count(character)
    for compare in words:
        if len(word) != len(compare):
            continue
        flg = True
        for key,value in temp_dict.items():
            if compare.count(key) != value:
                flg = False
                break
        if flg == True:
            result.append(compare)
    return result