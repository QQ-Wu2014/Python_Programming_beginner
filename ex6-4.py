day = int(input("please num 1-7"))
match day:
    case 1 | 2 | 3 | 4 | 5 :
        print("Bad Week day")
    case 6 | 7 :
        print("Best Week day")
    case  _ :
        print("please input num 1~7")
