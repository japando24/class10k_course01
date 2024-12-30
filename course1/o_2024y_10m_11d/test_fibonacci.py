from class10k.course1.o_2024y_10m_11d.FuncUnit import fibonacci, print_list_fibonacci

n=int(input("Enter position:"))
fib=fibonacci(n)
print("fib ({0})={1}".format(n,fib))
print("List of fibonacci from 1 to",n,":")
print_list_fibonacci(n)