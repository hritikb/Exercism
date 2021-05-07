def convert(number):
	string = ''.join(map(lambda x: x[1] if number % x[0] == 0 else '', {3:'Pling', 5:'Plang', 7:'Plong'}.items())) 
	return string if string != '' else str(number)

#Notes
#	(1).join() takes a list or iterable as an argument and forms a string by using the '' in between.
#	(2)map() takes two arguments one a function and the other an iterable each element of which will be passed to 
#   the function
#	items returns a list of tuples containing the dictionary key and value pairs eg. [(3, 'Pling'), (5, 'Plang'),
#	(7, 'Plong')]
