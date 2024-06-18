def factorial(num):
    result = 1
    
    for i in range(1,num+1):
        result*= i

    return result
    
def info(a = 30 ,b=10,c = 20):
    '''This is an info func
    ex : info()
    ans : 40'''
    return a - b + c 