import string
with open("2022/Day3/input.txt") as f:
    s = f.read();

s = s.strip().split("\n")

sameletters = []
# split string in the middle
for y in range(len(s)):
    x = s[y]
    str1 = slice(0, len(x)//2)
    str2 = slice(len(x)//2, len(x))
    # print(x[str1], x[str2])
    #find the same same once existing letters in part one and two of the split string and add them to a list
    a=list(set(x[str1])&set(x[str2]))
    # print("The common letters are:")
    for i in a:
        sameletters.append(i)

# print(sameletters)

# iterate through upper and lower case letters and add them to a list together with their score
letterlist = []
score = 0
for i in string.ascii_lowercase:
    score += 1
    letterlist.append([i, score])

score = 26
for i in string.ascii_uppercase:
    score += 1
    letterlist.append([i, score])

# print(llist)

# calculate the sum of all same letters within the "sameletters" list according to their score from "letterlist"
def calcSum(sameletters, letterlist):
    sum = 0
    for i in range(len(sameletters)):
        for y in range(len(letterlist)):
            if sameletters[i] == letterlist[y][0]:
                # print(llist[y][1])
                sum += letterlist[y][1]
    print(sum)

calcSum(sameletters, letterlist)

# Part Two
sameletters = []
# print(s[:3])
for i in range(0,len(s),3):
    a = list(set(s[i])&set(s[i+1])&set(s[i+2]))
    for i in a:
        # print(i)
        sameletters.append(i)

calcSum(sameletters, letterlist)