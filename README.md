# BreadthFirstSearch
- given a tree with Node class each node has Name and their optional children node.
- when put together , nodes form an acyclic tree like structure
- implement the breadthFirstSearch method on the Node class, take empty array as paremeter and return travesers the tree using the BFS approach, stores all of the nodes's name in te input array, and returns it.
# Solution
- because Queue is FIFO , so we can use it to process it node and current children,
- at each time  poll the first element of the list then add it to the current array result
- and then we addALl children in the queue
- the current add in will stay at the end
- then continue to poll the next element in the Queue, 
- the next loop it will poll out children of current loop and put children of the first current children to the Queue
- the loop will process until no more element in queue.
- return the array result.
