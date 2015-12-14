"""Import Module Plotly To Ploting Graph"""
import plotly.plotly as py
import plotly.graph_objs as go

"""Get data"""
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
    affected_z = []
    types_y = []
    for j in listdata:
        if j[0] == 'Philippines' and j[2] == type_z[i]:
            year_x.append(int(j[1]))
            affected_z.append(int(j[3]))
            types_y.append(type_z[i])
    trace.append(go.Scatter(x = year_x, y = affected_z, name = type_z[i], line = dict(
        color = fill_colors[i], width = 1.5)))

data = trace

"""Style Layout"""
layout = go.Layout(title = 'Total Affected', width = 800, height = 536, xaxis = dict(
        domain = [1, 0.7], tickangle = -45), yaxis = dict(title = 'Total Affected', titlefont = dict(color = '#eb0056'),
        tickfont = dict(color = '#eb0056')), autosize = True, plot_bgcolor = ["rgb(245, 245, 245)"], paper_bgcolor = ["rgb(245, 245, 245)"])
        
fig = go.Figure(data = data, layout = layout)
plot_url = py.plot(fig, filename = 'Total_Affected_in_Philippines')