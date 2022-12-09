with open("2022/Day2/input.txt") as f:
    s = f.read();

# A X = Rock = 1
# B Y = Paper = 2
# C Z = Sissors = 3

# loss = 0
# draw = 3
# win = 6

s = s.strip().split("\n")
for x in range(len(s)):
    s[x] = s[x].split(" ")

# print(s)

def partone(s):
    p = 0
    for a,b in s:
        if b == "X":
            p += 1
            if a == "A":
                p += 3
            elif a == "C":
                p += 6
        elif b == "Y":
            p += 2
            if a == "A":
                p += 6
            elif a == "B":
                p += 3
        elif b == "Z":
            p += 3
            if a == "B":
                p += 6
            elif a == "C":
                p += 3
    return p

print(partone(s))

# Part Two

# X = Lose = 0
# Y = Draw = 3
# Z = Win  = 6
# A Rock = 1
# B Paper = 2
# C Sissor = 3

z = 6
y = 3
x = 0

def parttwo(s):
    p = 0
    for a,b in s:
        if a == "A":
            if b == "X":
                p += 3 + x
            elif b == "Y":
                p += 1 + y
            elif b == "Z":
                p += 6 + 2
        elif a == "B":
            if b == "X":
                p += 1 + x
            elif b == "Y":
                p += 2 + y
            elif b == "Z":
                p += 3 + z
        elif a == "C":
            if b == "X":
                p += 2 + x
            elif b == "Y":
                p += 3 + y
            elif b == "Z":
                p += 1 + z
    return p

print(parttwo(s))