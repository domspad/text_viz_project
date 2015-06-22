import sys
sys.path.append('/Users/dominicspadacene/Desktop/school_books/text_viz_project/')
from datautils import load_book
import texttools as tt


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from bokeh import mpl
from bokeh.plotting import show
import pandas as pd

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


title = titles[1]
text = load_book(title)
print title
print tt.flesch_reading_ease(text)

title = titles[-1]
text = load_book(title)
print title
print tt.flesch_reading_ease(text)

title = titles[-3]
text = load_book(title)
print title
print tt.flesch_reading_ease(text) 

title = titles[-7]
text = load_book(title)
print title
print tt.flesch_reading_ease(text)

# 
# Looking for errors in count of sentences and words
# 

# probably counting stuff that's not words or sentences
# 
# sort the segmented text by char length and look at both ends
# 
# 
# 
# 

title = titles[0]
print title
text = load_book(title)
print tt.flesch_reading_ease(text)

sents = sorted(tt.segment(text,'sents'),key=len)
words = sorted(tt.segment(text,'words'),key=len)

# http://countwordsworth.com/statistics/alldata
webwords = 118667        
websents = 118667/21.24  #5586
websylls = 118667 * 1.49  #176813

# actually breaks up the sents and words fine..
# probably just becase 'Papa! Papa!' is counted as 2 sents, but, they are!
# 
for sent in sents[:10] :
	print sent
for word in words[:10] :
	print word

excerpt = text[464701:465300]
print excerpt
for sent in tt.segment(excerpt,'sents') :
	print sent
	print '\n'
for word in tt.segment(excerpt,'words') :
	print word



KNOWN examples
# 
text = "Even though John is not normally given to a display of his deeper emotions, he allegedly has developed a profound affection for Mary, as compared to the more equable feelings he seems to have for Lucy, Fran and, to a lesser extent, Sue."

print text
print tt.flesch_reading_ease(text)

text = "John has a profound affection for Mary."
print text
print tt.flesch_reading_ease(text)

text = "John loves Mary."
print text
print tt.flesch_reading_ease(text)


