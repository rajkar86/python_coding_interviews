# 848. Shifting Letters

# We have a string S of lowercase letters, and an integer array shifts.

# Call the shift of a letter, the next letter in the alphabet, (wrapping around so that 'z' becomes 'a'). 

# For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.

# Now for each shifts[i] = x, we want to shift the first i+1 letters of S, x times.

# Return the final string after all such shifts to S are applied.

S = "abc"
shifts = [3,5,9]

def shiftingLetters(S, shifts):


  n = len(shifts)
  for i in range(1,n):
    shifts[n-i-1] += shifts[n-i]

  # shifts = [s % 26 for s in shifts]

  def f(c, s):
    return chr((((ord(c) + s) - 97) % 26) + 97)

  res = [f(c,s) for c,s in zip(S,shifts)]

  return "".join(res)


print(shiftingLetters(S, shifts))

