def my_function(arg1, *argv):
    print("First argument:", arg1)
    for arg in argv:
        print("Next argument:", arg)


my_function('Welcome', 'to', 'Python!')

def my_function1(*argv):
  print(argv)

my_function1('Hello', 'World!')

