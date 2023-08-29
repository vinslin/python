x=5
def globalscope():
    global x
    x=x+1000000000000
    print(x)
globalscope()

def glo():
    print(x)

glo()
