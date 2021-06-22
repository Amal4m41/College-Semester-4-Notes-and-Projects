from rsa_asym import is_prime
import pickle

# prime_numbers=[]
# for i in range(2,10000):
#     if(is_prime(i)):
#         prime_numbers.append(i)


# with open('prime_number_list','wb') as fw:
#     pickle.dump(prime_numbers,fw)

pickle_off = open ("prime_number_list", "rb")
emp = pickle.load(pickle_off)

print(emp[0])

# print(array)