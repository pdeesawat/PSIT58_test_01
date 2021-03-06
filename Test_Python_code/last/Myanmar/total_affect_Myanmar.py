import plotly.plotly as py
import plotly.graph_objs as go

data = open('Real_Final_database_02.csv')
alldata = data.readlines()
listdata = []
for i in alldata:
    listdata.append(i.strip().split(','))
type_z = ['Flood', 'Epidemic', 'Drought', 'Earthquake', 'Storm']
size = [22, 19, 10, 7, 5]
fill_colors = ['#00d0f5', '#ff4a2e', 'a36800', '#ad9900', '#8b00db']
trace = []

for i in range(5):
    year_x = []
    affected_z = []
    types_y = []
    for j in listdata:
        if j[0] == 'Myanmar' and j[2] == type_z[i]:
            year_x.append(int(j[1]))
            affected_z.append(int(j[3]))
            types_y.append(type_z[i])
    trace.append(go.Scatter(
    x=year_x,
    y=affected_z,
    name=type_z[i],
    line = dict(color = fill_colors[i], width = 2),
    marker=dict(symbol='circle', sizemode='diameter', sizeref=0.85, size=size[i],
        line=dict(width=2), )))
    
data = trace
layout = go.Layout(
    title='Total Affect in Myanmar',
    yaxis=dict(title='Total Affected',
        titlefont=dict(color='#eb0056'),
        tickfont=dict(color='#eb0056')),
    
    paper_bgcolor='rgb(243, 243, 243)',
    plot_bgcolor='rgb(243, 243, 243)'
)
fig = go.Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='Total_Affected_in_Myanmar')
