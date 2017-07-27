def d2b(n):
    NEWBASE = 2
    ans = []
    while n >= 1:
        ans.append(n % NEWBASE)
        n //= NEWBASE
    for digit in ans[::-1]:
        print(digit,end='')

def b2d(n):
    OLDBASE = 2
    ans = 0
    n = [int(digit) for digit in str(n)]
    for digit in range(len(n)):
        ans += n[digit]*OLDBASE**(len(n)-digit-1)
    print(ans)

def d2o(n):
    NEWBASE = 8
    ans = []
    while n >= 1:
        ans.append(n % NEWBASE)
        n //= NEWBASE
    for digit in ans[::-1]:
        print(digit,end='')

def o2d(n):
    OLDBASE = 8
    ans = 0
    n = [int(digit) for digit in str(n)]
    for digit in range(len(n)):
        ans += n[digit]*OLDBASE**(len(n)-digit-1)
    print(ans)

def interpret(digit):
    maps = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return maps[int(digit)]

def d2h(n):
    NEWBASE = 16
    ans = []
    while n >= 1:
        ans.append(interpret(n % NEWBASE))
        n //= NEWBASE
    for digit in ans[::-1]:
        print(digit,end='')

def h2d(n):
    OLDBASE = 16
    ans = 0
    n = [digit.upper() for digit in str(n)]
    maps = { y:x for x,y in \
             enumerate("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")}
    for digit in range(len(n)):
        ans += maps[n[digit]]*OLDBASE**(len(n)-digit-1)
    print(ans)

# base-n number class
class Base_n:
    def __init__(self, base):
        self.base = base
        self.value = []

    def carryover(self):
        for pos in range(len(self.value)):
            curr = self.value[pos]
            temp = pos
            while curr >= self.base:
                carryover = curr//self.base
                self.value[temp] -= carryover*self.base
                curr -= carryover*self.base
                temp += 1
                if len(self.value) > temp:
                    self.value[temp] += carryover
                else:
                    self.value.append(carryover)
                curr = self.value[temp]

    def add(self, value):
        digit = 0
        while value >= 1:
            if len(self.value) <= digit:
                self.value.append(value % self.base)
            else:
                self.value[digit] += value % self.base
            digit += 1
            value //= self.base
        self.carryover()

    def multiply(self, value):
        for i in range(len(self.value)):
            self.value[i] *= value
            print(self.value[i])
        self.carryover()

    def getValueString(self):
        val = ''
        for digit in self.value[::-1]:
            val += interpret(digit)
        return val

# binary can be mapped to octal
def b2o(n):
    OLDBASE = 2
    NEWBASE = 8
    ans = Base_n(NEWBASE)
    n = [digit for digit in str(n)]
    for digit in range(len(n)):
        ans.add(n[digit]*OLDBASE**(len(n)-digit-1))
    print(ans.getValueString())

def o2b(n):
    OLDBASE = 8
    NEWBASE = 2
    ans = Base_n(NEWBASE)
    n = [int(digit) for digit in str(n)]
    for digit in range(len(n)):
        ans.add(n[digit]*OLDBASE**(len(n)-digit-1))
    print(ans.getValueString())

def b2h(n):
    OLDBASE = 2
    NEWBASE = 16
    ans = Base_n(NEWBASE)
    n = [int(digit) for digit in str(n)]
    for digit in range(len(n)):
        ans.add(n[digit]*OLDBASE**(len(n)-digit-1))
    print(ans.getValueString())

def h2b(n):
    OLDBASE = 16
    NEWBASE = 2
    ans = Base_n(NEWBASE)
    n = [digit.upper() for digit in str(n)]
    maps = { y:x for x,y in \
             enumerate("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")}
    for digit in range(len(n)):
        ans.add(maps[n[digit]]*OLDBASE**(len(n)-digit-1))
    print(ans.getValueString())

def o2h(n):
    OLDBASE = 8
    NEWBASE = 16
    ans = Base_n(NEWBASE)
    n = [digit.upper() for digit in str(n)]
    maps = { y:x for x,y in \
         enumerate("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")}
    for digit in range(len(n)):
        ans.add(maps[n[digit]]*OLDBASE**(len(n)-digit-1))
    print(ans.getValueString())

def h2o(n):
    OLDBASE = 16
    NEWBASE = 8
    ans = Base_n(NEWBASE)
    n = [digit.upper() for digit in str(n)]
    maps = { y:x for x,y in \
             enumerate("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")}
    for digit in range(len(n)):
        ans.add(maps[n[digit]]*OLDBASE**(len(n)-digit-1))
    print(ans.getValueString())

def n2m(n, m, num):
    OLDBASE = n
    NEWBASE = m
    ans = Base_n(NEWBASE)
    num = [digit.upper() for digit in str(num)]
    maps = { y:x for x,y in \
             enumerate("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")}
    for digit in range(len(num)):
        ans.add(maps[num[digit]]*OLDBASE**(len(num)-digit-1))
        print(ans.getValueString())
    print(ans.getValueString())

# binary mapping method
def b2omap(n):
    maps = [ '0'*(3-len(d2b(x))) + d2b(x) for x in range(8) ]
    digit = 0
    length = len(n)
    ans = []
    while digit < length:
        if digit + 2 >= length:
            # 3-length-digit-1


