from graphing_imports import *

words = []
labels = ['lat', 'long', 'locationID']
colors = ['red','yellow','blue','green']

df = pd.DataFrame()

def create_column(row):
    if row['time'] == 'morning':
        val = 0
    elif row['time'] == 'afternoon':
        val = 1
    elif row['time'] == 'evening':
        val = 2
    else:
        val = 3
    return val

for x in range(0, 12):
    new_filename = filename + "Pokemon_rare/"
    add_on = "part-0000" + str(x) if x < 10 else "part-000" + str(x)
    new_filename = new_filename + add_on + ".csv"

    df_temp = pd.read_csv(new_filename, sep=",", header=None)

    df = df.append(df_temp, ignore_index=True)

cols = [2,4,5,6,7]
df.drop(df.columns[cols],axis=1,inplace=True)

df.rename(columns={
    0: 'latitude',
    1: 'longitude',
    3: 'time'}, inplace=True)

print df.head()

df['time_num'] = df.apply(create_column, axis=1)

print df.head()

data = []

dict_ = dict(
    type = 'scattergeo',
    lon = df['longitude'],
    lat = df['latitude'],
    text = df['time'],
    marker = dict(
        size = 4,
        opacity = 0.5,
        color = df['time_num'],
        colorscale = 'Rainbow'
        ),
    name='Locations'
)

data.append(dict_)

layout = dict(
    title = 'Rare Pokemons in the World',
    geo = dict(
        showframe = False,
        projection = dict(
            type = 'Mercator'
        ),
        showland = True,
        showcoastlines=False,
        landcolor = 'rgb(239, 239, 239)',
        subunitcolor = "rgb(217, 217, 217)",
        countrycolor = "rgb(217, 217, 217)",
        countrywidth = 0.5,
        subunitwidth = 0.5
    ),
    showlegend=True
)

fig = dict( data=data, layout=layout )
offline.plot(fig)
#offline.plot(fig, image='png', filename='step3_image')
