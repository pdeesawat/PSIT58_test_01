import plotly.plotly as py
import plotly.graph_objs as go

#Get data
data = open('Real_Final_database_02.csv')
alldata = data.readlines()
listdata = []
for i in alldata:
    listdata.append(i.strip().split(','))

#Seperate information
year = []
affect = []
damage = []
death =[]
for j in listdata:
    if j[0] == 'Malaysia' and j[2] == 'Drought':
        year.append(int(j[1]))
        affect.append(int(j[3]))
        damage.append(int(j[4]))
        death.append(int(j[5]))

# Create and style traces
trace1 = go.Scatter(
    x=year,
    y=affect,
    mode='lines+markers',
    name="'Total Affected'",
    hoverinfo='Total Affected',
    line = dict(
        shape='spline',
        color = ('00CC00'),
        width = 1.5),
)
trace2 = go.Scatter(
    x=year,
    y=damage,
    mode='lines+markers',
    name='Total Damage \'000 US',
    hoverinfo='Total Damage \'000 US',
    line = dict(
        shape='spline',
        color = ('3399FF'),
        width = 1.5),
    yaxis='y2'
)
trace3 = go.Scatter(
    x=year,
    y=death,
    mode='lines+markers',
    name='Total Death',
    hoverinfo='Total Death',
    line = dict(
        shape='spline',
        color = ('FF3300'),
        width = 1.5),
    yaxis='y3'
)

data = [trace1, trace2, trace3]
layout = go.Layout(
    title='Drought in Malaysia',
    yaxis=dict(
        title='Total affected',
        titlefont=dict(
            color='00CC00'
        ),
        tickfont=dict(
            color='00CC00'
        )
    ),
    yaxis2=dict(
        title='Total Damage \'000 US',
        titlefont=dict(
            color='3399FF'
        ),
        tickfont=dict(
            color='3399FF'
        ),
        anchor='free',
        overlaying='y',
        side='left',
        position=0.15
    ),
    yaxis3=dict(
        title='Total Death',
        titlefont=dict(
            color='FF3300'
        ),
        tickfont=dict(
            color='FF3300'
        ),
        anchor='x',
        overlaying='y',
        side='right'
    )
)
fig = go.Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='bennyy')
