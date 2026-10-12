def countChar(ch, s):       
    n = 0                   
    i = 0                   
    while i < len(s):      
        if s[i] == ch:
            n = n + 1
        i = i + 1          
    return n


def isPalindrome(s):        
    left = 0
    right = len(s) - 1
    while left < right:     
        if s[left] != s[right]:
            return False
        left = left + 1
        right = right - 1
    return True


word = "deed"
print("จำนวน d =", countChar("d", word))     
print("palindrome =", isPalindrome(word))   