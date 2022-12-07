import math
import collections
import csv
import re

# git add - A, commit -m"message", push (to add files to REPO)
# git pull (to get files from REPO)

# all contributors
#zc285
#ass209
#kap401
#arb295


# 1.1
def findPercentage (file):
    
    typeToLevelDict = {}

    # how to read from a CSV
    with open(file) as pokedex:
        reader = csv.DictReader(pokedex, delimiter=',')
        next(reader)
        for row in reader:
            #print(row)
            if row['type'] not in typeToLevelDict.keys():
                typeToLevelDict[row['type']] = []
                typeToLevelDict[row['type']].append(row['level'])
            else:
                typeToLevelDict[row['type']].append(row['level'])

    
    #print(typeToLevelDict.items())
    countOfFirePokemon = len([i for i in typeToLevelDict["fire"]])

    countOfFirePokemon40 = len([i for i in typeToLevelDict["fire"] if float(i) > 40])

    percentage = (countOfFirePokemon40/countOfFirePokemon) * 100

    accurate_percentage = round(percentage)
    with open("pokemon1.txt", "w") as f:
        f.write(f"Percentage of fire type pokemon over level 40 = {accurate_percentage}")


def MostFrequentElement(lis):
    return max(set(lis), key = lis.count)

# 1.2     
def missingType(file):
    WeaknessToTypeDict = {}

    with open(file) as pokedex:
        csv_reader = csv.DictReader(pokedex, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            if row['weakness'] not in WeaknessToTypeDict.keys() and row['type'] != "NaN":
                WeaknessToTypeDict[row['weakness']] = []
                WeaknessToTypeDict[row['weakness']].append(row['type'])
            elif row['type'] != "NaN":
                WeaknessToTypeDict[row['weakness']].append(row['type'])
        pokedex.close()   


    with open(file, "r") as inp:
        reader = csv.DictReader(inp.readlines())
        

    with open("pokemonResult.csv", 'w') as out:
        writer = csv.DictWriter(out, fieldnames = reader.fieldnames, delimiter=',')
        writer.writeheader()
        for row in reader:
            
            if row['type'] == "NaN":
                mostCommonElement = MostFrequentElement(WeaknessToTypeDict[row['weakness']])
                row['type'] = mostCommonElement
                
                writer.writerow(row)
                
            else:
                writer.writerow(row)
        
# 1.3
def missingVals(file):
    keyList = ["atk", "hp", "def"]
    Level40 = {}    
    UnderLevel40 = {}
    for i in keyList:
        Level40[i] = []
        UnderLevel40[i] = []
    
    with open(file) as pokedex:
        csv_reader = csv.DictReader(pokedex, delimiter=',')
        #next(csv_reader)
        for row in csv_reader:
            if row['hp'] != "NaN":
                if float(row['level']) <= 40.0:
                    UnderLevel40['hp'].append(float(row['hp']))
                else:
                    Level40['hp'].append(float(row['hp']))
            if row['atk'] != "NaN":
                if float(row['level']) <= 40.0:
                    UnderLevel40['atk'].append(float(row['atk']))
                else:
                    Level40['atk'].append(float(row['atk']))
            if row['def'] != "NaN":
                if float(row['level']) <= 40.0:
                    UnderLevel40['def'].append(float(row['def']))
                else:
                    Level40['def'].append(float(row['def']))
    
    #print(Level40)
    #print(UnderLevel40)
    
    for i in Level40.keys():
        Level40[i] = round(sum(Level40[i]) / len(Level40[i]), 1)
        UnderLevel40[i] = round(sum(UnderLevel40[i]) / len(UnderLevel40[i]), 1)
    

    
    with open("pokemonResult.csv", "r") as inp:
        reader = csv.DictReader(inp.readlines())
        

    with open("pokemonResult.csv", 'w') as out:
        writer = csv.DictWriter(out, fieldnames = reader.fieldnames, delimiter=',')
        writer.writeheader()
        for row in reader:
             if row['hp'] == "NaN":
                if float(row['level']) <= 40.0:
                    row['hp'] = UnderLevel40['hp']
                    
                else:
                    row['hp'] = Level40['hp']
                    
            

             if row['atk'] == "NaN":
                if float(row['level']) <= 40.0:
                    row['atk'] = UnderLevel40['atk']
                    
                else:
                    row['atk'] = Level40['atk']
                    
             
             if row['def'] == "NaN":
                if float(row['level']) <= 40.0:
                    row['def'] = UnderLevel40['def']
                    
                else:
                    row['def'] = Level40['def']
             writer.writerow(row)      

                
# 1.4
def personalityDict(file):
    typeToPersonality = {}
    with open(file, "r") as pokedex:
        csv_reader = csv.DictReader(pokedex, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            if row['type'] not in typeToPersonality.keys():
                typeToPersonality[row['type']] = []
                typeToPersonality[row['type']].append(row['personality'])
            elif row['personality'] not in typeToPersonality[row['type']]:
                typeToPersonality[row['type']].append(row['personality'])
        
    sorted_dict = {}
    for key in sorted(typeToPersonality):
        sorted_dict[key] = sorted(typeToPersonality[key]) 
    
    with open("pokemon4.txt", "w") as output:
        output.write(f"Pokemon type to personality mapping:\n")
        for key in sorted_dict.keys():
            output.write(f"{key} : {sorted_dict[key]}\n")

    
    
# 1.5
def avgHitPoints(file):
    HitPoints = []

    with open(file, "r") as pokedex:
        csv_reader = csv.DictReader(pokedex, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            if row['stage'] == '3.0':
                HitPoints.append(float(row['hp']))
    #print(HitPoints)
    averageHP = sum(HitPoints) / len(HitPoints)
    #print(averageHP)

    with open("pokemon5.txt", "w") as output:
        output.write(f"Average hit point for pokemon of stage 3.0 = {round(averageHP)}")


def main():
    findPercentage("pokemonTrain.csv")
    missingType("pokemonTrain.csv")
    missingVals("pokemonResult.csv")
    personalityDict("pokemonResult.csv")
    avgHitPoints("pokemonResult.csv")
main()    
