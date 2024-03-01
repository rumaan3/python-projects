import DATA 
import random
import art


flag = True 
randomA = {}
randomB = {}
score = 0

data = DATA.data

print (art.logo)


def printLine(random):
    name = random['name']
    desc = random['description']
    foll = random['follower_count']
    country = random['country']
    print (f"{name}, a {desc} , from {country}")


while flag == True:
#choose a random from the list of data given and save to a variable (filter the name, description and country)

    print (f"score = {score}")
    
    if score == 0:
        randomA = random.choice(data)
    elif score > 0:
        randomA = randomB

    foll1 = randomA['follower_count']
    name1 = randomA['name']

#print the 1st variable
    printLine(randomA)
    print (art.vs)
#choose another random and save to a variable 
    randomB = random.choice(data)
    name2 = randomB['name']
#check whether the 1st variable and 2nd variable dont have the same values
    while name1 == name2:
        randomB = random.choice(data)
        name2 = randomB['name']

    foll2 = randomB['follower_count']
#print the 2nd variable
    printLine(random)
#ask the user to select if 1st varible is higher or lower than 2nd variable (based on followers)
    choose = input("who has more followers? TYPE 'A' or 'B'\n")
#compare the saved variables to check condition if 1>2 , if yes then higher , else lower 
    if foll1 > foll2:
        result = "a"
    else:
        result = "b"
#compare the result to user selected input if result == input then score +1 else fail 
    if choose == result:
        print ('You win \n')
        score +=1
        print (f" your score is {score}\n")
        print ("Once More!!!!!\n")
    else:
        print('you lose \n')
        print (f" your score is {score}\n")
        flag = False
        print('Game over!!!')












#if pass then flag is true (game repeats)
#if fail then end of game flag is false (display score)



