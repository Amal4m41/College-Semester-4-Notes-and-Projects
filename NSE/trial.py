p=47 
q=71

n=p*q
phi_n=(p-1)*(q-1)
e=79

# d=(1/e) % phi_n
d=y = pow(e, -1, phi_n)
m=123

c=m**e % n
print('c: ',c)

mes=c**d % n
print('mes: ',mes)
