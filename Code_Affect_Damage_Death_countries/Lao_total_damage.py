"""Import Module Plotly To Ploting Graph"""
import plotly.plotly as py
import plotly.graph_objs as go

"""Open and Read CSV from database"""
data = open('Real_Final_database_02.csv')
alldata = data.readlines()
listdata = []
for i in alldata:
    listdata.append(i.strip().split(','))
type_z = ['Flood', 'Epidemic', 'Drought', 'Earthquake', 'Storm']
size_fill = [15,20,25,30,35]
fill_colors = ['#00d0f5', '#ff4a2e', 'a36800', '#ad9900', '#8b00db']
trace = []

"""Select and Set variable Data that happen in each disaster in Laos"""
for i in range(5):
    year_x = []
    damage_z = []
    types_y = []
    for j in listdata:
        if j[0] == 'Lao' and j[2] == type_z[i]:
            year_x.append(int(j[1]))
            damage_z.append(int(j[4]))
            types_y.append(type_z[i])
    trace.append(go.Bar(x = year_x, y = damage_z, name = type_z[i],
                        marker=dict(color = [fill_colors[i] for k in damage_z])))
                        
data = trace

"""Part of code that adjust layout of graph"""
layout = go.Layout(barmode = 'group', 
                   bargap = 0.15,
                   bargroupgap = 0.1,
                   title = 'Total Damage',
                   xaxis = dict(tickangle = -45,
                              tickfont = dict(size = 14, color = 'rgb(107, 107, 107)')),
                   yaxis = dict(title = 'Total Damage',
                                titlefont = dict(size = 16, color = '#d60081'),
                                tickfont = dict(size = 14, color = '#d60081')))
                                
"""Part of plot graph in plotly"""
fig = go.Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='Total_Damage_in_Laos')