'''
Program which highlights different ways to solve the FizzBuzz coding challenge. 

Each function will 
Write a program that prints the numbers from 1 to 100
For numbers divisible by 3, print “Fizz”
For numbers divisible by 5, print “Buzz”
For numbers divisible by both 3 and 5, print “FizzBuzz”

'''
def fizz_buzz_if_calc():
    for x in range(1, 101):
        if x % 3 == 0 and x % 5 == 0:
            print("fizzbuzz")
            continue
        elif x % 3 == 0:
            print("fizz")
            continue
        elif x % 5 == 0:
            print("buzz")
            continue
        print(x)

def fizz_buzz_using_boolean():
    '''
    '''
    for x in range(1, 101):    
        fizz = x % 3 == 0 
        buzz = x % 5 == 0
        
        if fizz and buzz:
            print('FizzBuzz')
            continue
        elif fizz:
            print('Fizz')
            continue
        elif buzz:
            print('Buzz')
            continue
        else:
            print(x)
            continue

if __name__ == "__main__":
    fizz_buzz_if_calc()
    fizz_buzz_using_boolean()
