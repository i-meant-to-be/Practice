import Stack

S = Stack.Stack()
Input = []

while True:
    Input.extend(input("※ 명령 입력 : ").split(" "))

    if Input[0] == "Pop":
        if S.IsEmpty() is True:
            print(" - 스택에 원소가 없음. \n")
        else:
            print(" - %d을(를) 제거함. \n" % (S.Pop()))
    elif Input[0] == "Push":
        print(" - %d을(를) 삽입함. \n" % (S.Push(int(Input[1]))))
    elif Input[0] == "Peek":
        print(" - 최상단 원소는 %d임. \n" % S.Peek())
    elif Input[0] == "IsEmpty":
        if S.IsEmpty() is True:
            print(" - 스택에 원소가 없음. \n")
        else:
            print(" - 스택에 원소가 1개 이상 존재함. \n")
    elif Input[0] == "HowMany":
        if S.IsEmpty() is True:
            print(" - 스택에 원소가 없음. \n")
        else:
            print(" - 스택에 원소가 %d개 존재함. \n" % S.HowMany())
    elif Input[0] == "Exit":
        print(" - 프로그램 종료. \n")
        exit()
    else:
        print(" - 유효하지 않은 입력. \n")

    Input.clear()
