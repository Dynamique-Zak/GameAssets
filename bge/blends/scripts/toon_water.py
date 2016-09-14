from bge import logic

def base(cont):
	own = cont.owner
	speed_y = 0.01  # speed by which the coordinates are moved
	mesh = own.meshes[0] # access the mesh of the object in question
	v_array = mesh.getVertexArrayLength(0) # how many verts are there?
	for v in range(0,v_array): # go through the uv's of every vert
		vert = mesh.getVertex(0, v)
		uv = vert.getUV()
		uv[1] += speed_y # change the uv coordinates. uv[0] = x, uv[1] = y
		vert.setUV(uv)

def edge_water(cont):
	own = cont.owner
	speed_x = own['speed'] # speed by which the coordinates are moved
	mesh = own.meshes[0] # access the mesh of the object in question
	v_array = mesh.getVertexArrayLength(0) # how many verts are there?
	for v in range(0,v_array): # go through the uv's of every vert
		vert = mesh.getVertex(0, v)
		uv = vert.getUV()
		uv[0] += speed_x # change the uv coordinates. uv[0] = x, uv[1] = y
		vert.setUV(uv) # get the game engine to notice the change!!
