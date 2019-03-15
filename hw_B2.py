>>> string1 = 'AAAACCCGGT'
	    
>>> compl = str.maketrans('ATCG', 'TAGC')
	    
>>> string2 = (string1.translate(compl))[::-1]
	    
>>> print(string2)
