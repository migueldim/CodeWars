
def anagrams(word, words):

 anag = []
 for w in words:
  ana = True
  for c in word:
    ana &= str(word).count(c) == str(w).count(c) and len(w) == len(word)
  if ana:
    anag.append(w)

 return anag


print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))
print(anagrams('laser', ['lazing', 'lazy',  'lacer']))