def countingValleys(n, s):
    sealevel = 0
    valleys = 0

    for step in s:
        if step == "U":
            sealevel += 1
        else:
            sealevel -= 1

        if step == "U" and sealevel == 0:
            valleys += 1
    return valleys


print(countingValleys(8, 'UDDDUDUU'))

