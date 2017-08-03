# magic table number trick
def d2b(n):
    NEWBASE = 2
    ans = []
    i = 0 # return all digit positions
    while n >= 1:
        next_digit = n % NEWBASE
        if next_digit == 1:
            ans.append(i)
        n //= NEWBASE
        i += 1
    return ans

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
        # get binary digit positions
        binary = d2b(decimal)
        for i in binary:
            tables[i].append(decimal)

    # setup done, now make queries
    CELLMAX = len(str(HIGH)) + 2
    CHARMAX = 25 # maximum characters in one row
    ROWMAX = CHARMAX//CELLMAX
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
        valid = False
        while not valid:
            user = input(req_string + "\n").upper()
            if user == "Y":
                answer[i] = "1"
                break
            if user == "N":
                break
            print("Take it seriously. Y/N only.")
    result = ""
    for bit in answer[::-1]:
        result += bit
    result = b2d(result)
    print("Your number was " + str(result))


