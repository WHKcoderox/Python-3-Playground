# magic table number trick
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

def b2d(n):
    OLDBASE = 2
    ans = 0
    n = [int(digit) for digit in str(n)]
    for digit in range(len(n)):
        ans += n[digit]*OLDBASE**(len(n)-digit-1)
    return ans

import math

def magic():
    LOW, HIGH = int(input("State the lower number\n")),\
                int(input("Now state the higher number\n"))
    
    # make the tables
    tables = [ [] for i in range(math.ceil(math.log(HIGH,2))) ]
    for decimal in range(LOW, HIGH+1):
        # convert to binary
        binary = d2b(decimal)
        for i in range(len(binary)):
            if binary[0-(i+1)] == '1':
                tables[i].append(decimal)

    # setup done, now make queries
    CELLMAX = len(str(HIGH)) + 2
    CHARMAX = 25
    ROWMAX = 25//CELLMAX
    NEWLINE = "\n" + ("-"*CELLMAX)*ROWMAX + "\n"
    answer = ["0" for i in range(math.ceil(math.log(HIGH,2)))]
    for i in range(len(tables)):
        table = tables[i] # no need to manipulate table data
        # request user input
        req_string = "Do you see your number in this table? (Y/N)\n"
        counter = 0 # formats the table
        for elem in table:
            if counter > 0 and counter%ROWMAX == 0:
                req_string += NEWLINE
            elem = str(elem)
            length = len(elem)
            # standard sized table cell
            req_string += "|" + " "*((CELLMAX-2-length)//2) + str(elem) + " "*(math.ceil((CELLMAX-2-length)/2)) + "|"
            counter += 1
        user = input(req_string + "\n").upper()
        if user == "Y":
            answer[i] = "1"
    result = ""
    for bit in answer[::-1]:
        result += bit
    result = b2d(result)
    print("Your number was " + str(result))


