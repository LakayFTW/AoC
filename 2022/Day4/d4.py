with open("2022/Day4/input.txt") as f:
    s = f.read();

s = s.strip().split("\n")

for x in range(len(s)):
    s[x] = s[x].split(",")

# print(s[0][1])

print(s)