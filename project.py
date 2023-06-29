import datetime 
import random  
while True:   
    correct, count, totalquestions = 0, 0, 5 
    startTime = datetime.datetime.now()
    print("The quiz has started")
    print("Time:", startTime)
    
    while totalquestions>0:
    
        a = random.randint(0, 9)
        b = random.randint(0, 9)
        
        print("What is", a, "^", b, "?")  
        answer = int(input())
        
        if answer == a**b:
            print("You are correct!")
            correct += 1 
            count += 1 
        else:
            print("You are wrong! Correct answer is", a**b)
            count += 1
        totalquestions -= 1
    
    endTime = datetime.datetime.now()
    totalTime = endTime - startTime
    
    print("The number of points received are", correct, "out of", count)
    print("The time taken to complete the quiz: ", totalTime)
    
    choice = input("Do you want to retake the quiz? Type Y/N: ")
    if choice == 'N' or choice == 'n':
        break    