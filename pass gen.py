#code with idk

# import necessary modules
import random

#fastest password generator

def pas1(len):
    #it will ramdolly choose words , characters
    a = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()"  
    pas2 = "" #pass a empty string

    for i in range(len):
        pas2 = pas2 + random.choice(a)
    return pas2
    #it will return pas2

if __name__ == '__main__':
    len = int(input("Enter Your Lenght :"))
    pas2 = pas1(len)  

    print ('Your Generated Passwrod Is :' , pas2)
    #generated your password
    


