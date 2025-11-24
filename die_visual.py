from die import Die
import plotly.express as px

die = Die()
die2 = Die()

results = []
count = [0,0,0,0,0,0]

for i in range(10000):
    roll_1 = die.roll()
    roll_2 = die2.roll()
    results.append((roll_1, roll_2))
    count[roll_1 -1] += 1
    count[roll_2 - 1] += 1

print(f'1: {count[0]}\n2: {count[1]}\n3: {count[2]}\n4: {count[3]}\n5: {count[4]}\n6: {count[5]}')

# Visualise the results
title = 'Roll of a dice'
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=range(1,7), y=count, title=title, labels=labels)
fig.show()