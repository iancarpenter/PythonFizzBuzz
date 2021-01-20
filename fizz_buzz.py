'''
Program which highlights different ways to solve the FizzBuzz coding challenge. 

Each function will 
Write a program that prints the numbers from 1 to 100
For numbers divisible by 3, print “Fizz”
For numbers divisible by 5, print “Buzz”
For numbers divisible by both 3 and 5, print “FizzBuzz”

'''
def fizz_buzz_if_calc():
    
    fizz_buzz_list = []

    for x in range(1, 101):
        
        if x % 3 == 0 and x % 5 == 0:            
            fizz_buzz_list.append("fizzbuzz")
            continue
        elif x % 3 == 0:            
            fizz_buzz_list.append("fizz")
            continue
        elif x % 5 == 0:            
            fizz_buzz_list.append("buzz")
            continue        
        else:
            fizz_buzz_list.append(x)
    
    return fizz_buzz_list


def fizz_buzz_using_boolean():
    ''' '''
    fizz_buzz_list = []

    for x in range(1, 101):            

        fizz = x % 3 == 0 
        buzz = x % 5 == 0
        
        if fizz and buzz:            
            fizz_buzz_list.append('fizzbuzz')
            continue
        elif fizz:            
            fizz_buzz_list.append('fizz')
            continue
        elif buzz:            
            fizz_buzz_list.append('buzz')
            continue
        else:            
            fizz_buzz_list.append(x)            

    return fizz_buzz_list


if __name__ == "__main__":
    fb_list_1 = fizz_buzz_if_calc()    
    
    fb_list_2 = fizz_buzz_using_boolean()
    
    
