import plotly.plotly as py

#Get data from csv and split it
data = open('database_v0.csv')
alldata = data.readlines()
listdata = []
for ix in alldata:
    listdata.append(ix.strip().split(','))

#Get values of disaster in each country    
allcountry = ['Indonesia', 'Lao P Dem Rep', 'Malaysia', 'Philippines', 'Singapore',
           'Thailand', 'Cambodia', 'Viet Nam', 'Brunei', 'Myanmar']
country = ['IDN', 'LAO', 'MYS', 'PHL', 'SGP', 'THA', 'KHM', 'VNM', 'NBD', 'MMR']
listvalues = []
for iy in country:
    count = 0
    for iz in listdata:
        if iz[2] == iy:
            count += 1
    listvalues.append(count)
    
#Calculate to percent
summ = sum(listvalues)
value = []
for ia in listvalues:
    num = (ia/summ)*100
    value.append("%.2f" % num)
#listvalues = [float(ib) for ib in value]

#Apperence
pie_chart = {'data':[{'labels':allcountry, 'values':listvalues, "hoverinfo":"label+percent+name",
                      'type': 'pie'}], 'layout': {'title': 'Asian disaster'}}

url = py.plot(pie_chart)