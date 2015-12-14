"""Import Module Plotly To Ploting Graph"""
import plotly.plotly as py
import plotly.graph_objs as go

"""Get data"""
data = open('Real_Final_database_02.csv')
alldata = data.readlines()
listdata = []
for i in alldata:
    listdata.append(i.strip().split(','))
    
"""Create trace"""
type_z = ['Flood', 'Epidemic', 'Drought', 'Earthquake', 'Storm']
fill_colors = ['66FF33', 'FF66CC', '33FFCC', 'FF6600', 'FFFF00']
trace_list = ['trace1', 'trace2', 'trace3', 'trace4', 'trace5']
num = 0
last = []
wide = 0.5
opac = 0.8

for i in range(5):
    year_x = []
    affected_z = []
    types_y = []
    for j in listdata:
        if j[0] == 'Vietnam' and j[2] == type_z[i]:
            year_x.append(int(j[1]))
            affected_z.append(int(j[3]))
            types_y.append(type_z[i])
    if year_x != []:
        trace_list[i] = go.Scatter3d(x = year_x, y = types_y, z = affected_z,
        mode = 'markers', marker = dict(size = 12, line = dict(color = fill_colors[i], width = wide),
        opacity = opac))
        last.append(dict(trace_list[num]))
        wide += 0.5
        opac += 0.1

"""Style Layout"""
layout = dict(
    title = 'Total Affected',
    scene = dict(xaxis = dict(title = 'Year'), yaxis = dict(title = 'Types of Disaster'), zaxis = dict(title = 'Total Affected')))
    
fig = go.Figure(data = last, layout = layout)
plot_url = py.plot(fig, filename = 'Total Affected in Vietnam')