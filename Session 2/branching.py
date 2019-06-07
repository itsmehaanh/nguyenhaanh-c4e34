# yob=int(input("Year of birth?"))
# age=2019-yob
# print(age)

# if age<10:
#     print("Baby")
# elif age<18:
#     print("Teenager")
# elif age<25:
#     print("Khong biet")
# else: 
#     print("Adult")

# from random import randint
# n = randint(1, 101)
# print(n)
# if n<=30:
#     print("Sunny")
# elif n<=70:
#     print("Rainy")
# elif n<=100:
#     print ("Cloudy")

a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
print(a,b,c)
delta = b*b-4*a*c
print(delta)
if delta<0:
    print("Vo nghiem")
elif delta==0:
    x=-b/(2*a)
    print("Nghiem kep: {0}".format(x))
elif delta>0:
    import math
    x1=-b-(math.sqrt(b*b-4*a*c))
    x2=-b+(math.sqrt(b*b-4*a*c))
    print("2 nghiem phan biet: {0} va {1}".format(x1,x2))