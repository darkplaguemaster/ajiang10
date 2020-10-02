"""
Andrew Jiang (Team Name: Team Windows 9 with Benjamin Gallai and Ian Chen-Adamczyk)
SoftDev
K07 -- StI/O: Divine your Destiny!/Read in a csv file, print out a random the a occupation with respect to the percentages given
2020-10-02
"""

import random
def csv_format(csv):
    with open(csv, 'r') as in_stream:
        ls = in_stream.read()

    ls = ls.split('\n')

    for i in range(len(ls)):
        if ls[i] == '':
            ls.pop(i)

    return ls

def randomOccupation(dictionary):
    percentageSum = sum(dictionary.values())
    percentageRandom = random.random() * percentageSum
    percentageIndex = 0
    for key in dictionary:
        if percentageIndex + dictionary[key] > percentageRandom:
            return key
        else:
            percentageIndex += dictionary[key]

if __name__ == "__main__":
        inp = "y"
        jobs = csv_format("occupations.csv")
        jdict = {}

        del jobs[0]
        del jobs[-1]
        for i in jobs:
            if '"' not in i:
                cur = i.split(",")
            else:
                cur = i[1:].split('",')

            jdict[cur[0]] = float(cur[1])

        while inp == "y":
                print(randomOccupation(jdict))
                inp = str(input("Next Occupation? (y/n)")).lower()





