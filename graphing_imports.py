# Necessary Imports
import re
import pandas as pd

get_ipython().magic(u'matplotlib inline')
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from decimal import Decimal
import plotly.plotly as py
import plotly
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go
from plotly import tools
import plotly.offline as offline
import plotly.graph_objs as go
offline.init_notebook_mode()

from IPython.display import Image

def toCSVLine(data):
    return ','.join(str(d) for d in data)

plotly.tools.set_credentials_file(username='skylarnam', api_key='ojmEG8EAPWrBZR2hT6n1')
filename = "/Users/Sulim/Desktop/CSE427S/"
labels = ['lat', 'long', 'name_of_page']

