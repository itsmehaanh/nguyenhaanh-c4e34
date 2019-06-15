from random import *

def generate_quiz():
    from random import randint

    x = randint(1,10)
    y = randint(1,10)
    list_op = ['+','-','*','/']
    oper = list_op[randint(0,3)]

    result= eval(x,y,op)
    random_result = randint(-1,1)
    final_result = random_result + result

    return [x, y, op, result]

def check_answer(x, y, op, result, user_choice):
   if eval(x,y,op) == result:
        if user_choice == True:
            return True
        else:
            return False
    elif eval(x,y,op) != result:
        if user_choice == True:
            return False
        else:
            return True

