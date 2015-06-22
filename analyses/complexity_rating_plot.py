import sys
sys.path.append('/Users/dominicspadacene/Desktop/school_books/text_viz_project/')
from datautils import load_book
import texttools as tt

import pandas as pd

import numpy as np
import bokeh.plotting as bp
from bokeh.models import HoverTool 


# put data in read-in format
data_file = '../text_data.txt'


# read in data as dataframe
with open(data_file,'r') as f :
	df = pd.read_csv(f, sep='\t')

df_texts = df[df.text == 1]
# append col for complexity
newcol =[]
for title in df_texts.Title : 
	text = load_book(title)
	newcol.append(tt.flesch_reading_ease(text))

df_texts['flesch'] = newcol

# plot complexity vs rating with num_rating as size

import numpy as np
import bokeh.plotting as bp
from bokeh.models import HoverTool, ColumnDataSource, BoxZoomTool, ResetTool, ResizeTool, PanTool, WheelZoomTool
bp.output_file('complexity_rating.html')

x = df_texts.flesch.values
y = df_texts.Goodreads_rating.values
size = df_texts.Goodreads_num.values / 30000
titles = df_texts.Title.values

source = ColumnDataSource(
    data=dict(
        x=x,
        y=y,
        size=size,
        titles=titles
    )
)

hover = HoverTool(
    tooltips = [
        ("x", "@x"),
        ("y", "@y"),
        ("size", "@size"),
        ("titles","@titles")
    ]
)

tools = [hover, BoxZoomTool(), ResetTool(),ResizeTool(),PanTool(), WheelZoomTool()]

fig = bp.figure(tools=tools,title='Complexity Vs Rating')

s = fig.scatter('x','y',size='size',source=source)
# s.select(dict(type=HoverTool)).tooltips = {"x":"$x", 
# 											"y":"$y", 
# 											"size":"$size"}
bp.show(fig)