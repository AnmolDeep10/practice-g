print("hello world")

def main():
    print("This is the main function.")
    hlo = "Hello, World!"
    print(hlo)

def add(a, b):
    result = []
    for i in range(len(a)):
        result.append(a[i] + b[i])
    return result

add([1, 2, 3], [4, 5, 6])
