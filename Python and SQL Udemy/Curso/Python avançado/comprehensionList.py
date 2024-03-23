x = [1, 2, 3, 4, 5]
y = []
z = []
for i in x:
    y.append(i ** 2)
    if i % 2 == 0:
        z.append(i)
print(x)
print(y)
print(z)
print("=" * 30)

# Com comprehension
x = [1, 2, 3, 4, 5]
y = [i ** 2 for i in x]
z = [i for i in x if i % 2 == 0]
print(x)
print(y)
print(z)