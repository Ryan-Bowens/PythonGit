print("#1:")
for i in range(150):
    print(i)
print("---------")

print("#2:")
for i in range(5, 1005, 5):
        print (i)
print("---------")

print("#3:")
for i in range(1, 100):
    if i % 5 == 0:
        print(f"{i}: Coding")
    if i % 10 == 0:
        print(f"{i}: Coding Dojo")
print("---------")

print("#4:")

print("---------")

print("#5:")
for i in range(2018, 0, -4):
    print(i)
print("---------")

print("#6:")
def flexCounter(lowNum, highNum, mult):
    for i in range(lowNum, highNum + 1):
        if i % mult == 0:
            print(i)
print(flexCounter(2, 9, 3))