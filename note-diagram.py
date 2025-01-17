notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

def print_string(note):
	start = notes.index(note) # this is the section to fix, perhaps .find() will assist

	octaves = 2
	size = len(notes)

	# print('[', end='')
	for i in range(size * octaves + 1):
		if (i % size) == 0:
			print('[', end='')

		print(notes[(start + i) % size], end='')
		
		if (i % size) == 0:
			print(']', end='')
		
		if i >= 0 and i < (size * octaves):
			if len(notes[(start + i) % size]) == 1:
				print('---', end='')
			else:
				print('--', end='')
	print()

def print_instrument(instrument):
	print(f'{str(instrument['key'])} Note Chart\n')

	for i in reversed(instrument['strings']):
		print_string(i)
	print()

def print_instruments(instruments):
	for i in instruments:
		print_instrument(i)

instruments = [{ 'key': 'Guitar',   'strings': ['E', 'A', 'D', 'G', 'B', 'E']},
			   { 'key': 'Ukelele',  'strings': ['G', 'C', 'E', 'A']},
 			   { 'key': 'Violin',   'strings': ['G', 'D', 'A', 'E']},
 			   { 'key': 'Bouzouki', 'strings': ['C', 'F', 'A', 'D']}]

print_instruments(instruments)