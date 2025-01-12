def input_value(val_type, request_msg):
    """generic function for input a value of a given type."""
    while True:
        val = input(request_msg + ": ")
        try:
            val = val_type(val)
            return val
        except ValueError:
            print(val + " can't convert to " + str(val_type) + 
                  ". please try again:")
            
x = input_value(int, "please input an integer")