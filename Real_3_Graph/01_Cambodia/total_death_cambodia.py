import plotly.plotly as py
import plotly.graph_objs as go

data = open('Real_Final_database_02.csv')
alldata = data.readlines()
listdata = []
for i in alldata:
    listdata.append(i.strip().split(','))
type_z = ['Flood', 'Epidemic', 'Drought', 'Earthquake', 'Storm']
fill_colors = ['#00d0f5', '#ff4a2e', 'a36800', '#ad9900', '#8b00db']
trace = []
for i in range(5):
    year_x = []
    death_z = []
    types_y = []
    for j in listdata:
        if j[0] == 'Cambodia' and j[2] == type_z[i]:
            year_x.append(int(j[1]))
            death_z.append(int(j[5]))
            types_y.append(type_z[i])
    trace.append(go.Scatter(
    x=year_x,
    y=death_z,
    name=type_z[i],
    line = dict(
        color = fill_colors[i],
        width = 1.5),
        )
    )

data = trace
layout = go.Layout(
    title='Total Death In Cambodia',
    width=800,
    height=482,
    xaxis=dict(
        domain=[1, 0.7],
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
    autosize=True,
    plot_bgcolor=["rgba(0, 0, 0, 0)"],
    paper_bgcolor=["rgba(0, 0, 0, 0)"],
    )
fig = go.Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='Total_Death_in_Cambodian')