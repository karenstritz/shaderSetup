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
import PythonQt
from PythonQt import QtGui, QtCore

# ------------------------------------------------------------------------------

# set up toolbar and create shader setup window when monkey icon is clicked
def toolbar():
	mari.app.createToolBar('Custom Tools', 4, 1)
	customTools = mari.app.toolBar('Custom Tools')
	shaderSetupAction = mari.actions.create('Shader Setup', 'window = shaderSetupClass()')
	shaderSetupAction.setIconPath(mari.resources.path(mari.resources.ICONS)+"/Monkey.png" )
	customTools.addAction('/Mari/Scripts/Shader Setup', [1,2], 0)
	
if mari.app.isRunning():
	mari.app.deleteToolBar('Custom Tools')
	toolbar()
