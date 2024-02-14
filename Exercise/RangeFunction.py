# ^ range(start, stop, step) function have 3 argument
# 1. start --> from where we have to start iteration
# 2. stop --> from where we have to stop
# 3. step --> up to which value we have to move ahead

for i in range(1, 10, 2):
    print(i)
print("================================")
for i in range(10, 0, -1):
    print(i)
print("================================")
# cheking if no in range or not
x = 5
if x in range(1, 10):
    print(f"{x} is in the range")

y = 9
if y in range(0, 100, 2):
    print(f"{y} is even value")
else:
    print(f"{y} is not even value")
