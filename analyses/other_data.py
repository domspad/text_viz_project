import sys
sys.path.append('/Users/dominicspadacene/Desktop/school_books/text_viz_project/')
from datautils import load_book
import texttools as tt

import pandas as pd

import numpy as np
import bokeh.plotting as bp
from bokeh.models import HoverTool 

data_file = '../other_data.txt'

with open(data_file,'r') as f :
	df = pd.read_csv(f, sep='\t')

import numpy as np
import bokeh.plotting as bp
from bokeh.models import HoverTool, ColumnDataSource, BoxZoomTool, ResetTool, ResizeTool, PanTool, WheelZoomTool
bp.output_file('other_data.html')



x = df['Flesch Reading Ease'].values
y = df['Words'].values
size = df['Words Per Sentence'].values
titles = df['Book Name'].values


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

fig = bp.figure(tools=tools,title='Complexity Vs Length')

s = fig.scatter('x','y',size='size',source=source)
# s.select(dict(type=HoverTool)).tooltips = {"x":"$x", 
# 											"y":"$y", 
# 											"size":"$size"}
bp.show(fig)