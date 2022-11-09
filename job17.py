def myFunction( *params ):
    myList = []
    for param in params:
        if isinstance(param, (int)):
            myList.append(param)
        else :
            print("un des paramètre n'est pas numérique")

    for element in myList:
        if element % 2 == 0:
            print(element)   
myFunction(5,9,10,44,56,)    
    