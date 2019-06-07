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
print('''Estimate this answer (exact calculation not needed):
Jack scored these marks in 5 math tests: 49, 81, 72, 66 and 52. What is the mean?
1. About 55
2. About 65
3. About 75
4. About 85''' )
question2 = {
    "Estimate this answer (exact calculation not needed)": {
        "1":"About 55",
        "2": "About 65",
        "3": "About 75",
        "4": "About 85",}
}

answer_2 = input("Your code:")
if answer_2 == "2":
    print("Bingo!")
else:
    print(":(")

if answer == "3" and answer_2 == "2":
    print("You correctly answer both questions")
elif answer != "3" and answer_2 != "2":
    print("You got both answers incorrect")
else:
    print("You correctly answer 1 out of 2 questions")