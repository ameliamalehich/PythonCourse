>>> line1 = 'GAGCCTACTAACGGGAT'
>>> line2 = 'CATCGTAATGACGGCCT'
>>> distance = [(x,y) for x,y in zip(line1, line2) if x != y]
>>> print(len(distance))
