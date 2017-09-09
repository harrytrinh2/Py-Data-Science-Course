def absolutely_value(val):
    if val < 0:
        return 0 - val
    return val
print ("The absolutely is: ",absolutely_value(-6))


def my_abs(val):
    if val < 0:
        print (0-val) #cai nay chi ka print thoi ma, dau co luu vo bien hay tra ve (return) dau
    else:
        print (val)
    return val
print (my_abs(-5))

def swap(val1, val2):
	tmp = val1
	val1 = val2
	val2 = tmp
x=1
y=7
swap(x, y)
print(x,y)