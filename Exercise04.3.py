def area(x0, y0, x1, y1, x2, y2):
    return abs(x0*(y1 - y2) + x1*(y2 - y0) + x2*(y0 - y1)) / 2

print(area(0,0, 4,0, 0,3))  
print(area(1,2, 4,6, 5,2))  

