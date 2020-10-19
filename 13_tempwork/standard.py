#!/usr/bin/env python
# Team SeniorMars: Andrew Jiang, Saqif Abedin, and Carlos Hernandez
# SoftDev
# K13: Template for Success: Started working with tuples to iterate with jinja.
# 2020-10-19
import csv
from random import choices

key = []
links = []
values = []
with open("./data/occupations.csv", "r", newline='') as csv_file:
    # occupations = {} # we don't want to use a dictionary cuz our methods
    # require lists
    # we are lazy so we used the csv library
    reader = csv.reader(csv_file, delimiter=',')
    for row in reader:
        if not (row[0] == "Job Class" or row[0] == "Total"): # skip over lines
            key.append(row[0])
            links.append(row[1])
            values.append(float(row[2]))


def get_all_jobs() -> list:
    return key

def get_occupations() -> tuple:
    # we found that you had to zip to create a tuple so
    # jinja can iterate through each list
    return zip(key, links, values)


def get_random_occupations() -> str:
    return choices(key, values, k=1)[0]


if __name__ == "__main__":
    print(get_random_occupations())
