# 71. Simplify Path
# Given an absolute path for a file (Unix-style), simplify it. Or in other words, convert it to the canonical path.

# In a UNIX-style file system, a period . refers to the current directory. Furthermore, a double period .. moves the directory up a level.

# Note that the returned canonical path must always begin with a slash /, and there must be only a single slash / between two directory names. The last directory name (if it exists) must not end with a trailing /. Also, the canonical path must be the shortest string representing the absolute path.


path = "/a//b////c/d//././/.."

def simplifyPath(path: str) -> str:
  s = []
  for w in path.split("/"):
    if w == "." or w == "": continue
    if w == "..": 
      if s: s.pop()
      continue
    s.append(w)
  
  return "/" + "/".join(s)
  
print(simplifyPath(path))