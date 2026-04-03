def char_counts(s: str):
    """ s is a string of lowercase chars.
    Return a tuple where the first element is the number of vowels in s,
    and the second element is the number of consonants in s."""
    
    (vowels,consonants) = (0, 0)
    
    for i in s:
        if i in "aeiou":
            vowels += 1
        else:
            consonants += 1
    a = (vowels, consonants)
    return a
    

#print(char_counts("dgsdjaaaagkshdfglkj"))

def mean(*args):
    total = 0
    for i in args:
        total += i
    return total/len(args)
#print(mean(1, 2, 3, 4,))


def sum_and_prod(L: list)-> tuple:
    """L is a list of numbers 
    Return a tuple where the first value is the sum of all elements in L
    and the second value is the product of all the elements in L."""
    sum = 0
    product = 1
    for i in L:
        sum += i
        product *= i
    return sum, product

print(sum_and_prod([2,3,4, 5,6,7,4,44]))