def makeSubtaskDifficulties():
	# given number of nodes
	# given number of users
	user_subtasks = {}
	for i in range(n_user):
		# input user name
		subtasks = {}
		for j in range(n_nodes):
			for k in range(n_nodes):
				# associate j to k with given difficulty
	return user_subtasks

def createTaskRecipe(subtasks):
	# given start and end node.
	path = dijkstra(start, end)
	return path, start, end

def resetSubtaskDifficulties(user_subtasks, user):
	# given node1 and node2, reset the task difficulties

def renderTaskRecipes(user_subtasks):
	recipes = {}
	for user in user_subtasks:
		recipe = createTaskRecipe(user_subtasks[user])
		recipes[(user, start, end)] = recipe
	return recipes