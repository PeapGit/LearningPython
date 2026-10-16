import os, datetime

def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

def word_count(text):
    return len(text.split())

def list_dir(path="."):
    return os.listdir(path)

def timestamp():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def main():
    print(greet("world"))
    print("2 + 3 =", add(2, 3))
    print("Words:", word_count("the quick brown fox"))
    print("Current time:", timestamp())
    print("Files here:", list_dir())

if __name__ == "__main__":
    main()
