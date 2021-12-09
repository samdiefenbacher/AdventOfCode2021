import copy as cp

puzzleInput = [1,1,5,2,1,1,5,5,3,1,1,1,1,1,1,3,4,5,2,1,2,1,1,1,1,1,1,1,1,3,1,1,5,4,5,1,5,3,1,3,2,1,1,1,1,2,4,1,5,1,1,1,4,4,1,1,1,1,1,1,3,4,5,1,1,2,1,1,5,1,1,4,1,4,4,2,4,4,2,2,1,2,3,1,1,2,5,3,1,1,1,4,1,2,2,1,4,1,1,2,5,1,3,2,5,2,5,1,1,1,5,3,1,3,1,5,3,3,4,1,1,4,4,1,3,3,2,5,5,1,1,1,1,3,1,5,2,1,3,5,1,4,3,1,3,1,1,3,1,1,1,1,1,1,5,1,1,5,5,2,1,5,1,4,1,1,5,1,1,1,5,5,5,1,4,5,1,3,1,2,5,1,1,1,5,1,1,4,1,1,2,3,1,3,4,1,2,1,4,3,1,2,4,1,5,1,1,1,1,1,3,4,1,1,5,1,1,3,1,1,2,1,3,1,2,1,1,3,3,4,5,3,5,1,1,1,1,1,1,1,1,1,5,4,1,5,1,3,1,1,2,5,1,1,4,1,1,4,4,3,1,2,1,2,4,4,4,1,2,1,3,2,4,4,1,1,1,1,4,1,1,1,1,1,4,1,5,4,1,5,4,1,1,2,5,5,1,1,1,5]

testInput = [3,4,3,1,2]

class Groups(object):
    group0 = 0
    group1 = 0
    group2 = 0
    group3 = 0
    group4 = 0
    group5 = 0
    group6 = 0
    group7 = 0
    group8 = 0

def solvePuzzle(input):
    groups = Groups()
    count = 0

    # populate
    for num in input:
        if num == 0:
            groups.group0 += 1
        if num == 1:
            groups.group1 += 1
        if num == 2:
            groups.group2 += 1
        if num == 3:
            groups.group3 += 1
        if num == 4:
            groups.group4 += 1
        if num == 5:
            groups.group5 += 1

    while count < 257:
        if count == 0:
            print(groups.group0 + groups.group1 + groups.group2 + groups.group3 + groups.group4 + groups.group5 + groups.group6 + groups.group7, count)
            print(groups.group0 , groups.group1 , groups.group2 , groups.group3 , groups.group4 , groups.group5 , groups.group6 , groups.group7)
        group0Old = groups.group0
        groups.group0 = groups.group1
        groups.group1 = groups.group2
        groups.group2 = groups.group3
        groups.group3 = groups.group4
        groups.group4 = groups.group5
        groups.group5 = groups.group6
        groups.group6 = groups.group7 + group0Old
        groups.group7 = groups.group8
        groups.group8 =  group0Old

        print(groups.group0 + groups.group1 + groups.group2 + groups.group3 + groups.group4 + groups.group5 + groups.group6 + groups.group7, count)

        count += 1
        

def main():
    print(solvePuzzle(puzzleInput))

main()