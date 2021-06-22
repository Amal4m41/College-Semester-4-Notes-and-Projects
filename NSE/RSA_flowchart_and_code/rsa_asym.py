import random as rn
import pickle 

pickle_off = open ("prime_number_list", "rb")   #this file contains the list of prime numbers from 1 to 10000
prime_num_list = pickle.load(pickle_off)   #importing the list of prime numbers generated

def is_prime(num):  #checking if the number is a prime number
    for i in range(num-1,1,-1):
        if(num%i==0):
            return 0
    else:
        return 1

def generate_key():
    p=q=4
    while(p==q):        #choosing a large prime number in for p and q from the list of prime numbers
        p=rn.choice(prime_num_list[26:40])   
        q=rn.choice(prime_num_list[26:40])   #restricting the range of prime numbers for faster computation

    n=p*q
    phi_n=(p-1)*(q-1)

    e=phi_n
    while(phi_n%e==0 and e>=phi_n):      #finding a value for e such that gcf(e,phi_n) is 1
        e=rn.choice(prime_num_list)
    
    d= pow(e, -1, phi_n)         

    return (e,n,d)

def encrypt(e,n,message):
    cipher_text=message**e % n
    return cipher_text

def decrypt(d,n,cipher_text):
    plain_text=(cipher_text**d) % n
    return plain_text



e,n,d=generate_key()

message=int(input('Enter the number : '))
cipher_text=encrypt(e,n,message)
plain_text=decrypt(d,n,cipher_text)
print('Entered message : ',message)
print('Encrypted form : ',cipher_text)
print('Decrypted form : ',plain_text)



