""""
The rgb() method is incomplete. Complete the method so that passing in RGB decimal values will result in a hexadecimal
representation being returned. The valid decimal values for RGB are 0 - 255.
Any (r,g,b) argument values that fall out of that range should be rounded to the closest valid value.

The following are examples of expected output values:
"""

def rgb(r,g,b):

    r = max(min(255, r),0)
    g = max(min(255, g), 0)
    b = max(min(255, b), 0)

    result = str(hex(r))[-2:]+str(hex(g))[-2:]+str(hex(b))[-2:]
    result = result.replace("x","0")
    result = result.upper()

    return result


print(rgb(255,255,255))
print(rgb(255,255,300))
print(rgb(0,0,0))
print(rgb(148,0,211))

