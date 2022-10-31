import random
import string
l=int(input("enter the length of password"))
a=string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation
b=random.sample(a,l)
p="".join(b)
print("password is:",p)