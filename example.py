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
affected = []
damage = []
death =[]
for j in listdata:
    if j[0] == country and j[2] == types:
        year.append(int(j[1]))
        affected.append(int(j[3]))
        damage.append(int(j[4]))
        death.append(int(j[5]))
    #print(year)
    #print(affected)
    #print(damage)
    #print(death)
    
#code that we have to write for make line in praph
trace1 = go.Scatter(
    x=[1, 2, 3],
    y=[4, 5, 6],
    name='yaxis1 data'
)
trace2 = go.Scatter(
    x=[2, 3, 4],
    y=[40, 50, 60],
    name='yaxis2 data',
    yaxis='y2'
)
trace3 = go.Scatter(
    x=[4, 5, 6],
    y=[40000, 50000, 60000],
    name='yaxis3 data',
    yaxis='y3'
)
trace4 = go.Scatter(
    x=[5, 6, 7],
    y=[400000, 500000, 600000],
    name='yaxis4 data',
    yaxis='y4'
)
data = [trace1, trace2, trace3, trace4]
layout = go.Layout(
    title='multiple y-axes example',
    width=800,
    xaxis=dict(
        domain=[0.3, 0.7]
    ),
    yaxis=dict(
        title='yaxis title',
        titlefont=dict(
            color='#1f77b4'
        ),
        tickfont=dict(
            color='#1f77b4'
        )
    ),
    yaxis2=dict(
        title='yaxis2 title',
        titlefont=dict(
            color='#ff7f0e'
        ),
        tickfont=dict(
            color='#ff7f0e'
        ),
        anchor='free',
        overlaying='y',
        side='left',
        position=0.15
    ),
    yaxis3=dict(
        title='yaxis4 title',
        titlefont=dict(
            color='#d62728'
        ),
        tickfont=dict(
            color='#d62728'
        ),
        anchor='x',
        overlaying='y',
        side='right'
    ),
    yaxis4=dict(
        title='yaxis5 title',
        titlefont=dict(
            color='#9467bd'
        ),
        tickfont=dict(
            color='#9467bd'
        ),
        anchor='free',
        overlaying='y',
        side='right',
        position=0.85
    )
)
fig = go.Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='pdeesawat69')