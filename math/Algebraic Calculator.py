def quadratic_formula(a,b,c):
    list = []
    list.append((-b + √(b^2 - 4ac))/2a)
    list.append((-b - √(b^2 - 4ac))/2a)
    return list
print(quadratic_formula(1,6,9))