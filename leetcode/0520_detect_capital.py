# Given a word, you need to judge whether the usage of capitals in it is right or not.

# We define the usage of capitals in a word to be right when one of the following cases holds:

# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital, like "Google".
# Otherwise, we define that this word doesn't use capitals in a right way.

def detectCapitalUse(word):
  def is_capital(letter):
    return (letter < 'a')

  def check_case(word, is_cap):
    for n in word:
      if is_capital(n) != is_cap:
        return False
    return True
  
  if len(word) < 2:
    return True

  if is_capital(word[0]):
    return check_case(word[2:], is_capital(word[1]))
  else: 
    return check_case(word[1:], False)
  

print(detectCapitalUse("Flag"))
print(detectCapitalUse("flag"))
print(detectCapitalUse("USA"))
print(detectCapitalUse("fLag"))
