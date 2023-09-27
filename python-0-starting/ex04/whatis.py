import sys


if len(sys.argv) < 2:
    sys.exit(1)
try:
    if len(sys.argv) > 2:
        raise AssertionError("can't have more than one argument")
except AssertionError as e:
    print(f"AssertionError: {e}")
    sys.exit(1)

try:
    number = int(sys.argv[1])
except ValueError:
    try:
        raise AssertionError("argument is not an integer")
    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(1)

if number % 2 == 0:
    print("I'm Even.")
elif number % 2 != 0:
    print("I'm Odd.")
