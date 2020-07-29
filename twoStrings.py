def twoStrings(s1, s2):
    print(set(s1))
    print(set(s2))
    print(set(s1) & set(s2))
    if set(s1) & set(s2):
        print("Yes")
    else:
        print("No")


twoStrings("hello friend", "bugs")
