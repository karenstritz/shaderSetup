# ------------------------------------------------------------------------------
# Shader Setup by Karen Stritzinger 
# June 2014
# A tool for MARI 2.0 and above to set up diffuse, bump, and specular channels 
# and connect them to appropriate inputs in a specified type of shader. Bump
# and spec channels are created with a base color of 50% gray. Multiple shaders
# can be created if the tool is used again. In this case, channels will not 
# be created again.
# ------------------------------------------------------------------------------

import mari

# ------------------------------------------------------------------------------

# create channels with resolution and depth selected by user
def createChannels(res, depth):
	obj = mari.geo.current()
	# set existing diffuse channel to specified res and depth 
	obj.channel('diffuse').resize(res)
	obj.channel('diffuse').setDepth(depth, 1)
	# check to see if bump and spec already exist
	channel = obj.currentChannel()
	if obj.findChannel('bump') == None:
		obj.createChannel('bump', res, res, depth)
		# create 'Base' bump layer filled with 50% gray
		obj.channel('bump').createPaintableLayer('Base', 0, mari.Color(.5,.5,.5, 1))
		print "Bump channel created."
	if obj.findChannel('spec') == None:
		obj.createChannel('spec', res, res, depth)
		# create 'Base' spec layer filled with 50% gray
		obj.channel('spec').createPaintableLayer('Base', 0, mari.Color(.5,.5,.5, 1))
		# set bump and spec channels to 50% gray
		print "Spec channel created."

# create shader based on type selected by user
def createShader(type, diffuse, specular, subtype):
	obj = mari.geo.current()
	# create specified type of shader
	if type == 'Diffuse Specular':
		if diffuse == 'Lambertian':
			if specular == 'Phong':
				shaderName = 'Phong - L'
				obj.createDiffuseSpecularShader(shaderName, 'Lighting/Diffuse/Lambertian', 'Lighting/Specular/Phong')
			if specular == 'Cook Torrance':
				shaderName = 'Cook Torrance - L'
				obj.createDiffuseSpecularShader(shaderName, 'Lighting/Diffuse/Lambertian', 'Lighting/Specular/Cook Torrance')
			if specular == 'Beckman':
				shaderName = 'Beckman - L'
				obj.createDiffuseSpecularShader(shaderName, 'Lighting/Diffuse/Lambertian', 'Lighting/Specular/Beckman')
			if specular == 'Blinn':
				shaderName = 'Blinn - L'
				obj.createDiffuseSpecularShader(shaderName, 'Lighting/Diffuse/Lambertian', 'Lighting/Specular/Blinn')
		
		if diffuse == 'Minnaert':
			if specular == 'Phong':
				shaderName = 'Phong - M'
				obj.createDiffuseSpecularShader(shaderName, 'Lighting/Diffuse/Minnaert', 'Lighting/Specular/Phong')
			if specular == 'Cook Torrance':
				shaderName = 'Cook Torrance - M'
				obj.createDiffuseSpecularShader(shaderName, 'Lighting/Diffuse/Minnaert', 'Lighting/Specular/Cook Torrance')
			if specular == 'Beckman':
				shaderName = 'Beckman - M'
				obj.createDiffuseSpecularShader(shaderName, 'Lighting/Diffuse/Minnaert', 'Lighting/Specular/Beckman')
			if specular == 'Blinn':
				shaderName = 'Blinn - M'
				obj.createDiffuseSpecularShader(shaderName, 'Lighting/Diffuse/Minnaert', 'Lighting/Specular/Blinn')
		
	if type == 'Standalone':
		if subtype == 'Flat':
			shaderName = 'Flat'
			obj.createStandaloneShader(shaderName, 'Lighting/Standalone/Flat')
		if subtype == 'BRDF':
			shaderName = 'BRDF'
			obj.createStandaloneShader(shaderName, 'Lighting/Standalone/BRDF')
		if subtype == 'Standard Lighting':
			shaderName = 'Standard Lighting'
			obj.createStandaloneShader(shaderName, 'Lighting/Standalone/Standard Lighting')
			
	print shaderName+" shader created."
	
	return shaderName
	
# connect channels into shader
def connectChannels(shaderName):
	obj = mari.geo.current()
	currentShader = obj.shader(shaderName)
	if shaderName == 'Flat':
		currentShader.setInput('Color', obj.channel('diffuse'))
	else:
		currentShader.setInput('DiffuseColor', obj.channel('diffuse'))
		currentShader.setInput('Bump', obj.channel('bump'))
		currentShader.setInput('SpecularColor', obj.channel('spec'))
		
	print "Shader set up successfully!"
	
# call functions to set up shaders
def shaderSetup(type, diffuse, specular, subtype, res, depth):
	res = int(res)
	depth = int(depth)
	shaderName = ''
	createChannels(res, depth)
	shaderName = createShader(type, diffuse, specular, subtype)
	connectChannels(shaderName)
