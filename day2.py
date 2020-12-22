from collections import Counter


def parse(line):
    [policy, pw] = line.strip().split(":")

    return policy, pw.strip()


def check_policy(policy, pw):
    [times, char] = policy.split(" ")
    counter = Counter(pw)
    [mint, maxt] = [int(t) for t in times.split("-")]
    return counter[char] >= mint and counter[char] <= maxt


with open("day2.txt") as f:
    lines = [parse(line) for line in f.readlines()]

count = 0
for policy, pw in lines:
    if check_policy(policy, pw):
        count += 1
print(count)


def check_policy_2(policy, pw):
    [pos, char] = policy.split(" ")
    [leftp, rightp] = [int(t) - 1 for t in pos.split("-")]
    return (pw[leftp] == char) ^ (pw[rightp] == char)


count = 0
for policy, pw in lines:
    if check_policy_2(policy, pw):
        count += 1
print(count)
