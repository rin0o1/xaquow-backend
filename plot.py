# These steps will be running every day when the weather is available
#  1- Get current soil moinsture from Basilea target file (this in practice should come from the API, but for now lets simulate using real data from csv)
#  2- Run the ML algorithm to get the NDSM 
#  3- Show the optimized SMTS
#  4- Show DSMI point where the irrigation should stop
#  5- Show performance of simulations using different tresholds as well different irrigation TYPE=0(default) and TYPE=1(DSMI)

# Use plotly as plot library so that it can be plugged into XaquoWeb
import plotly.graph_objects as go
import plotly.utils
import json

y_scale = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]

# Generate these values via machine learning 
y = [22, 13, 25, 22, 23, 24, 22]
x = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']
labels = ['Mo (R)', 'Real-time SM', 'We (Estimated)', 'Th (Estimated)', 'Fr (Estimated)', 'Sa (Estimated)', 'Su (Estimated)']
colours = ['#23C88E', '#C767FF', '#86D1FF', '#86D1FF', '#86D1FF', '#86D1FF', '#86D1FF']

# Run this optimisation algorithm
SMTS = [17, 26, 27, 32]

fig = go.Figure()

# Create the main scatter plot for the existing data
for i in range(len(x)):
    label = labels[i]  
    colour = colours[i]
    fig.add_trace(go.Scatter(x=[x[i]], y=[y[i]], mode='markers', marker=dict(size=15, color=colour), name=label))


# Draw an orange line at y=15
fig.add_shape(
    type='line',
    x0=0,
    x1=len(x) - 1,
    y0=SMTS[0],
    y1=SMTS[0],
    line=dict(color='orange', width=1, dash='dash')
)

fig.add_annotation(
    text='Xaquo optimised soil moisture target',
    xref='paper',
    yref='y',
    x=1.09,
    y=SMTS[0] + 0.15,
    showarrow=False,
    font=dict(color='orange')
)


# Add a new marker for Wednesday with a different shape
fig.add_trace(go.Scatter(x=['Tu'], y=[13 + (30 - 25)], mode='markers', marker=dict(size=15, color='red', symbol='x'), name='Xaquo DSMI break-point'))
fig.add_trace(go.Scatter(x=['Tu'], y=[30], mode='markers', marker=dict(size=15, color='gray', symbol='x'), name='Traditional break-point'))

# Draw an orange line at y=30
fig.add_shape(
    type='line',
    x0=0,
    x1=len(x) - 1,
    y0=30,
    y1=30,
    line=dict(color='orange', width=1, dash='dash')
)
fig.add_annotation(
    text='Field Capacity (%)',
    xref='paper',
    yref='y',
    x=1.02,
    y=30 + 0.15,
    showarrow=False,
    font=dict(color='orange')
)

# Set the background color to black and reduce grid line opacity
fig.update_layout(
    plot_bgcolor='#181818',
    paper_bgcolor='#181818',
    xaxis=dict(showgrid=True, gridcolor='rgba(255, 255, 255, 0.1)'),
    yaxis=dict(showgrid=True, gridcolor='rgba(255, 255, 255, 0.1)'),        
)

# Set the axis labels and title
fig.update_xaxes(title_text="Week 2023-09-15", showgrid=False, tickfont_color='white', linecolor='white', title_font=dict(color='white'))
fig.update_yaxes(title_text="Soil Moisture (% TAW)", showgrid=False, tickfont_color='white', linecolor='white', title_font=dict(color='white'))

fig.show()

fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

# Save the JSON string to a file
with open('plotly_chart.json', 'w') as json_file:
    json_file.write(fig_json)
