
import codecs
from unidecode import unidecode #(DOES THE SAME UNIDECODING AS UNIREPLACE)


UNIREPLACE = {u'\u2026' : u'...',
			u'\u2013' : u'-',
			u'\u2014' : u'-',
			u'\u2019' : u'\'',
			u'\u2018' : u'\'', 
			u'\u201d' : u'"',
			u'\u201c' : u'"'}

def _filename(title) :
	"""
	computes filename given a book's title

		"The Adventure's of Huckleberry Finn" --->

		the_adventures_of_huckleberry_finn.txt

	"""
	newtitle = ''
	for char in title.lower() :
		if char.isalnum() :
			newtitle += char
		elif char == ' ' : 
			newtitle += '_'
	return newtitle + '.txt'



def _replace_uni(text) : 
	"""
	returns text with unicode chars replaced by string counterparts (UNIREPLACE mapping)
	"""
	for orig,new in UNIREPLACE.iteritems() :
		print (u'replacing {} with {}'.format(orig,new))
		text = text.replace(orig,new)
	return text

def _get_unique_non_ascii(text) :
	"""
	returns set of all non-ascii unicode chars in text
	"""
	import unicodedata
	nonascii = set([c for c in text if ord(c) >= 128])
	for c in nonascii :
		print (c, '\t', hex(ord(c)),'\t', unicodedata.name(c))
	return nonascii 


def load_book(title) :
	"""
	returns utf-8 encoded book text

		"The Adventure's of Huckleberry Finn" --> text
	"""
	fname = _filename(title)
	full_path = '/Users/dominicspadacene/Desktop/school_books/text_viz_project/texts/' + fname
	with codecs.open(full_path,encoding='utf-8') as f :
		text = f.read()
	
	print('replacing strange non-ascii chars...')
	replaced_text = unidecode(text)
	# replaced_text = _replace_uni(text)
	# check
	nonascii = _get_unique_non_ascii(replaced_text)
	if len(nonascii) == 0 :
		print ('ALL UNICODE REPLACED')
	else :
		print ('Still some unicode chars not cleaned...', nonascii)
	return replaced_text
