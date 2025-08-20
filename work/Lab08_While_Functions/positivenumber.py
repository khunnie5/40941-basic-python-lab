def positive(inp):
    return inp>0

while True:
    i=int(input())
    if positive(i):
        break
print(f"accepted value: {i}")