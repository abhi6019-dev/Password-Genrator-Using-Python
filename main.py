import string
import random
import time 

print("Password Genrator By Abhi6019-dev")
time.sleep(2)
 
if __name__ == "__main__":
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation

    plen = int(input("Enter Your Password's Length : "))
    time.sleep(2)

    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    print("Genrating Your Password ...")
    time.sleep(2)
    
    print("Your Password Is : " + "".join(random.sample(s,plen)))
