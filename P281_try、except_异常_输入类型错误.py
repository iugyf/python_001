while True:
    try:
        x = int(input("please enter an integer: "))
        break
    except ValueError:
        print("Error: I need an integer. Try again:")