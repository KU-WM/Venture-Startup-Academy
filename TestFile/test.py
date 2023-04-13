def solution(s):
    P = 0
    Y = 0
    
    for i in s.upper():
        if (i == "Y"):
            Y += 1
        elif (i == "P"):
            P += 1
    
    if(P == Y):
        print("true")
    else:
        print("false")

    print("P : " , P, "Y : ", Y)

    return True

a = input()

solution(a)