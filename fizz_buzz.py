"""
Program to showcase different ways to solve the FizzBuzz coding challenge. 

Each function will 
    Count from 1 - 100 inclusive     
    For numbers divisible by 3, Add to the list the string fizz
    For numbers divisible by 5, Add to the list the string buzz
    For numbers divisible by both 3 and 5, Add to a list the string fizzbuzz
    For all other numbers add the number to the list and return it to the caller    
"""


def fizz_buzz_using_boolean():
    """The results of the mod calculations are set to booleans
       which makes the if statements easier to understand"""
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


def fizz_buzz_if_calc():
    """Fizzbuzz solution with the mod operator used within the 
       if statements"""
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


if __name__ == "__main__":    

    fb_list_2 = fizz_buzz_using_boolean()
    print(fb_list_2)

    fb_list_1 = fizz_buzz_if_calc()
    print(fb_list_1)            
