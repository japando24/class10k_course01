def move (n,A,B,C):
    """
    Di chuyển n đĩa từ tháp A qua tháp C, với tháp B là tháp trung gian
    :param n:
    :param A:
    :param B:
    :param C:
    :return:
    """
    if n==1: #điểm dừng vì chỉ có 1 đĩa, chuyển trực tiếp
        print(f"Move {A}=>{C}")
    else:#Thực hiện đệ quy
        move(n-1,A,C,B)
        print(f"Move {A}=>{C}")
        move(n-1,B,A,C)
    #thử nghiệm 1:
    #n-1 đĩa là đệ quy
    #ta tưởng tượng: n=2
    #n-1 <=>

#test_case_1
print("TEST CASE n=1")
n=1
move(n,"A","B","C")
# test_case_2
print("*"*25)
print("TEST CASE n=2")
n=2
move(n,"A","B","C")

print("*" * 25)
print("TEST CASE n=3")
n = 3
move(n, "A", "B", "C")

print("*" * 25)
print("TEST CASE n=3")
n = 64
move(n, "A", "B", "C")
