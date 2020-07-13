# --------------
#Code starts here
import sys

def palindrome(num):
    numstr =str(num)
    for i in range (num+1,sys.maxsize):
        if str(i) ==str(i)[: : -1]:
            return i

palindrome(8)


# --------------
#Code starts here
def a_scramble(str_1, str_2):
    str_1 = list(str_1.lower())
    str_2 = list(str_2.lower())
    for i in range(0,len(str_2)):
        if str_2[i] in str_1:
            str_1.remove(str_2[i])
            if i == len(str_2) -1:
                return True
        else:
            return False

    
a_scramble("Tom Marvolo Riddle", "Voldemort")


# --------------
#Code starts here
def check_fib(num):
    num1 = 0
    num2 = 1
    num3 = 0
    while num>num3:
        num3 = num1 + num2
        if num == num3:
            return True
        elif num<num3:
            return False
        num1 = num2
        num2 = num3

        
check_fib(145)
check_fib(234)


# --------------
#Code starts here
def compress(word):
    word = word.lower()
    result = ""
    count = 1
    result += word[0]
    for i in range(len(word)-1):
        if(word[i] == word[i+1]):
            count +=1
        else:
            result += str(count)
            result += word[i+1]
            count = 1
    result += str(count)
    return result

compress("xxcccdex")
compress('Ss')
compress('ssggtts')
compress('banana')


# --------------
#Code starts here
def k_distinct(string, k):
    string = string.lower()
    unique = []
    for char in string[: :]:
        if char not in unique:
            unique.append(char)
    count = len(unique)

    if count == k:
        return True
    else:
        return False


k_distinct('Messoptamia', 8)



