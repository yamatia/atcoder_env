def Base10toN(x,n):
    s = ''
    while x:
        s = str(x%n) + s
        x//=n
        print(s)
    return s

print(Base10toN(10,8))
print(oct(10))