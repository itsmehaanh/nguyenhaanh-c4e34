code = {
    "thik" : "thích",
    "iu" : "yêu",
    "j" : "gì",
    "hok" : "không",
}
while True:
    for key in code: 
        print (key, end = "  ")


    Teencode = input("Nhập từ khoá:")
    if Teencode in code:
        fancy = code[Teencode]
        print(fancy)
    else:
        answer = input("Do you want to add meanings? (Y/N)").upper()
        if answer == "Y":
            meaning = input("Meaning:")
            code[Teencode] = meaning
            for key in code: 
                print (key, end = "  ")
            print()
        else:
            print("Good bye!")
            break



