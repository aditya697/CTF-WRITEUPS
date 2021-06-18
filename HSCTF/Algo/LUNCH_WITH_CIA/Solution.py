def get_waste(l, w, a):
    if (l, w) in result:
        return result[(l,w)]
    minimum = l*w
    for cake in a:
        x = cake[0]
        y = cake[1]
        if (x <= l and y <= w):
            minimum = min(minimum, (get_waste(l-x, w, a) + get_waste(x, w-y, a)))
            minimum = min(minimum, (get_waste(l, w-y, a) + get_waste(l-x, y, a)))
    result[(l,w)] = minimum
    return minimum

    
l, w, n = map(int, input().split())

lst = []

for i in range(n):
    dim = []
    x, y = map(int, input().split())
    dim.append(x)
    dim.append(y)
    lst.append(dim)

result = {}
print(get_waste(l,w,lst))
