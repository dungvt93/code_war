# The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.
#
# Examples
# "din"      =>  "((("
# "recede"   =>  "()()()"
# "Success"  =>  ")())())"
# "(( @"     =>  "))(("

import itertools
def duplicate_encode(word):
    result = ""
    word = word.lower()
    for c in word:
        if word.count(c) > 1:
            result += ")"
        else:
            result += "("
    return result
print(duplicate_encode("mHkGwFFxT!bc(lSGcG G)akmwQu"))


# OR
def duplicate_encode(word):
    word = word.lower()
    return ''.join('(' if word.count(x) == 1 else ')' for x in word)