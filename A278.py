def isBadVersion(x):
    if x >= 666:
        return True
    else:
        return False

def firstBadVersion(n: int) -> int:
    l, r = 1, n
    c = 0
    while (r-l>1):
        z = (r + l)//2
        if (isBadVersion(z)):
            r = z
        else:
            l = z
        c += 1
    if (isBadVersion(l)):
        return l, c+1
    else:
        return r, c+1

print("Answer: ", firstBadVersion(1000000)[0], "Count: ", firstBadVersion(1000000)[1])
