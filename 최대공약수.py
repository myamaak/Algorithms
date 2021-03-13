def GCD(x, y) :
    # print("x",x,"y",y)
    if y == 0:
        return x
    else:
        return GCD(y, x%y)
