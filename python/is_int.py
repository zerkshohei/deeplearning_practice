def is_int(x):
    if x - round(x,0) > 0:
        return False
    else:
        return True



print is_int(7.0)
print is_int(3)
