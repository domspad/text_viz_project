"""
Tools and utility functions for working with text
"""

from __future__ import print_function, division
import nltk
from nltk import word_tokenize #, pos_tag
import nltk.data
import string
from syllablecount import sylco, sylco_com
from time import time
import numpy as np

SENTENCIZER = nltk.data.load('tokenizers/punkt/english.pickle')


def segment(text,unit) :
	"""
	returns the text broken up and filtered according to the unit

		'sents','words','sylls' (later add paragraphs)

		e.g. 'The quick brown fox runs. The turtle doesn\'t.', 'words'

			('The', 'quick', 'brown', 'fox','runs', 'The', 'turtle','doesn\'t')
	"""

	# if unit == 'paragraphs' :
	# 	'\n\s'
	if unit == 'sents' :
		return SENTENCIZER.tokenize(text)

	elif unit == 'words' :
		return [word.strip(string.punctuation) for word in text.split()]

	elif unit == 'sylls' :
		print('not implemented yet')
		return None
	elif unit == 'book' :
		return [text]

	else :
		print("not valid input for unit")
		return None



def get_lengths(text, unit='words', count_unit='chars') :
	"""
	returns the lengths of ___

			words (in chars or sylls)
			sents	(in chars or words)
			paragraphs (in sents, words, or chars)
			book 	(in sents, words, sylls or chars)
	"""
	print ("getting lengths of {} in terms of {}".format(unit,count_unit))
	t0 = time()
	# break up into units
	tokens = segment(text,unit)

	# break units up into count units
	counts = []
	for token in tokens :
		
		# breaking up token into chars would be waste
		if count_unit == 'chars' :
			counts.append(len(token))
		# breaking up into sylls actually quite difficult...
			# instead trying to just call count_syl on each word
		elif count_unit == 'sylls' : 
			# breaking each token into words if necessary
			# counting syllables
			if unit != 'words' :
				subtokens = segment(token,'words')
				sylcount = reduce(lambda agg,word : agg + sylco_com(word), subtokens, 0)
			else :
				sylcount = sylco_com(token)

			# appending value
			counts.append(sylcount)

		else : 
			subtokens = segment(token, count_unit)
			counts.append(len(subtokens))			

	print ("finished in {} secs".format(str(round(time()-t0,1))))
	# return count
	return np.array(counts)

def get_unique_words(text) :
	"""
	returns the set of unique words in the text (modulo case)
	"""
	pass

def unique_word_density(text) :
	"""
	returns the density of unique words in the text 

			# unique words
			--------------
			# words
	"""
	pass

def pos_counts(text) :
	"""
	returns counts of each part of speech tag
	"""
	pass

def flesch_reading_ease(text) :
	"""
	see https://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests
	"""

	sylls = get_lengths(text,'book','sylls')
	words = get_lengths(text,'book','words')
	sents = get_lengths(text,'book','sents')
	print ("words / sent {}\nsylls / word {}".format(words/sents, sylls/words))
	print("sylls {}\n words {}\n sents {}".format(sylls, words, sents))
	return (206.835 - 1.015 * (words / sents) - 84.6 * (sylls / words))[0]
