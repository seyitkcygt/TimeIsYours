from tube import Tube


import copy


class Node:  # store the information about all posible valuess
	def __init__(self,curr_liste,level):
		self.possible_list = [] # all posiblle values
		self.chosen_list = []  # chosen values
		self.curr_list = curr_liste # get the current state which has tube classes in it
		self.calculatelist = []
		self.avaliableforpush = []
		self.completedlist = []
		self.f = 0
		self.level = level
		self.refresh()


	def refresh(self):
		self.calculatelist = []
		self.avaliableforpush = []

		for i in self.curr_list:
			if(i.spaceCount() != 0):
				self.avaliableforpush.append(i)      # get all tubes that has avaliable space

		for i in self.curr_list:
			if(i.currSize() != 0):
				self.calculatelist.append(i)         # get all tubes that is has some elements

	def check(self):
		for i in self.curr_list:
			if(i.spaceCount() == 0 and i.checkElems() == 0):
				self.completedlist.append(i)
				self.curr_list.remove(i)


	def calcH(self):
		h = 0
		for i in self.calculatelist:
			h += i.spaceCount() + i.checkElems()           # h value is gonna be sum of the avaliable space count and different type of items
		return h

	def calculatef(self):
		# for h we are gonna take the nu ber of differnt ballsand number of avalible sapce
		# g is gonna be the level number
		# f = h + g
		h = self.calcH()

		self.f = h + self.level



	def writecurr(self):       # write tubes
		for i in self.curr_list:
			print(i)
			for j in i.elements:
				print(j)


	def generate_childs(self):
		self.refresh()
		children = []


		for i in self.curr_list:           # take a tube from list
			for j in self.avaliableforpush:   # take another tube that has avaliable space to push element
				if(len(i.elements) == 0):        # if first tube empty break
					break

				j.push(i.pop())           # push elemnt to second tube that popped from the first tube
				cl = []
				for c in self.curr_list:
					t = copy.deepcopy(c)    # deepcopy all the tubes that is in current list
					cl.append(t)

				child_node = Node(cl,self.level+1)   # create a new instance of node with new list "cl"
				child_node.calculatef()              # calculate f value of that instance
				children.append(child_node)          # append that instance to children list
				i.push(j.pop())                      # take back our move to not change the base case to be able to generate all possible values


		return children





	def isEqual(self,node2): # return true if the conitions are same like a tube 

				#    has [1,2,3],[],[2,1,3] and other one has
				#     [],[2,1,3],[1,2,3]


		conc = []
		res = []

		for i in node2.curr_list:
			t = []
			for j in self.curr_list:
				# i and j are tubes
				if(i.isEqual(j) != True):
					continue
				else:
					t.append(1)
			conc.append(t)

		for i in conc:
			if(sum(i) >= 1):
				res.append(1)
			else:
				res.append(0)

		if(0 in res):
			return False
		else:
			return True

