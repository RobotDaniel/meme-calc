
def mainMenu():
    main=input("1.Enter the app\n2.Quit")
    if main == "1":
        getInputs()
    elif main == "2":
        print("")
    else:
        print("Invalid Input")
        mainMenu()
    

def getInputs():
    global operation
    global firstNumber
    global secondNumber
     
    operation=input("Select operation \n 1. + Add \n2. - subtract \n3. / divide  \n4. * muliply")
    
    firstNumber=input("First Number")
    secondNumber=input("Second Number")
    
    errorHandling()
    checkOperation()
def errorHandling():
    try:
        
        float(firstNumber)
        float(secondNumber)
    except:
        print("Invalid Input")
        getInputs()

    
def checkOperation():
    if operation == "1" and float(firstNumber) == 9.0 and float(secondNumber) == 10.0:
        ninePlusTen()
        mainMenu()
    
    elif operation == "1":
        add()
        mainMenu()
    elif operation == "2":
        subtract()
        mainMenu()
    elif operation == "3":
        divide()
        mainMenu()
    elif operation == "4":
        multiply()
        mainMenu()
    else:
        print("Invalid Input")
        getInputs()

def add():
    print(float(firstNumber)+float(secondNumber))
def ninePlusTen():
    print(float(firstNumber)+float(secondNumber)+2)
    
def subtract():
    print(float(firstNumber)-float(secondNumber))
def divide():
    print(float(firstNumber)/float(secondNumber))
def multiply():
    print(float(firstNumber)/float(secondNumber))
mainMenu()

