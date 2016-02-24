sum1=0
for i in range(1000):
    if (i%3==0)|(i%5==0):
        sum1=sum1+i
print(sum1)

x,y = [x for x in range(0, 1000, 3)], [y for y in range(0, 1000, 5)]
xy = list(set(x + y))
print(sum(xy))