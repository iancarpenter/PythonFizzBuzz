# first attempt
# for x in range(100):
#     if x % 3 == 0 and x % 5 == 0:
#         print("fizzbuzz")
#         continue
#     elif x % 3 == 0:
#         print("fizz")
#         continue
#     elif x % 5 == 0:
#         print("buzz")
#         continue
#     print(x)

# refactored
for x in range(100):
    
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
