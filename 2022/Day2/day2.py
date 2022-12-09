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

