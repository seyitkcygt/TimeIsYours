import copy
class Tube():
	def __init__(self,max_size,elements):
		self.max_size = max_size
		self.elements = elements # list of integers that current tube has


	def currSize(self):
		return len(self.elements)


	def spaceCount(self):
		return self.max_size - self.currSize()

	def pop(self):
		popped = self.elements[-1]
		self.elements = self.elements[:-1]
		return popped

	def push(self,elem):
		self.elements.append(elem)

	def checkElems(self):
		types = {}
		for i in self.elements:
			if(i in types):
				types[i] += 1
			else:
				types[i] = 1

		return len(types) - 1


	def isEqual(self,t2):
		return self.elements == t2.elements


		




# heuristic function will be sum of check elements and space count