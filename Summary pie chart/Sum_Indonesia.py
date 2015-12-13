import plotly.plotly as py

"""Get data from csv and split it"""
data = open('Real_Final_database_02.csv')
alldata = data.readlines()
listdata = []
for ix in alldata:
    listdata.append(ix.strip().split(','))

"""Seperate data in each type of disaster."""
all_disaster = {'Drought':0, 'Flood':0, 'Storm':0, 'Epidemic':0, 'Earthquake':0}
for iy in listdata:
        if iy[0] == 'Indonesia' and iy[2] in all_disaster:
            all_disaster[iy[2]] += 1

"""Calculate each type for make an average."""
total = sum(all_disaster.values())
average = []
for iz in all_disaster:
    all_disaster[iz] = float("%.2f" % ((all_disaster[iz]/total)*100))
label = [i for i in all_disaster]
value = [all_disaster[j] for j in label]

"""Apprerance"""
make_circle = {"data": [{"values":value,"labels":label,
"name": "Average", "hoverinfo":"label+percent+name", "hole": 0.39, "type": "pie"}], 
"layout": {"title":"Indonesia's Average Disaster from 2000 to 2014", "annotations": [{"font": {"size": 20},
"showarrow": False, "text": ""}]}}

url = py.plot(make_circle, filename='Indonesia\'s Average Disaster from 200o to 2014')
