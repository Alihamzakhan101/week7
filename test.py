def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    name = input("Enter your name: ")
    print(greet(name))


def say_goodbye(name):
    return f"Goodbye, {name}!"

if __name__ == "__main__":
    name = input("Enter your name: ")
    print(greet(name))
    print(say_goodbye(name))

