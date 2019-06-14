def get_even_list(l):
    r = []
    for n in l :
        if n % 2 == 0:
            r.append(n)
    return r
print(get_even_list([1, 4, 5, -1, 10]))