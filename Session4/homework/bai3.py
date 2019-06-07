print ('''If x = 8, then what is 4(x+3)? 
1. 35
2.36
3.40
4.44''')
question = { 
    "If x = 8, then what is 4(x+3)?" : {
        "1" : 35,
        "2" : 36,
        "3" : 40,
        "4" : 44,}

}
answer = input("Your code:")
if answer == "3":
    print("Bingo!")
else:
    print(":(")



