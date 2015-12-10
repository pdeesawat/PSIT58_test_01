import plotly.plotly as py
import plotly.graph_objs as go

#Get data from csv file
data = open('Real_Final_database_02.csv')
alldata = data.readlines()
listdata = []
for i in alldata:
    listdata.append(i.strip().split(','))

#Seperate each list to display in graph
year = []
affect = []
damage = []
death =[]
for j in listdata:
    if j[0] == 'Lao' and j[2] == 'Flood':
        year.append(int(j[1]))
        affect.append(int(j[3]))
        damage.append(int(j[4]))
        death.append(int(j[5]))

trace0 = go.Bar(
    x=year,
    y=affect,
    name='Affect',
    marker=dict(
        color='#FFBBFF'
    )
)

trace1 = go.Bar(
    x=year,
    y=damage,
    name='Damage',
    marker=dict(
        color='#FF0000',
    )
)

trace2 = go.Bar(
    x=year,
    y=death,
    name='Death',
    marker=dict(
        color='#FF8C00',
    )
)


data = [trace0, trace1, trace2]
layout = go.Layout(
    xaxis=dict(
        # set x-axis' labels direction at 45 degree angle
        tickangle=-45,
        tickfont=dict(
            size=14,
            color='rgb(107, 107, 107)'
        )
    ),
    barmode='group',
    title='Flood In Lao',
    
    yaxis=dict(
        titlefont=dict(
            size=16,
            color='rgb(107, 107, 107)'
        ),
        tickfont=dict(
            size=14,
            color='rgb(107, 107, 107)'
        )
    ),
)
fig = go.Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='Lao_Flood')