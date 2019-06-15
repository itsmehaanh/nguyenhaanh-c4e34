def is_inside(point, rectangular):             
    if rectangular[0] <= point[0] <= rectangular[0] + rectangular[2] and rectangular[1] <= point[1] <= rectangular[1] + rectangular[3]:
        confirm = True
        print(confirm)
    else:
        confirm = False
        print(confirm)

    return confirm

test = is_inside([100, 120], [140, 60, 100, 200]) 

if test == True:
   print("Your function is correct")
else:
   print("Ooops, bugs detected")