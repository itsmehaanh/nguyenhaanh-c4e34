n=int(input("Nhap n"))
is_prime=True
if n< 2:
    print(" ko phai so nguyen to")
for x in range (2,n):
    if n % x == 0:
        is_prime=False
        break
if is_prime==True :
    print("so nguyen to ")
else: 
    print("Khong phai so nguyen to")      