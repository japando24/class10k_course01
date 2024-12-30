def H10toH2(n):
    if n>0:
        sd=n%2
        n=n//2
        H10toH2(n)
        print(sd,end=" ")

#test_case:
H10toH2(13)
print("")
H10toH2(11)
print("")
H10toH2(325)