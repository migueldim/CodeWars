"""
In this kata you have to create all permutations of an input string and remove duplicates, if present. 
This means, you have to shuffle all letters from the input in all possible orders.
"""

def permutations(string):

    # Build combination 

    # Swap string 
    if(len(string)>1):
        result = {string}
       
        for i in range(len(string)):
            index = string[i]
            rest = string[:i]+string[i+1:]

            for perm in permutations(rest): 
                result.add(index+perm)
        return list(result)
    else:
        return [string]




#print(inserts("a", "abb"))
#print(inserts("aa", "bb"))
#print(inserts("aab", "b"))

# print(permutations("a"))
#print(permutations("ab"))
print(permutations("aabb"))
print(permutations("abc"))
