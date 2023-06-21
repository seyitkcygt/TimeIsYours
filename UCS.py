
from node import Node
from tube import Tube

from datetime import datetime



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


class UCS:
	def __init__(self):  # define some veriables to use
		self.closed = []
		self.open = []
		self.tubes = []
		self.value_size = 0
		self.steps = 0



	def isEqual(self,n1,n2):
		return n1.isEqual(n2)


	def procces(self,textfile):
		currtime = datetime.now()            # get current time measure time
		file = open(textfile,"r")
		firstline = file.readline().strip()
		empty_tube_count = int(firstline.split(" ")[1])          # get values from file

		for line in file.readlines():
			values = line.strip().split(" ")           # for ever line of file
			values = [int(x) for x in values]			# split line by space to get ints
			self.value_size = len(values)				
			t = Tube(len(values),values)                # create instance of Tube class
			self.tubes.append(t)

		for i in range(empty_tube_count):
			t = Tube(self.value_size,[])                # create empty Tube instance
			self.tubes.append(t)


		firstNode = Node(self.tubes,1)                  # create instance of node with Tubes
		self.open.append(firstNode)

		while True:
			
			self.steps += 1                      # increase steps every turn
			curr = self.open[0]                  # get the node which has the minimum f value
			curr.writecurr()
			print("\n\n\n")
			if(len(self.open) == 0 or curr.calcH() == 0):
				break
			

			for i in curr.generate_childs():         # generate all possible nodes
				i.f += curr.f   
				for j in self.open:
					if (self.isEqual(i,j)):
						#that means we already have that child in our list
						break
				else:
					self.open.append(i)



			self.closed.append(curr)				# append used node to the closed list

			del self.open[0]						# delete used node from the open list

			

			self.open.sort(key=lambda x:x.f,reverse=False)           # sort open list based on the cumulative cost values of nodes

		print(self.steps, " steps : Finished in " ,(datetime.now()-currtime).seconds, "seconds",(datetime.now()-currtime).microseconds, "microseconds" )



		



if __name__ == "__main__":

	a = UCS()
	a.procces("initfile.txt") # 952 steps # 5640

