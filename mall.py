def P1(dictionary):
	floor_colors = dictionary["floor_colors"]
	sections = dictionary["sections"]
	numbers = dictionary["numbers"]

	res = []

	for color in floor_colors:
		for sec in sections:
			for number in numbers:
				st = color + " " + sec + ":" + str(number)
				res.append(st)


	return res


def P2(dictionary):
	floor_colors = dictionary["floor_colors"]
	sections = dictionary["sections"]
	numbers = dictionary["numbers"]

	res = []

	c = 0
	s = 0
	n = 0

	while c < len(floor_colors):
		while s < len(sections):
			while n < len(numbers):
				st = floor_colors[c] + " " + sections[s] + ":" + str(numbers[n])
				res.append(st)
				n += 1
			s += 1
			n = 0
		c += 1
		s = 0


	return(res)






def P3(liste):
	res = []
	for i,H in enumerate(liste):
		if(H.find("Green") == 0):
			res.append([H,False])

		else:
			if(H.find(str((i+1)%10)) != -1 and ((i+1)%10 in [1,3,5,7,9])):

				res.append([H,False])

			else:
				res.append([H,True])


	return res





def P4(liste):
	res = []
	for p in liste:
		if(p[1]):
			res.append(p)

	return "There is a total of {} parking spaces in the mall and currently {} of them are available.".format(len(liste),len(res))


def P5(liste,day="weekday"):
	if(day == "weekend"):
		return P3(liste)
	else:
		return [i for i in P3(liste) if i[0].find("Red") == -1]



dc = {'floor_colors':('Red','Green','Orange','Yellow'),
'sections': ('A','B','C','D'),
'numbers': (1,2,3,4,5,6,7,8,9,10)
}
 
print(P1(dc))

print(P3(P1(dc)))

print(P4(P1(dc)))

print(P5(P1(dc)))


