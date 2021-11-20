import numpy as np

class edge:
	def __init__(self, fromV, to, cost):
		self.fromV = fromV
		self.to = to
		self.cost = cost

def dijkstra(g, n, s):
	vis = [false] * n
	dist = [np.inf] * n
	dist[s] = 0
	pq = []
	pq.append((s,0))
	while = len(pq) != 0:
		index, minValue = pq.poll()
		vis[index] = True
		for edge in g[index]:
			if vis[edge.to]: continue
			newDist = dist[index] + edge.cost
			if newDist < dist[edge.to]:
				dist[edge.to] = newDist
				pq.append((edge.to, newDist))
	return dist

def makeSubtaskDifficulties():
	# given number of nodes
	n_nodes = raw_input("please provide number of nodes")
	# given number of users
	n_user = raw_input("please provide number of users")
	user_subtasks = {}
	for i in range(n_user):
		# input user name
		user_name = raw_input("please provide the user name")
		subtasks = {}
		for j in range(n_nodes):
			for k in range(n_nodes):
				# associate j to k with given difficulty
				j = raw_input("please provide node 1")
				k = raw_input("please provide node 2")
				difficulty = raw_input("please provide updated difficulty")
				subtasks[(j,k)] = d
		user_subtasks[user_name] = subtasks
	return user_subtasks

def createTaskRecipe(subtasks):
	# given start and end node.
	path = dijkstra(start, end)
	return path, start, end

def resetSubtaskDifficulties(user_subtasks, user):
	# given node1 and node2, reset the task difficulties
	node1 = raw_input("please provide node 1")
	node2 = raw_input("please provide node 2")
	difficulty = raw_input("please provide updated difficulty")
	user_subtasks[user][(node1, node2)] = difficulty

def renderTaskRecipes(user_subtasks):
	recipes = {}
	for user in user_subtasks:
		recipe = createTaskRecipe(user_subtasks[user])
		recipes[(user, start, end)] = recipe
	return recipes