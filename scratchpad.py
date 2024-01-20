# Prime number function
# This program checks if a given number is prime or not.
def is_prime(num):
    
    if (num % num == 0 and num % 1 == 0 ):
        print ("The number is ", num, "and it's a prime number.")
        if num < 2 :
            print ("Number is not prime")
    else:
        print ("invalid opertaion")
num=input("Enter number to test whether prime or not: ")
print ( is_prime(num))