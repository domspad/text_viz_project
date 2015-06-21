 
from datautils import load_book
import texttools as tt



# 
# TEST 1
# 

# title = 'Madame Bovary'

# text = load_book(title)

# print title

# print text[:1000]

# wc = tt.get_lengths(text, 'words','chars')
# wsy = tt.get_lengths(text, 'words','sylls')
# sw = tt.get_lengths(text, 'sents','words')
# sc = tt.get_lengths(text, 'sents','chars')
# ssy = tt.get_lengths(text, 'sents','sylls')
# bc = tt.get_lengths(text, 'book','chars')
# bsy = tt.get_lengths(text, 'book','sylls')
# bw = tt.get_lengths(text, 'book','words')
# bs = tt.get_lengths(text, 'book','sents')


# 
# TEST 2
# 

# for plotting....
# http://bokeh.pydata.org/en/latest/docs/gallery/violin.html
# 

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from bokeh import mpl
from bokeh.plotting import show

# for the hover tool
# from collections import OrderedDict
# from bokeh.models import HoverTool


# get book data
titles = ['Madame Bovary',
			'1984',
			'Animal farm',
			'Catch 22',
			'Grapes of Wrath',
			'Brave New World',
			'Catcher in the Rye',
			'Harry Potter and the Sorcerers Stone',
			'Macbeth',
			# 'Julius Caeser',  UnicodeDecodeError: 'utf8' codec can't decode byte 0xe6 in position 3843: invalid continuation byte
			'Metamorphosis',
			'The Adventures of Huckleberry Finn',
			'To Kill a Mockingbird',
			'The Crucible',
			'Frankenstein',
			'Heart of Darkness',
			'The Odyssey']

for title in titles :
	text = load_book(title)
	data.append(tt.get_lengths(text,'sents','words'))
data = np.array(data)

# And then just call the violinplot from Seaborn
sns.violinplot(data, color="Set3", names=titles)

plt.title("Seaborn violin plot in bokeh.")

# show(mpl.to_bokeh(name="violin"))