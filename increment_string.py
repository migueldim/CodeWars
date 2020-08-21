#Your job is to write a function which increments a string, to create a new string.

#If the string already ends with a number, the number should be incremented by 1.
#If the string does not end with a number. the number 1 should be appended to the new string.
#Examples:

#foo -> foo1
#foobar23 -> foobar24
#foo0042 -> foo0043
#foo9 -> foo10
#foo099 -> foo100

#Attention: If the number has leading zeros the amount of digits should be considered.

def increment_string(strng): 
    for i in range(len(strng)):
        digit = str(strng[i:])
        if digit.isdigit(): 
            digit = str(int(digit)+1).zfill(len(strng[i:]))
            return strng[0:i]+ digit
    return strng+"1"

# I could have used the rstrip function instead of the doing a loop

print(increment_string("foo"))
print(increment_string("foobar001"))
print(increment_string("foobar1"))
print(increment_string("foobar00"))
print(increment_string("foobar99"))
print(increment_string("foobar099"))
print(increment_string(""))

    
    




        
       
            
