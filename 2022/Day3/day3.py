with open("2022/Day3/input.txt") as f:
    s = f.read();

s = s.strip().split("\n")

# split string in the middle
for y in range(len(s)):
    x = s[y]
    str1 = slice(0, len(x)//2)
    str2 = slice(len(x)//2, len(x))
    print(x[str1], x[str2])

# print(s)