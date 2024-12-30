#range (1,n) --> chạy từ 1 tới n-1
#range (1,n+1) --> chạy từ 1 tới n+1-1=n
#5!=1*2*3*4*5
def factorial_non_recursive(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact

def factorial_recursive(n)
    if n==0:
        return 1
    else:
        return n*factorial_non_recursive(n-1)

