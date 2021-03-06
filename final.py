"""Structured English
First create a main function that imports the text file in readme mode.
And adds that text file to a list. And that displayed the number of grades and average grade.
Then create a second function that calculates the percent of grades that are above the average.
"""
""" Psudocode
list = []
define main function
    scorelist = open file in read mode
    for every line in list,
        append it to the list as an integer
define a function for calculateing the average grade
    print = "number of grades" (len(list))

    average grade  = (sum(list))/ (len(list))

    print(average grade)
    aboveAvgList = empty
    for every variable in list
        if variable is > average grade
            aboveAvgList.append var
    percentAboveAvg = len aboveAvgList / len list * 100
    finalPercent = round the final grade
    print (finalPercent)
Call main()
Call calculate_percent_above_average
"""
scoreInt = []

def main():
    scoreList = open('final (1).txt', "r")
    for line in scoreList:
        scoreInt.append(int(line.strip()))

def calculate_percent_above_average():
    print ("number of grades: ", len(scoreInt))

    average = (sum(scoreInt)) / (len(scoreInt))

    print ("Average grade: ", average)
    aboveAverage = []
    for var in scoreInt:
        if var > average:
            aboveAverage.append(var)
    percentAboveAverage = ((len(aboveAverage)) / (len(scoreInt))) * 100
    finalPercent = round(percentAboveAverage, 2)
    print (finalPercent, "%")
main()
calculate_percent_above_average()
