from itertools import permutations

a1 = 'ytbbedmkd'
a2 = 'yhdbtyydd'
s = 'edytertpty'

letters = 'ytbedmkhrp'

def trans(word, digits, wrong=None):
    r = word.translate(str.maketrans('ytbedmkhrp', digits))
    if wrong is not None:
        # 01234567 = word indices
        # 76543210 = exponents
        #        8 = len(word)
        
        i = len(word) - 1 - wrong
        r = r[:i] + '0' + r[i+1:]
    return int(r)

def check(issum=False):
    """Uses global variables because I didn't want to pass 5 parameters."""
    rem = total - add1 - add2
    if issum: rem = -rem
    if rem % 10**w == 0 and 0 < rem // 10**w < 10:
        print("...Found one! Place 10**" + str(w) + " should be", rem)
        print(letters)
        print(p, '->', add1, '+', add2, '=', total)

for w in range(len(a1)):
    # The wrong letter is in the 10**w's place.
    print(f"Assuming the 10**{w}'s place in a1 is wrong.")
    for perm in permutations('0123456789'):
        p = ''.join(perm) # Permutations of strings are character tuples.
        add1 = trans(a1, p, w)
        add2 = trans(a2, p)
        total = trans(s, p)
        check()
            
for w in range(len(a2)):
    print(f"Assuming the 10**{w}'s place in a2 is wrong.")
    for perm in permutations('0123456789'):
        p = ''.join(perm)
        add1 = trans(a1, p)
        add2 = trans(a2, p, w)
        total = trans(s, p)
        check()

for w in range(len(s)):
    print(f"Assuming the 10**{w}'s place in s is wrong.")
    for perm in permutations('0123456789'):
        p = ''.join(perm)
        add1 = trans(a1, p)
        add2 = trans(a2, p)
        total = trans(s, p, w)
        check(issum=True)

##  Output:
##
##  <snip>
##  Assuming the 10**1's place in a1 is wrong.
##  ...Found one! Place 10**1 should be 60
##  ytbedmkhrp
##  6951324708 -> 695513203 + 673596633 = 1369109896
##  <snip>
##  Assuming the 10**1's place in a2 is wrong.
##  ...Found one! Place 10**1 should be 50
##  ytbedmkhrp
##  6951324708 -> 695513243 + 673596603 = 1369109896
##  <snip>
##  Assuming the 10**1's place in s is wrong.
##  ...Found one! Place 10**1 should be 70
##  ytbedmkhrp
##  6951324708 -> 695513243 + 673596633 = 1369109806
##  <snip>

