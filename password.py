import random
import string
def password():
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    all = lower + upper + num 
    temp = random.sample(all,10)
    password = "".join(temp)
    return password