import random

cap_letter = ("A","B","C","D","E","F",'G','H','I','J','K','L','M','N','0','P','Q','R','S','T','V','W','X','Y','Z')
lowercase_letter = ('a','b','c','d','e','f','g','h','i','j','k','m','n','o','p','q','r','s','t','v','w','x','y','z')
num1_10 = ('21','51','95','87','00')
symbol = (".",',','!','&','$','*')

c = (cap_letter)
l = (lowercase_letter)
n = (num1_10)
s = (symbol)

password=random.choice(c) + random.choice(l) + random.choice(c) + random.choice(n)*2 + random.choice(l) + random.choice(l) + random.choice(c) + random.choice(c) +  random.choice(n) + random.choice(s)



print(password)
