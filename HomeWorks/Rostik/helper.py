import time
mainIsOn = True
targetValue = -1
while mainIsOn:
    print("Select category\n"
          "0 - Close App\n"
          "1 - Lists\n"
          "2 - While\n")
    if targetValue == -1:
        try:
            targetValue = int(input())
        except ValueError as e:
            print("Wrong statement. Try again!")
            targetValue = -1
    if targetValue == 1:
        print("List = []\n"
              "Initialize empty list\n"
              "List = [a, b, c]\n"
              "Initialize string List\n"
              "List = [1, 2, 3]\n"
              "Initialize string list\n")
        time.sleep(5)
        targetValue = -1
    if targetValue == 2:
        print("while boolean(True of False)\n"
              "Or \n"
              "a = 0\n"
              "while a < 100:\n"
              "print(do something)\n"
              "a = a + 1")
        print("Operator break\n"
              "force stop circle while and if")
        time.sleep(5)
        targetValue = -1
    if targetValue == 0:
        print("Close app")
        time.sleep(1)
        print("5")
        time.sleep(1)
        print("4")
        time.sleep(1)
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        mainIsOn = False
        time.sleep(1)
        print("Bye Bye!")
