notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

def print_string(note):
	test = notes.index(note)

	print('[', end='')
	for i in range(len(notes) + 1):
		print(notes[(i + test) % (len(notes))], end='')
		if i != len(notes):
			print('-', end='')
	print(']')

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