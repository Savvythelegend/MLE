n = int(input())
table = [n*i for i in range(1,11)]
print(table)
for i,j in enumerate(table):
    print(f"{n} * {i+1} = {j}") 