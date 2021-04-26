"""Accept a string from user and reverse that string after reversing change case of each letter
 upper to lower and lower to upper
 #input : InformaTIon TEChnology
 output: YGOLONHcet NOitAMROFNi """

def main():
    str_input=input("enter a string to reverse")
    result=change(str_input)

    print("result after changing case and reversed it",result)

def change(str_input):

    name="".join(reversed(str_input))
    res=changecase(name)
    return res

def changecase(name):

    return (name.swapcase())


if __name__ == "__main__":
    main()