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
    if j[0] == 'Indonesia'and j[2] == 'Flood':
        year.append(int(j[1]))
        affect.append(int(j[3]))
        damage.append(int(j[4]))
        death.append(int(j[5]))
        
import plotly.plotly as py
import plotly.graph_objs as go

death = go.Scatter(
    x=year,
    y=death,
    mode='markers',
    marker=dict(
        color=['#FF8C00' for i in death],
        opacity=[0.4 for i in death],
        size=[15 for i in death],
    )
)

damage = go.Scatter(
    x=year,
    y=damage,
    mode='markers',
    marker=dict(
        color=['#FF0000' for i in damage],
        opacity=[0.6 for i in damage],
        size=[25 for i in damage],
    )
)

affect = go.Scatter(
    x=year,
    y=affect,
    mode='markers',
    marker=dict(
        color=['#FFBBFF' for i in damage],
        opacity=[0.8 for i in damage],
        size=[10 for i in damage],
    )
)

data = [death, damage, affect]
layout = go.Layout(
    showlegend=True,
    height=600,
    width=600,
)
fig = go.Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='pdeesawat69_2')