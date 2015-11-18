from pylab import *
data = open('database.csv')
alldata = data.readlines()
listdata = []
for i in alldata:
    listdata.append(i.strip().split(','))
x = []
y = []
country = input()
year = input()
for j in listdata:
    if j[0] == country and j[1] == year:
        x.append(int(j[4]))
        print(j[3], "Total Damage = "+j[4]+" $.")
plot(x)
show()
