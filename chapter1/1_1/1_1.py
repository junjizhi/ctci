# simplest way: use a hash table <letter, count> 

# If not using a data structure, a brute force way is to try to find each letter in substring without that letter. the complexity is O(n^2). 

# implementation with an dict
def isAllUnique(string):
    allChars = {}
    # go over each char
    for c in string:
        if c in allChars:
            return False
        allChars[ c ] = True
    return True

s1 = "asdfasdfasasdfas"
s2 = "12345679"
s3 = "12345671"
s4 = "1234abcd567AB"
print s1, 'is', isAllUnique(s1)
print s2, 'is', isAllUnique(s2)
print s3, 'is', isAllUnique(s3)
print s4, 'is', isAllUnique(s4)


# Solutions that I have not thought of: 
# 1. trading space for time. Assume we only have 256 ascii letters, then we use an array of 256 to record the occurrence. So the time complexity is O(n)
# 2. If we can modify the input string, we can sort string by letters and count the neighbouring letters. The complexity is O(nlogn)

# remaining question: Is using a hash table more efficient than an array?
