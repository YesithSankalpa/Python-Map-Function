li = []
Loop = True

while Loop == True:
    name = input("Enter Student's Name: ")
    age = int(input("Enter Student's Age: "))
    over = input("Is All The Students Entered (Y/N): ")

    if (over == "Y"):
        Loop = False

    li.append([name, age])

    print("\n\n", li, "\n\n\n")


def func(x):
    x.append("Ananda College")
    return x


print("\n\n")
print(list(map(func, li)))

input()
