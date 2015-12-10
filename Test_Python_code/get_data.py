"""Get data from csv file"""
data = open('Real_Final_database_02.csv') #Open file database that use
alldata = data.readlines()
listdata = []
for i in alldata:
    listdata.append(i.strip().split(',')) #Add data form database file into list
