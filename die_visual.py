from die import Die
import plotly.express as px

die = Die()
die2 = Die()

results = []
count = [0,0,0,0,0,0,0,0,0,0,0,0]

for i in range(100000):
    total = die.roll() + die2.roll()
    results.append(total)
    count[total -1] += 1

# Visualise the results
title = 'Roll of a dice'
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=range(1,13), y=count, title=title, labels=labels)

fig.update_layout(xaxis_dtick=1)
fig.show()