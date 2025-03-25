def relative_err(actual=1, desire=1):
    actual = float(input("Please input actual value here as float: "))
    desire = float(input("Please input desire value here as float: "))
    print("Relative error is:", end=" ")
    print(f"{(abs(actual - desire) / desire) * 100}%")