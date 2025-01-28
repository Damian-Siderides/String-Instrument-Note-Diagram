notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

def print_string(note, octaves):
	start = notes.index(note)

	size = len(notes)

	print('│', end='')
	for i in range(size * octaves + 1):
		if (i % size) == 0:
			print('[', end='')

		print(notes[(start + i) % size], end='')
		
		if (i % size) == 0:
			print(']', end='')
		
		if i >= 0 and i < (size * octaves):
			if len(notes[(start + i) % size]) == 1:
				print('───', end='')
			else:
				print('──', end='')
	print('│')

def print_instrument(instrument):

	octaves = 3

	name = str(instrument['key']) + ' Note Chart'

	heading_length = (octaves * 50 + 1) - len(name)
	padding = heading_length // 2

	dashes = octaves * 50 + 3

	odd = 1
	if heading_length % 2 != 1:
		odd = 0

	print('┌' + '─' * padding + ' ', end='')
	print(f'{str(instrument['key'])} Note Chart', end='')
	print(' ' + '─' * (padding + odd) + '┐')
	print('│' + ' ' * dashes + '│')

	print('├' + '─' * dashes + '┤')
	for i in reversed(instrument['strings']):
		print_string(i, octaves)
	print('└' + '─' * dashes + '┘\n')

def print_instruments(instruments):
	for i in instruments:
		print_instrument(i)

instruments = [{ 'key': 'Guitar',   'strings': ['E', 'A', 'D', 'G', 'B', 'E']},
			   { 'key': 'Ukelele',  'strings': ['G', 'C', 'E', 'A']},
 			   { 'key': 'Violin',   'strings': ['G', 'D', 'A', 'E']},
 			   { 'key': 'Bouzouki', 'strings': ['C', 'F', 'A', 'D']}]

print_instruments(instruments)