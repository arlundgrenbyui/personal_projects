from graphviz import Digraph

def exp_3_and_mod_100(i):
	return (i ** 3) % 100

def exp_3_and_mod_50(i):
	return (i ** 3) % 50

def exp_2_and_mod_100(i):
	return (i ** 2) % 100

def exp_2_and_mod_50(i):
	return (i ** 2) % 50

def find_loop(number, op):
	loop = [number]
	i = number
	loop_found = False
	done = False
	while not done:
		i = op(i)
		if i == 0 or i == 1:
			done = True
		if i in loop and i == number:
			if len(loop) > 1:
				loop_found = True
				done = True
				loop.append(i)
			else:
				done = True
		elif i in loop and i != number:
			done = True
		else:
			loop.append(i)
	if loop_found:
		return loop
	else:
		return False

loops = []
loops1 = []
loops2 = []
loops3 = []
for x in range (2,101):
	result = find_loop(x, exp_2_and_mod_100)
	if result != False:
		if len(loops) > 0:
			dup = False
			for loop in loops:
				for ele in loop:
					if ele in result:
						dup = True
						break
			if not dup:
				loops.append(result)
		else:
			loops.append(result)
	result = find_loop(x, exp_3_and_mod_100)
	if result != False:
		if len(loops1) > 0:
			dup = False
			for loop in loops1:
				for ele in loop:
					if ele in result:
						dup = True
						break
			if not dup:
				loops1.append(result)
		else:
			loops1.append(result)
	result = find_loop(x, exp_2_and_mod_50)
	if result != False:
		if len(loops2) > 0:
			dup = False
			for loop in loops2:
				for ele in loop:
					if ele in result:
						dup = True
						break
			if not dup:
				loops2.append(result)
		else:
			loops2.append(result)
	result = find_loop(x, exp_3_and_mod_50)
	if result != False:
		if len(loops3) > 0:
			dup = False
			for loop in loops3:
				for ele in loop:
					if ele in result:
						dup = True
						break
			if not dup:
				loops3.append(result)
		else:
			loops3.append(result)

graphs = []
ascii_val = 65
for loop in loops:
	dot = Digraph(comment='Loop')
	for ele in loop:
		dot.node(chr(ascii_val), str(ele))
		ascii_val += 1
	for x in range(65,ascii_val):
		if x != ascii_val - 1:
			dot.edge(chr(x), chr(x + 1), constraint='false')
		else:
			dot.edge(chr(x), chr(65), constraint='false')
	graphs.append(dot)
	ascii_val = 65

num_graphs = 1
for graph in graphs:
	graph.format = 'png'
	graph.render('test-output/loopx2mod100_%d.gv' % num_graphs, view=True)
	num_graphs += 1

graphs = []
ascii_val = 65
for loop in loops1:
	dot = Digraph(comment='Loop')
	for ele in loop:
		dot.node(chr(ascii_val), str(ele))
		ascii_val += 1
	for x in range(65,ascii_val):
		if x != ascii_val - 1:
			dot.edge(chr(x), chr(x + 1), constraint='false')
		else:
			dot.edge(chr(x), chr(65), constraint='false')
	graphs.append(dot)
	ascii_val = 65

num_graphs = 1
for graph in graphs:
	graph.format = 'png'
	graph.render('test-output/loopx2mod50_%d.gv' % num_graphs, view=True)
	num_graphs += 1

graphs = []
ascii_val = 65
for loop in loops2:
	dot = Digraph(comment='Loop')
	for ele in loop:
		dot.node(chr(ascii_val), str(ele))
		ascii_val += 1
	for x in range(65,ascii_val):
		if x != ascii_val - 1:
			dot.edge(chr(x), chr(x + 1), constraint='false')
		else:
			dot.edge(chr(x), chr(65), constraint='false')
	graphs.append(dot)
	ascii_val = 65

num_graphs = 1
for graph in graphs:
	graph.format = 'png'
	graph.render('test-output/loopx3mod100_%d.gv' % num_graphs, view=True)
	num_graphs += 1

graphs = []
ascii_val = 65
for loop in loops3:
	dot = Digraph(comment='Loop')
	for ele in loop:
		dot.node(chr(ascii_val), str(ele))
		ascii_val += 1
	for x in range(65,ascii_val):
		if x != ascii_val - 1:
			dot.edge(chr(x), chr(x + 1), constraint='false')
		else:
			dot.edge(chr(x), chr(65), constraint='false')
	graphs.append(dot)
	ascii_val = 65

num_graphs = 1
for graph in graphs:
	graph.format = 'png'
	graph.render('test-output/loopx3mod50_%d.gv' % num_graphs, view=True)
	num_graphs += 1
# for loop in loops:
# 	print(loop)


	#print(find_loop(x, exp_2_and_mod_50))