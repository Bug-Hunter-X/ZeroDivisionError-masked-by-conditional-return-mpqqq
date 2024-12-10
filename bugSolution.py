def my_function(x):
    if x == 0:
        return 0  # Correct handling of the zero division case
    elif x < 0:
      raise ValueError("Input value must be non-negative")
    else:
        return 1 / x