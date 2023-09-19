# Trie
# You cab do Trie = lambda: collections.defaultdict(Trie)
# prefix and suffix, option 1. paired trie, for "apple" store ("a", "e"), ("a", None"), (None "e") 
# prefix and suffix, option 2. for "apple", store from "apple", "e#apple", ..., "apple#apple"

class Trie(object):

  def __init__(self):
    # T = lambda: defaultdict(T)
    # self.root = T()
    self.root = {}


  def insert(self, word):
    # reduce(dict.__getitem__, word, self.root)["$"] # Alternative for Trie()
    # reduce(lambda x,y: x.setdefault(y,{}), word, self.root).setdefault("$",{}) # Alternative for {}
    d = self.root
    for c in word:
      if c not in d: d[c] = {}
      d = d[c]
    d["#"] = {}
    
  def get(self, word):
    d = self.root
    for c in word:
      if c not in d: return None
      d = d[c]
    return d

  def search(self, word):
    d = self.get(word) 
    return d is not None and "#" in d

  def startsWith(self, prefix):
    return self.get(prefix) is not None
  
  def searchRe(self, word):
    def helper(w, d):
      if len(w) == 0: return "#" in d # base case
      s = set(d) - set("#") if w[0] == '.' else set(w[0])
      return any (helper(w[1:], d[c]) for c in s if c in d)
    return helper(word, self.root)

# Your Trie object will be instantiated and called as such:
obj = Trie()
word = "apple"
prefix = "app"
obj.insert(word)
print(obj.search(word))
print(obj.search(prefix))
print(obj.startsWith(prefix))
print(obj.searchRe("a.p.e"))
print(obj.searchRe("..p."))
print(obj.searchRe("....."))
