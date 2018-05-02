#Visualization for DBPedia

from graphing_imports import *

# Parsing
words = []

# Change the filepath if someone else is going to use it
with open(filename + "lat_longs") as f:
    for line in f:
        words.append([n for n in line.strip().split(' ')])
        
df = pd.DataFrame.from_records(words, columns=labels)

df['name_of_page'] = df['name_of_page'].str.replace('<http://dbpedia.org/resource/|>', "")
df.head()

# Graphing
data = [ dict(
    type = 'scattergeo',
    lon = df['long'],
    lat = df['lat'],
    text = df['name_of_page'],
    marker = dict(
        size = 2,
        opacity = 0.8,
        color = '#CF1020',
        colorscale = 'Viridis'
        ),
    name='Locations'
) ]

layout = dict(
    title = 'Data of All the Locations Found On <a href="http://wiki.dbpedia.org/">DBPedia</a>',
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
# if you want to just see the plot, uncomment and run this.
# however, it doesn't save the image file.
# offline.plot(fig)
# if you want to see the plot AND save the image file,
# run this.
offline.plot(fig, image='png', filename='step3_image')

