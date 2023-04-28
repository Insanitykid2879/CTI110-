#taking numofscores as input from user
numofscores=int(input("How many scores do you want to enter? "))

#creating an empty list to store scores
scoreslist=[]

#for loop to take scores as inputs
for i in range(1,numofscores+1):
    
    #while loop to take input until user enters correct input
    while True:
        try:
            #taking score as input from user
            score=int(input("Enter score #{}: ".format(i)))
            
            #checking if score is between 0 and 100
            if score>=0 and score<=100:
                
                #if yes, then appends to list
                scoreslist.append(score)
                break
            #if not, then prints this and asks for input again
            else:
                print("\nINVALID Score entered!!!!\nScore should be between 0 and 100")
        except:
            continue
print("--------------Results--------------")
#printing lowest score entered
lowestscore=min(scoreslist)
print("Lowest score entered: {}".format(lowestscore))

#rprinting modified list after dropping lowest score
scoreslist.remove(lowestscore)
print("Modified List : ",scoreslist )
#printing average of modified scoreslist
avgofscoreslist=sum(scoreslist)/len(scoreslist)
print("Scores Average: {}".format(avgofscoreslist))
#printing letter grade
print("Letter grade of average of modified scoreslist: ")
if avgofscoreslist>80 and avgofscoreslist<=100:
    print("Letter grade: A")
elif avgofscoreslist>60 and avgofscoreslist<=80:
    print("Letter grade: B") 
elif avgofscoreslist>40 and avgofscoreslist<=60:
    print("Letter grade: C")
elif avgofscoreslist>20 and avgofscoreslist>=40:
    print("Letter grade: D")
else:
    print("Letter grade: E")
print("-----------------------------------")
