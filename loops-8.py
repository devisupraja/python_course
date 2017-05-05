def is_even(x):
    if x%2==0:
        print "it's even"
        return True
    else:
        print "it's not even"
        return False

def is_int(x):
    if (x%1==0):
        print "it's integer"
        return True
    else:
        print "it's not integer"
        return False

def digit_sum(n):
    q=0
    while(n>0):
        p=n%10
        q = q+p
        n /=10
    print q
    return q
digit_sum(696)

def factorial(x):
    n=1
    while(x>0):
        n *=x
        x -=1
    return n

def is_prime(x):
    if x <= 1:
        return False
    elif x <= 3:
        return True    
    else:
        for n in range(2,x):
            if x % n == 0:
                return False
        else:
            return True

def  reverse(text):
    backwards = []
    for letter in text:
        backwards.insert(0,letter)
    end = ""
    for item in backwards:
        end += item
    print end
    return end

def anti_vowel(text):
    new = list(text)
    new_list = new[:]
    for c in new_list:
        if c in "aeiouAEIOU":
            new.remove(c)
    return ''.join(new)

score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
def scrabble_score(word):
    points = 0
    word = word.lower()
    for key in score:
        for i in range(0, len(word)):
            if word[i] == key:
                points += score[key]
            else:
                points += 0
    return points

def censor(text, word):
    x = text.split()
    for i in range(len(x)):
        if x[i] == word:
            x[i] = len(x[i]) * "*"
    return " ".join(x)

def count(sequence,item):
    
    co = 0
    for i in sequence:
        if i == item:
            co = co + 1
        print co
    return co

def purify (list_odd):
    list_even = []
    for even in list_odd :
        if even % 2 == 0 :
            list_even.append(even)
        else:
            list_even = list_even
    return list_even
print purify([2 , 5 , 8, 9 ,26 , 17 , 13 , 23])

def product(lst):
    total = 1
    for num in lst:
        total *= num
    return total

def remove_duplicates(lst):
    copy = list(lst)
    count_a = len(copy) - 1
    while count_a >= 0:
        count_b = count_a - 1
        while count_b >= 0:
            if copy[count_b] == copy[count_a]:
                copy.remove(copy[count_b])
                count_a -= 1
                count_b -= 1
            else:
                count_b -= 1
        count_a -= 1
    return copy

def median(num_list):
    num_list = sorted(num_list)
    pos1 = len(num_list) / 2
    pos2 = pos1 - 1
    if len(num_list) % 2 == 0:
        return float(num_list[pos1]+num_list[pos2])/2
        
    else:
        return float(num_list[pos1])
print median([4,5,5,4])
