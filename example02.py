import plotly.plotly as py
import plotly.graph_objs as go

#Get data from csv file
data = open('Real_Final_database_02.csv')
alldata = data.readlines()
listdata = []
for i in alldata:
    listdata.append(i.strip().split(','))

#Seperate each list to display in graph
country = input()
types = input()
year = []
affect = []
damage = []
death =[]
for j in listdata:
    if j[0] == country and j[2] == types:
        year.append(int(j[1]))
        affect.append(int(j[3]))
        damage.append(int(j[4]))
        death.append(int(j[5]))
    
#Put the data of graph
trace1 = go.Scatter(
    x = year,
    y = affect,
    name = 'Total Affected' 
)
trace2 = go.Scatter(
    x = year,
    y = damage,
    name = 'Total Damage',
    yaxis='y2'
)
trace3 = go.Scatter(
    x = year,
    y = death,
    name = 'Total Death',
    yaxis='y3'
)

#arrange and colour
data = [trace1, trace2, trace3]
layout = go.Layout(
    title = 'ASIAN DISASTER',
    width = 8000,
    xaxis=dict(
        domain=[0.3, 0.7]
    ),
    yaxis=dict(
        title = 'Total Affected',
        titlefont=dict(
            color='#ff8247'
        ),
        tickfont=dict(
            color='#ff8247'
        )
    ),
    yaxis2=dict(
        title = 'Total Damage',
        titlefont=dict(
            color='#EE00EE'
        ),
        tickfont=dict(
            color='#EE00EE'
        ),
        anchor='free',
        overlaying='y',
        side='left',
        position=0.15
    ),
    yaxis3=dict(
        title = 'Total Death',
        titlefont=dict(
            color='#ff6a6a'
        ),
        tickfont=dict(
            color='#ff6a6a'
        ),
        anchor='x',
        overlaying='y',
        side='right'
    ),
)
fig = go.Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='pdeesawat69')
