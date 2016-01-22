
def anagram(s1, s2):
    if sorted(s1) == sorted(s2):
        return True
    else:
        return False

s1 = "abcd"
s2 = "adcb"
s3 = "bbdc"
s4 = "acdeb"
s5 = "dcba"

print s1, s2, "Anagram(T/F)", anagram(s1,s2)
print s1, s3, "Anagram(T/F)", anagram(s1,s3)
print s1, s4, "Anagram(T/F)", anagram(s1,s4)
print s1, s5, "Anagram(T/F)", anagram(s1,s5)
