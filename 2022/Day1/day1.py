with open("2022/Day1/input.txt") as f:
    s = f.read();

s = s.strip().split("\n\n")

# print(s[0])

for y in range(len(s)):
    s[y] = s[y].split("\n")

for y in s:
    for x in range(len(y)):
        y[x] = int(y[x])

# print(s)

print(s)
# print(max(sum(z) for z in s))
