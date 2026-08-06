def add(a,b):
    return a+b
 
 
def subtract(a,b):
    return a-b

def multiply(a,b):
    return a *b
 
def division(a,b):
    if b==0:
        raise ValueError("cannot divide by 0")
    return a/b
 
if __name__=="__main__":
    print("add result",add(10,50))
    print("subtraction result", subtract(20,10))