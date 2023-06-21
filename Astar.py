
from UCS import Node
from UCS import Tube

from datetime import datetime

class Astar:
	def __init__(self): # define some veriables to use
		self.open = []
		self.closed = []
		self.tubes = []
		self.value_size = 0
		self.steps = 0

	def isEqual(self,n1,n2):
		return n1.isEqual(n2)


	def procces(self,textfile):
		currtime = datetime.now()         # get current time measure time
		file = open(textfile,"r")
		firstline = file.readline().strip()
		empty_tube_count = int(firstline.split(" ")[1])   # get values from file

		for line in file.readlines():               # for ever line of file
			values = line.strip().split(" ")		# split line by space to get ints
			values = [int(x) for x in values]
			self.value_size = len(values)
			t = Tube(len(values),values)           # create instance of Tube class
			self.tubes.append(t)

		for i in range(empty_tube_count):
			t = Tube(self.value_size,[])           # create empty Tube instance
			self.tubes.append(t)


		firstNode = Node(self.tubes,1)             # create instance of node with Tubes
		self.open.append(firstNode)
		self.closed.append(firstNode)

		while True:
			correctopen = []
			self.steps += 1                        # increase steps every turn
			curr = self.open[0]	
			self.closed.append(curr)					# get the node which has the minimum f value
			curr.writecurr()
			print("\n\n\n")
			if(curr.calcH() == 0):                 # if h value of node is 0 than all tubes sorted
				break

			l = curr.generate_childs()           # generate all possible nodes based on used node
			for i in l:

				for j in self.closed:
					if(self.isEqual(i,j)):        # see if the two nodes have same conditions in terms of tubes and tube values
						break
				else:
					correctopen.append(i)          # append only unused nodes to avoid to our program from going back

			self.open = correctopen              # change open list to correctopen

			
			self.open.sort(key=lambda x:x.f,reverse=False)  # sort open list increasing order by f value

		print(self.steps, " steps : Finished in " ,(datetime.now()-currtime).seconds, "seconds",(datetime.now()-currtime).microseconds, "microseconds" )

		file.close()

		




a = Astar()
a.procces("initfile.txt") # 10 steps
