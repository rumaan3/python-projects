# Write your code below this line 👇
def prime_checker(number):
    is_prime=True
    if number%number==0 and number%1==0:
        for i in range(2,number):
            if number%i==0:
                is_prime=False
                break
    if is_prime==True :
        print ("It's a prime number.")
    else:
        print ("not a prime")




# Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input()) # Check this number
prime_checker(number=n)