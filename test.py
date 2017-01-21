from pypassgen import generate_password


for i in range(10, 30, 3):
    print(generate_password(i))

for i in range(10, 30, 3):
    print(generate_password(i, True, numbers=False, symbols=False))

for i in range(10, 30, 3):
    print(generate_password(i, True, numbers=True, symbols=False))
