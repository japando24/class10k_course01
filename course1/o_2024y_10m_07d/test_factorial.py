from class10k.course1.o_2024y_10m_07d.factorial import factorial_non_recursive

f5=factorial_non_recursive(5)
print(f"{5}!={f5}")

for i in range (0,11):
    fi=factorial_non_recursive(i)
    print(f"{i}!={fi}")

print("------------------Recursive---------------------")
f5r=factorial_non_recursive(5)
print(f"{5}!={f5r}")