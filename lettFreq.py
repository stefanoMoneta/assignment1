import time
import os
import argparse
import matplotlib.pyplot as plt
import logging
logging.basicConfig(level=logging.INFO)

_description = 'Print the relative frequence of each letter of the alphabet from a book.'


def process(file_path):
	"""Main processing routine.
	"""
	
	start_time = time.time()
	
	# Basic sanity checks.
	assert file_path.endswith('.txt')
	assert os.path.isfile(file_path)
	
	# Good to go---open the input file.
	logging.info('Opening file %s...', file_path)
	with open(file_path) as input_file:
		data = input_file.read()
	logging.info('Done. %d character(s) found.', len(data))
	
	letters = 'abcdefghijklmnopqrstuvwxyz'
	frequency_dict = {}
	for ch in letters:
		frequency_dict[ch] = 0
		
	# Loop over the actual data.
	logging.info('Looping over the input text')
	for ch in data.lower():
		if ch in letters:
			frequency_dict[ch] += 1
	"""
		try:
			frequency_dict[ch] += 1
		except KeyError:
			pass
	"""
	
	num_characters = float(sum(frequency_dict.values()))
	
	# Normalize the occurrences.
	for ch in letters:
		frequency_dict[ch] = frequency_dict[ch] / num_characters
	
	# Print stuff.
	print(frequency_dict)
	
	# Insert data in a bar plot.
	plt.bar(range(len(frequency_dict)), list(frequency_dict.values()), align='center')
	plt.xticks(range(len(frequency_dict)), list(frequency_dict.keys()))
	
	plt.ylabel('Letter frequency [%]')
	plt.title('Distribution of letter frequency')
	
	plt.show()
	
	elapsed_time = time.time() - start_time
	
	logging.info('Total elapsed time: %s s', elapsed_time)



if __name__ == '__main__':
	parser = argparse.ArgumentParser(description=_description)
	parser.add_argument('infile', help='path to the input text file')
	args = parser.parse_args()
	process(args.infile)
