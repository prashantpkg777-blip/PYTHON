a = 34

def func():
    global a
    print(a)
    a = 45
    print(a)

func()
print(a)