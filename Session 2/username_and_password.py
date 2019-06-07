Username=input("Nhap Username:")

if Username == "c4e":
    Password=input("Nhap password:")
    print(Password)
    if Password == "codethechange":
        print("Welcome"+Username)
    else:
        print("Wrong Password")

else:
    print("Not found")
