#Visualization for Synthetic

from graphing_imports import *

words = []
labels = ['lat', 'long', 'locationID']

with open(filename + "sample_geo.txt") as f:
    for line in f:
        words.append([n for n in line.strip().split('\t')])
        
df = pd.DataFrame.from_records(words[1:], columns=labels)

data = [ dict(
    type = 'scattergeo',
    lon = df['long'],
    lat = df['lat'],
    text = df['locationID'],
    marker = dict(
        size = 2,
        opacity = 0.8,
        color = '#CF1020',
        colorscale = 'Viridis'
        ),
    name='Locations'
) ]

layout = dict(
    title = 'Synthetic Cluster Locations Data',
    geo = dict(
        showframe = False,
        projection = dict(
            type = 'Mercator'
        ),
        showland = True,
        showcoastlines=False,
        landcolor = 'rgb(234, 234, 234)'
    ),
    showlegend=True
)

fig = dict( data=data, layout=layout )
offline.plot(fig)
#offline.plot(fig, image='png', filename='step3_image')


