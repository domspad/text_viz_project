"""
This script will output

	med_word_length_syll	med_sent_length_word	med_word_length_char
	9	3	23
	3	5	52
	3	2 	52
	.. 	.. 	..


FOR ALL TEXTS EXCEPT JULUIS CAESAR AND ROMEO AND JULIET

to be copied over to the data file
"""
import sys
sys.path.append('/Users/dominicspadacene/Desktop/school_books/text_viz_project/')
from datautils import load_book
import texttools as tt

import pandas as pd

import numpy as np


# read in current data file
data_file = '../text_data.txt'
with open(data_file,'r') as f :
	df = pd.read_csv(f, sep='\t')

df = df[df.text == 1]
# sort by title
df.sort(['Title'], ascending=False, inplace=True)


# for each title, compute cols and print out 
results = []
for title in df.Title.values :
	text = load_book(title)
	ws = tt.get_lengths(text,'words','sylls')
	wc = tt.get_lengths(text,'words','chars')
	sw = tt.get_lengths(text,'sents','words')
	results.append("\t".join(map(lambda x : str(np.median(x)), [ws,sw,wc])))

print '\n'.join(df.Title.values)
print '\n'.join(results)

# EXTRA FUN WITH ANALYSIS
for title in df.Title.values : 
	text = load_book(title)
	words = tt.segment(text,'words')
	words.sort(key=len)
	print title
	print '\tLongest words (chars)'
	print '\t' + '\n\t'.join(words[-5:])
	print '\n'
	print '\tLongest words (syls)'
	words.sort(key=tt.sylco_com)
	print '\t' + '\n\t'.join(words[-5:])