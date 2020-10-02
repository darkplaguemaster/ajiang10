
"""
Andrew Jiang (Team Name: Team Windows 9 with Benjamin Gallai and Ian Chen-Adamczyk)
SoftDev
K06 -- Learnination Through Amalgamation, simplifiyed K05 code for picking random value from dictionary
2020-10-02
"""

import random

KREWES = {
    'orpheus': ['ERIC', 'SAUVE', 'JONATHAN', 'PAK', 'LIAM', 'WINNIE', 'KELLY', 'JEFFREY', 'KARL', 'ISHITA', 'VICTORIA', 'BENJAMIN', 'ARIB', 'AMELIA', 'CONSTANCE', 'IAN'],
    'rex': ['ANYA', 'DUB-Y', 'JESSICA', 'ALVIN', 'HELENA', 'MICHELLE', 'SHENKER', 'ARI', 'STELLA', 'RENEE', 'MADELYN', 'MAC', 'RYAN', 'DRAGOS'],
    'endymion': ['JASON', 'DEAN', 'MADDY', 'SAQIF', 'CINDY', 'YI LING', 'RUOSHUI', 'FB', 'MATTHEW', 'MAY', 'ERIN', 'MEIRU']
}
team = input("Pick a team from orpheus, rex, or endymion: ").lower()
while team not in KREWES:
    team = input("Please enter either orpheus, rex, or endymion: ").lower()
print(random.choice(KREWES[team]))
