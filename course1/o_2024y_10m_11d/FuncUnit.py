#giai thừa
def factotial(n):
    if n==0:
        return 1
    else:
        return n*factotial(n-1)
#tổ hợp
def A(n,k):
    return factotial(n)/factotial(n-k)
#chỉnh hợp
def C(n,k):
    return  A(n,k)/factotial(k)

#fibonacci
def fibonacci(n):
    if n==1 or n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

def print_list_fibonacci(n):
    for i in range (1,n+1):
        fib=fibonacci(i)
        print(fib,"=>",end="")

def hanoi_tower (n,A,B,C):
    """
    Đây là giải thuật đệ quy cho bài toán tháp HN
    :param n: lag số đĩa cần di chuyển từ cột A qua cột C, với cột B làm trung gian
    :param A: là cột nguồn chứa n đĩa ban đâu cần chuyển qua C
    :param B: là cột trung gian để trung chuyển đĩa do: chỉ chuyển 1 đĩa 1 lần và đĩa nhỏ nằm trên
    :param C: là cột đích sẽ nhận đĩa từ cột A
    :return:
    """
    if n==1: #điểm dừng
        print(f"Move {A} ==> {C}")
    else:
        hanoi_tower(n-1,A,C,B)
        print(f"Move {A} ==> {C}")
        hanoi_tower(n-1,B,A,C)