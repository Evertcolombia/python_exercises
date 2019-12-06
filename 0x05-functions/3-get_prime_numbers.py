#!/usr/bin/python

# input max prime

# Function to know if a number is prime
def is_prime(num):
    state = true

    # for from 2 till the num conrresponds to the iteration
    for i in range(2, num):

        # If num % i reminder is = to 0 return false
        if (num % i) == 0:
                state = false
                return state
    # else return true
    return state


# function to  get the primes number in introduce it in a list
def get_primes(max_number):
    
    #list for prime numbers empty
    list_of_primes = []

    # for loop in a range  from 2 to the max_number passing by the user
    for num1 in range(2, max_number):
            
        # call function to know if the number is prime passing num in the index iteration
        if is_prime(num1):

            # if the return answer is true so append the number n the empty list
            list_of_primes.append(num1)
    
    # Return the prime numbers list
    return list_of_primes


#get the user num to check
max_num_to_check = int(input("Search for primes up to: "))

# call the function and get the primes number list
list_of_primes = get_primes(max_num_to_check)

# For loop to go through the list and print each number into this
for prime in list_of_primes:
        print(prime)
