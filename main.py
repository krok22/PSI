import csv
# import numpy as np


class Country:

    def __init__(self, name, happinessRank, happinessScore, economy, family, health, freedom, trust, generosity, dystopiaResidual):
        self.name = name
        self.happinessRank = happinessRank
        self.happinessScore = happinessScore
        self.economy = economy
        self.family = family
        self.health = health
        self.freedom = freedom
        self.trust = trust
        self.generosity = generosity
        self.dystopiaResidual = dystopiaResidual

    def getName(self):
            return self.name

    def getHappinessRank(self):
            return self.happinessRank

    def getHappinessScore(self):
            return self.happinessScore

    def getEconomy(self):
            return self.economy

    def getFamily(self):
            return self.family

    def getHealth(self):
            return self.health

    def getFreedom(self):
            return self.freedom

    def getTrust(self):
            return self.trust

    def getGenerosity(self):
            return self.generosity

    def getDystopiaResidual(self):
            return self.dystopiaResidual

class DataSet:

    def __init__(self):
        self.countriesNumber = 0
        self.csvreader = ''
        self.csvfile = ''
        self.countries = []

    def setFile(self, file):
        self.csvfile = open(file, 'r', encoding="utf8", newline='')

    def loadFromFile(self):
        self.csvreader = csv.reader(self.csvfile, delimiter=';')
        i = 0
        for row in self.csvreader:
            if i != 0:
                self.countries.append(Country(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))
            i += 1
        self.countriesNumber = i

    def getCountry(self, number):
        return self.countries[number]

    def getCountriesNumber(self):
        return self.countriesNumber

def main():
    data2015 = DataSet()
    data2015.setFile('./input/2015fixed.csv')
    data2015.loadFromFile()
    print("Name\tHappiness rank\tHappiness score\tEconomy\tFamily\tHealth\tFreedomtTrust\tGenerosity\t Dystopia residual")

    for x in range(0, data2015.getCountriesNumber()-1):
        print(data2015.getCountry(x).getName() + '\t' + data2015.getCountry(x).getHappinessRank() + '\t' + data2015.getCountry(x).getHappinessScore() + '\t' + data2015.getCountry(x).getEconomy() + '\t' + data2015.getCountry(x).getFamily() + '\t' + data2015.getCountry(x).getHealth() + '\t' + data2015.getCountry(x).getFreedom() + '\t' + data2015.getCountry(x).getTrust() + '\t' + data2015.getCountry(x).getGenerosity() + '\t' + data2015.getCountry(x).getDystopiaResidual())
    print("############################################################################################################################################################\n\n")


    data2016 = DataSet()
    data2016.setFile('./input//2016fixed.csv')
    data2016.loadFromFile()
    print("Name\tHappiness rank\tHappiness score\tEconomy\tFamily\tHealth\tFreedomtTrust\tGenerosity\t Dystopia residual")

    for x in range(0, data2016.getCountriesNumber() - 1):
        print(data2016.getCountry(x).getName() + '\t' + data2016.getCountry(x).getHappinessRank() + '\t' + data2016.getCountry(x).getHappinessScore() + '\t' + data2016.getCountry(x).getEconomy() + '\t' + data2016.getCountry(x).getFamily() + '\t' + data2016.getCountry(x).getHealth() + '\t' + data2016.getCountry(x).getFreedom() + '\t' + data2016.getCountry(x).getTrust() + '\t' + data2016.getCountry(x).getGenerosity() + '\t' + data2016.getCountry(x).getDystopiaResidual())
    print("############################################################################################################################################################\n\n")



    data2017 = DataSet()
    data2017.setFile('./input//2017fixed.csv')
    data2017.loadFromFile()
    print("Name\tHappiness rank\tHappiness score\tEconomy\tFamily\tHealth\tFreedomtTrust\tGenerosity\t Dystopia residual")

    for x in range(0, data2017.getCountriesNumber() - 1):
        print(data2017.getCountry(x).getName() + '\t' + data2017.getCountry(x).getHappinessRank() + '\t' + data2017.getCountry(x).getHappinessScore() + '\t' + data2017.getCountry(x).getEconomy() + '\t' + data2017.getCountry(x).getFamily() + '\t' + data2017.getCountry(x).getHealth() + '\t' + data2017.getCountry(x).getFreedom() + '\t' + data2017.getCountry(x).getTrust() + '\t' + data2017.getCountry(x).getGenerosity() + '\t' + data2017.getCountry(x).getDystopiaResidual())
    print("############################################################################################################################################################\n\n")


main()