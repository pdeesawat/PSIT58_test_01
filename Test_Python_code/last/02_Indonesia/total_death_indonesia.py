import plotly.plotly as py
import plotly.graph_objs as go

data = open('Real_Final_database_02.csv')
alldata = data.readlines()
listdata = []
for i in alldata:
    listdata.append(i.strip().split(','))
type_z = ['Flood', 'Epidemic', 'Drought', 'Earthquake', 'Storm']
size_fill = [15,20,25,30,35]
fill_colors = ['#00d0f5', '#ff4a2e', 'a36800', '#ad9900', '#8b00db']
trace = []

for i in range(5):
    year_x = []
    death_z = []
    types_y = []
    for j in listdata:
        if j[0] == 'Indonesia' and j[2] == type_z[i]:
            year_x.append(int(j[1]))
            death_z.append(int(j[5]))
            types_y.append(type_z[i])
    trace.append(go.Scatter(
    x=year_x,
    y=death_z,
    name=type_z[i],
    mode='markers',
    marker=dict(
        color = [fill_colors[i] for k in death_z],
        size=[size_fill[i] for k in death_z]
            )
        )
    )
    
data = trace
layout = go.Layout(
    title='Total Death In Indonesia',
    showlegend=True,
    height=600,
    width=600,
    
    xaxis=dict(
        # set x-axis' labels direction at 45 degree angle
        tickangle=-45,
    ),
    
    yaxis=dict(
        title="Total Death",
        titlefont=dict(
            color='#ff2323'
        ),
        tickfont=dict(
            color='#ff2323'
        )
    ),
)
fig = go.Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='Total_Death_in_Indonesia')