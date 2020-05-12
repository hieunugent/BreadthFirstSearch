class Node:
    def _init_(seft,name):
      seft.children= []
      seft.name= name
    
    def addChild(seft, name):
      seft.children.append(Node(name))
      return seft
    
    def breadthFirstSearch(self, array):
        queue = [self]
		    while len(queue) > 0:
		    	current = queue.pop(0)
		    	array.append(current.name)
		    	for child in current.children:
			    	queue.append(child)
	    	return array
    
