def counter(init=0):
    count = init

    def interface(command):
        nonlocal count
        if command == 'value':
            return count
        elif command == 'inc':
            count += 1
        elif command == 'dec':
            count -= 1
        else:
            return 'Not understood.'
    return interface

count1 = counter()
count2 = counter(10)

count1("inc")
for i in range(4):
    count1("inc")

count2("inc")
for i in range(3):
    count2("dec")

print(count1('value'),count2("value"))