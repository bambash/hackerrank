def checkMagazine(magazine, note):
    # match = "Yes"
    # for i in note:
    #     if i in magazine:
    #         magazine.remove(i)
    #     else:
    #         match = "No"
    # print(match)
    from collections import Counter
    a = Counter(magazine)
    b = Counter(note)
    if (a & b) == b:
        print("Yes")
    else:
        print("No")


magazine = "two times three is not four".split()
note = "two times two is four".split()

print(checkMagazine(magazine, note))
# if __name__ == '__main__':
#     mn = input().split()

#     m = int(mn[0])

#     n = int(mn[1])

#     magazine = input().rstrip().split()

#     note = input().rstrip().split()

#     print(checkMagazine(magazine, note))
