#Visualization for K-Means

from graphing_imports import *

# Automated script to draw the points.
# You might want to change the commented "textposition"
# to make the Cluster text more visible.
# Make sure all the folders (e.g. dbpedia_eu_6, synthetic_eu_2)
# are within the same folder.

# Necessary Imports
import time
import plotly.graph_objs as go

filenames = ['dbpedia_eu_6','dbpedia_gc_6','synthetic_eu_4','synthetic_gc_4','synthetic_eu_2','synthetic_gc_2','device_eu_5']
colors = ['rgb(234, 234, 234)', 'rgb(26, 94, 204)', 'rgb(81, 24, 165)', 'rgb(216, 145, 30)',
         'rgb(24, 155, 51)', 'rgb(7, 170, 188)']

# Change the filepath if someone else is going to use it
for fn in filenames:
    cluster_no = fn[-1] # getting the k (k=6,2,4...)
    print "File %s, cluster no. %s" % (fn, cluster_no)
    
    # part-r-00000
    part = filename + fn + "/part-00000"
    try:
        df_part = pd.read_csv(part, sep=",", header=None)
    except:
        df_part = pd.read_csv(part + ".csv", sep=",", header=None)

    df_part.rename(columns={
        0: 'cluster',
        1: 'latitude',
        2: 'longitude'}, inplace=True)

    # if you want to test, run this to get a smaller sample
    df_part = df_part.sample(n=1000)

    data2 = []
    
    if "dbpedia" in fn:
        dict_1 = dict(
            type = 'scattergeo',
            lon = df_part['longitude'],
            lat = df_part['latitude'],
            text = df_part['cluster'],
            marker = dict(
                size = 2,
                opacity = 0.5,
                color = df_part['cluster'],
                colorscale = 'Viridis'
                ),
            name='Locations'
        )
    else:
        dict_1 = dict(
            type = 'scattergeo',
            lon = df_part['longitude'],
            lat = df_part['latitude'],
            text = df_part['cluster'],
            marker = dict(
                size = 3,
                opacity = 0.5,
                color = df_part['cluster'],
                colorscale = 'Viridis'
                ),
            name='Locations'
        )
    data2.append(dict_1)
    
    # centroids
    centroids = filename + fn + "/centroids.txt"
    df_cent = pd.read_csv(centroids, sep=",", header=None)
    df_cent.rename(columns={
        0: 'cluster',
        1: 'latitude',
        2: 'longitude'}, inplace=True)

    dict_2 = dict (
        type = 'scattergeo',
        lat=df_cent['latitude'],
        lon=df_cent['longitude'],
        marker = dict(
            size = 13,
            opacity = 1,
            color = df_cent['cluster'],
            colorscale = 'Viridis',
            line = dict(width=3, color='white'),
            symbol = "diamond"
            ),
        mode="markers+text",
        text=[],
        textfont={
            "color": 'black',
            "size": 15
        },
        textposition=[]
)
    
    if fn == 'dbpedia_eu_6' or fn == 'dbpedia_gc_6':
        positions = ['bottom center','right center','bottom left','top center','bottom right','bottom center']
    elif fn == 'synthetic_eu_4' or fn == 'synthetic_gc_4':
        positions = ['top center','left center','bottom right','top center']
    elif fn == 'synthetic_eu_2' or fn == 'synthetic_gc_2':
        positions = ['top center','top center']
    else: # device
        positions = ['top center','bottom left','right center','bottom right','top right']
    
    dict_2['textposition'] = positions
        
    for x in range(0, int(cluster_no)):
        dict_2['text'].append("Cluster" + str(x))

    data2.append(dict_2)
    
    if "dbpedia" in fn:
        layout = dict(
            title = '',
            showlegend=False,
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
            )
        )
    else:
        layout = dict(
            title = '',
            showlegend=False,
            geo = dict(
                scope='usa',
                projection=dict( type='albers usa' ),
                showland = True,
                landcolor = "rgb(250, 250, 250)",
                subunitcolor = "rgb(217, 217, 217)",
                countrycolor = "rgb(217, 217, 217)",
                countrywidth = 0.5,
                subunitwidth = 0.5
            ),
        )

    source = ""
    measure = ""
    
    if "dbpedia" in fn and "eu" in fn:
        source = "DBPedia"
        measure = "Euclidean Distance"
    elif "dbpedia" in fn and "gc" in fn:
        source = "DBPedia"
        measure = "Great Circle Distance"
    elif "synthetic" in fn and "eu" in fn:
        source = "Synthetic"
        measure = "Euclidean Distance"
    elif "synthetic" in fn and "gc" in fn:
        source = "Synthetic"
        measure = "Great Circle Distance"
    elif "device" in fn and "eu" in fn:
        source = "Device"
        measure = "Euclidean Distance"
    else:
        source = "Device"
        measure = "Great Circle Distance"
    
    layout['title'] = 'K-Means with k=%s, %s<br>%s' % (cluster_no, source, measure)

    fig2 = dict( data=data2, layout=layout )
    offline.plot(fig2)
    #offline.plot(fig2, image='png', filename='step3_image')

    time.sleep(3)

