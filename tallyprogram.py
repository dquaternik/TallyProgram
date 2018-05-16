# Reddit Challenge #361 Tally Program
# 5 Friends (let's call them a, b, c, d and e) are playing a game and need to keep track of the scores. Each time 
# someone scores a point, the letter of his name is typed in lowercase. If someone loses a point, the letter of his name 
# is typed in uppercase. Give the resulting score from highest to lowest.
# Input Description
# A series of characters indicating who scored a point. Examples:
# 
# abcde
# dbbaCEDbdAacCEAadcB
# 
# Output Description
# The score of every player, sorted from highest to lowest. Examples:
#
# a:1, b:1, c:1, d:1, e:1
# b:2, d:2, a:1, c:0, e:-2
# 
# Challenge Input
# EbAAdbBEaBaaBBdAccbeebaec


def main():
    
    #Take input for the scores
    raw_scores = input('Please enter the scores here: ')

    scores = [['a',0],
                ['b',0],
                ['c',0],
                ['d',0],
                ['e',0]]

    #Tally scores from raw scores
    for char in raw_scores:
        if char=='a':
            scores[0][1] += 1
        elif char=='b':
            scores[1][1] +=1
        elif char=='c':
            scores[2][1] +=1
        elif char=='d':
            scores[3][1] +=1
        elif char=='e':
            scores[4][1] +=1
        #Remove Points
        elif char=='A':
            scores[0][1] -=1
        elif char=='B':
            scores[1][1] -=1
        elif char=='C':
            scores[2][1] -=1
        elif char=='D':
            scores[3][1] -=1
        elif char=='E':
            scores[4][1] -=1

    scores.sort(key=lambda x:x[1], reverse=True)
    print(scores)


main()
