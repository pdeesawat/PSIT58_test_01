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
    if j[0] == 'Myanmar' and j[2] == 'Flood':
        year.append(int(j[1]))
        affect.append(int(j[3]))
        damage.append(int(j[4]))
        death.append(int(j[5]))

# Create and style traces
trace0 = go.Scatter(
    x=year,
    y=affect,
    mode='markers',
    name='Total Affected',
    marker=dict(
        symbol='circle',
        sizemode='diameter',
        sizeref=0.85,
        size=[29.810746602820924, 18.197149567147044, 14.675557544415877,
              6.610603004351287, 19.543385335458176, 14.956442130894114,
              21.72077890062975, 10.792626698654045, 16.52185943835442,
              4.353683242838546, 41.50240100063496, 10.066092062338873,
              21.91453196050797, 3.6377994860079204, 46.258986486204044,
              3.8334450569607683, 11.437310410545528, 45.16465542353964,
              6.227961099314154, 6.709136738617642, 24.694430700391482,
              16.285386604676816, 6.264612285824508, 30.812100863425822,
              7.325179403286266, 9.227791164226492, 12.68649752933601,
              22.60573984618565, 18.849582296257626, 17.910159625556144,
              9.337109185582111, 5.774872714286052, 29.999726284159046,
              23.063420581238734, 7.40199199438875, 18.54140518159347, 60,
              4.612764339536968, 15.369704446995708, 2.3067029222366395,
              18.084735199216812, 12.79910818701753, 15.592022291528775,
              34.24915519732991, 33.57902844158756, 5.496191404660524,
              31.887651824471956, 12.329112567064463, 16.55196774082315,
              27.887232791984047, 17.696194784090615, 18.11688103909921],
        line=dict(
            width=2
        ),
    )
)
trace1 = go.Scatter(
    x=year,
    y=damage,
    mode='markers',
    name='Total Damage \'000 US',
    marker=dict(
        sizemode='diameter',
        sizeref=0.85,
        size=[21.94976988499517, 10.441052822396196, 47.66021903725089,
              19.979112486875845, 13.95267548575408, 22.993945975228556,
              7.029852430522167, 11.682689085146487, 10.555193870118702,
              12.823544926991564, 9.108293955789053, 12.259853478972317,
              10.082039742103595, 9.458604761285072, 5.765006135966166,
              36.048202790993614, 8.23689670992972, 6.22565654446431,
              8.927648460491556, 18.514711052673302, 6.865187781408511,
              3.5540539239313094, 60, 6.41976234423909, 17.658738378883186],
        line=dict(
            width=2
        ),
    )
)
trace2 = go.Scatter(
    x=year,
    y=death,
    mode='markers',
    name='Total Death',
    marker=dict(
        sizemode='diameter',
        sizeref=0.85,
        size=[9.330561207739747, 1.390827697025556, 20.266312242166443,
              6.211273648937339, 60, 4.3653750211924, 55.05795036085951,
              24.703896200017994, 13.769821732555231, 8.664520214956125,
              4.188652530719761, 18.654412200415056, 4.0651192623762835,
              7.975814912067495, 11.57117523159306, 3.271861016562374,
              8.231768913808876, 2.8011347940934943, 11.418845373343052,
              8.882667412223675, 2.9579312056937046, 21.49670117903256,
              15.768343552577761, 8.680479951148044, 3.525577657243318,
              7.4587209016354095, 7.261486641287726, 7.95397619750268,
              13.3280083790662, 15.256667990032932, 3.312103798885452,
              7.787039017632765],
        line=dict(
            width=2
        ),
    )
)
data = [trace0, trace1, trace2]
layout = go.Layout(
    title='Flood in Myanmar',
    xaxis=dict(
        title='Years'),
    yaxis=dict(
        title='Total affected',
        titlefont=dict(
            color='3333FF'
        ),
        tickfont=dict(
            color='3333FF'
        )
    ),
    yaxis2=dict(
        title='Total Damage \'000 US',
        titlefont=dict(
            color='FF6633'
        ),
        tickfont=dict(
            color='FF6633'
        ),
        anchor='free',
        overlaying='y',
        side='left',
        position=0.15
    ),
    yaxis3=dict(
        title='Total Death',
        titlefont=dict(
            color='33CC33'
        ),
        tickfont=dict(
            color='33CC33'
        ),
        anchor='x',
        overlaying='y',
        side='right'
    ),
##        title='Life Expectancy (years)'),
##        gridcolor='rgb(255, 255, 255)',
##        #range=[36.12621671352166, 91.72921793264332],
##        zerolinewidth=1,
##        ticklen=5,
##        gridwidth=2,
    #),
    paper_bgcolor='rgb(243, 243, 243)',
    plot_bgcolor='rgb(243, 243, 243)'
)
fig = go.Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='bennyy')
##    yaxis2=dict(
##        title='Total Damage \'000 US',
##        titlefont=dict(
##            color='3399FF'
##        ),
##        tickfont=dict(
##            color='3399FF'
##        ),
##        anchor='free',
##        overlaying='y',
##        side='left',
##        position=0.15
##    ),
##    yaxis3=dict(
##        title='Total Death',
##        titlefont=dict(
##            color='FF3300'
##        ),
##        tickfont=dict(
##            color='FF3300'
##        ),
##        anchor='x',
##        overlaying='y',
##        side='right'
##    )
##)
##fig = go.Figure(data=data, layout=layout)
##plot_url = py.plot(fig, filename='bennyy')
