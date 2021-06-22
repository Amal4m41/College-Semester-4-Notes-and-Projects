import re,string

def encrypt(text,n):
    cipher_text=''
    for i in text:
        if(i==' '):
            cipher_text+=i
        else:    
            cipher_text+=chr(((ord(i)-65)+n)%26+65)            # (alphabet_value+n)%26

    return cipher_text    

def decrypt(text,n):
    plain_text=''
    for i in text:        
        if(i==' '):
            plain_text+=i
        else:
            plain_text+=chr(((ord(i)-65)-n)%26+65)

    return plain_text    

def clean_text(text):
    text = re.sub(r'\d+', '', text)     #removing digits from text
    text = text.translate(str.maketrans('', '', string.punctuation))     #removing all punctuations
    return text

while(1):
    choice=int(input('1-Encrypt\n2-Decrypt\nEnter your choice: '))
    if(choice==1):
        input_text=input("Enter the plain text(only alphabets) : ").upper()
        n=int(input('Enter the key/number of places to be shifted(eg 3 or shifting 3 forwards) : '))  
        c=encrypt(clean_text(input_text),n)
        print('Cipher text: ',c)

    elif(choice==2):
        input_text=input("Enter the cipher text(only alphabets) : ").upper()
        n=int(input('Enter the key/number of places to be shifted(eg 3 or shifting 3 backwards) : '))
        c=decrypt(clean_text(input_text),n)
        print('Plain text: ',c)

    else:
        print("Entered wrong choice")

    ch=input("Do you want to continue? [Y/N] : ").lower()
    if(ch=='n'):
        print("Thank you!")
        break

