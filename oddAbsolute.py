def calculateAbsolute():
    
    # This first line is provided for you
    in_num  = int(input("Enter a number: "))
    
    if in_num > 21:
    #double the absolute difference
        absoluteDiff = abs(in_num - 21) * 2
        print ("Result:", absoluteDiff) 
    elif in_num <= 21:
        absoluteDiff = abs(in_num-21)
        print("Result:", absoluteDiff)
    
        

    # end assignment

## If you want to test locally run > python payCalculator.py

if __name__ == "__main__":
    calculateAbsolute()
