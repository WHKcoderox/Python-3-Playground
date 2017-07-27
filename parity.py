# generate parity
# 7 digits
# + + + + + + + +
# even, simple
def s_even_parity(bit):
    total = 0
    for digit in bit:
        if digit == '1':
            total += 1
    if total%2 == 0:
        return bit + '0'
    return bit + '1'

def d2b(n):
    NEWBASE = 2
    ans = []
    ans2 = ''
    while n >= 1:
        ans.append(n % NEWBASE)
        n //= NEWBASE
    for digit in ans[::-1]:
        ans2 += str(digit)
    return ans2

def parity_for_ascii(char, parityGen=s_even_parity):
    return parityGen(d2b(ord(char)))
