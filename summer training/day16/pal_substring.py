'''input:abdbsdabca
output:bdb'''
def expand(s, l, r):
    while l>= 0 and r < len(s) and s[l] == s[r]:
        l-= 1
        r+= 1
    return l + 1, r- 1

def longest_palindromic_substring(s):
    if not s:
        return ""

    start, end = 0, 0

    for i in range(len(s)):
        l1, r1 = expand(s, i, i)
        l2,r2 = expand(s, i, i + 1)
        if r1-l1 > end - start:
            start, end = l1, r1
        if r2 - l2 > end - start:
            start, end = l2, r2

    return s[start:end + 1]
s1= "abdbsdabca"
output_str = longest_palindromic_substring(s1)
print(output_str)  
