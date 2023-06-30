def is_palindrome(word):
    
    word = word.replace(" ", "").lower()
    left = 0
    right = len(word) - 1
    while left < right:
    
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1
    return True

word = "madam"
result = is_palindrome(word)
if result == True:
  print("The word madam is a palindrome.")
else: 
  print("The word madam is not a palindrome.")
