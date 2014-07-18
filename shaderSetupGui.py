# ------------------------------------------------------------------------------
# Shader Setup by Karen Stritzinger 
# June 2014
# A tool for MARI 2.0 and above to set up diffuse, bump, and specular channels 
# and connect them to appropriate inputs in a specified type of shader. Bump
# and spec channels are created with a base color of 50% gray. The diffuse 
# channel resolution and depth are set to match the newly created bump and spec 
# channels. Multiple shaders can be created if the tool is used again. In this 
# case, channels will not be created again.
# ------------------------------------------------------------------------------

import mari
import PythonQt
from PythonQt import QtGui as gui
from PythonQt import QtCore as core
import shaderSetup as ss

# ------------------------------------------------------------------------------

class shaderSetupClass:
	def __init__(self):
		print "-----Shader Setup-----"
		self.dlg = gui.QDialog()
		self.createDropDowns()
		self.createButtons()
		self.createLayout()
		self.connect()
		self.setLayout()
		self.checkResult()
		
	def createDropDowns(self):
		# create shader type drop down box
		self.shaderTypeBox = gui.QComboBox()
		self.shaderTypeBox.addItem("Diffuse Specular")
		self.shaderTypeBox.addItem("Standalone")
		# set default to Diffuse Specular
		self.shaderTypeBox.setCurrentIndex(0)
		
		# create diffuse type drop down
		self.diffuseTypeBox = gui.QComboBox()
		self.diffuseTypeBox.addItem("Lambertian")
		self.diffuseTypeBox.addItem("Minnaert")
		# set default to Lambertian
		self.diffuseTypeBox.setCurrentIndex(0)
		
		# create specular type drop down
		self.specularTypeBox = gui.QComboBox()
		self.specularTypeBox.addItem("Phong")
		self.specularTypeBox.addItem("Cook Torrance")
		self.specularTypeBox.addItem("Beckman")
		self.specularTypeBox.addItem("Blinn")
		# set default to Phong
		self.specularTypeBox.setCurrentIndex(0)
		
		# create subtype drop down
		self.subTypeBox = gui.QComboBox()
		self.subTypeBox.addItem("Flat")
		self.subTypeBox.addItem("BRDF")
		self.subTypeBox.addItem("Standard Lighting")
		# set default to Flat
		self.subTypeBox.setCurrentIndex(0)
		
		# create resolution drop down
		self.resBox = gui.QComboBox()
		self.resBox.addItem("256")
		self.resBox.addItem("512")
		self.resBox.addItem("1024")
		self.resBox.addItem("2048")
		self.resBox.addItem("4096")
		self.resBox.addItem("8192")
		self.resBox.addItem("16384")
		self.resBox.addItem("32768")
		# set default to 4096
		self.resBox.setCurrentIndex(4)
		
		# create depth drop down
		self.depthBox = gui.QComboBox()
		self.depthBox.addItem("8")
		self.depthBox.addItem("16")
		self.depthBox.addItem("32")
		# set default to 8-bit
		self.depthBox.setCurrentIndex(0)
		
	def createButtons(self):
		# buttons to run setup shader script and cancel
		self.setupShaderButton = gui.QPushButton("Set Up Shader")
		self.cancelButton = gui.QPushButton("Cancel")
	
	def createLayout(self):
		# create layout
		self.layout = gui.QFormLayout()
		self.layout.addRow("Shader Type", self.shaderTypeBox)
		self.layout.addRow("Diffuse Type", self.diffuseTypeBox)
		self.layout.addRow("Specular Type", self.specularTypeBox)
		self.layout.addRow("Subtype", self.subTypeBox)
		self.layout.addRow("Channel Resolution", self.resBox)
		self.layout.addRow("Channel Depth", self.depthBox)
		self.layout.addRow(self.setupShaderButton, self.cancelButton)
		
	def connect(self):
		# connect result to button
		self.setupShaderButton.connect("clicked()", self.dlg.accept)
		self.cancelButton.connect("clicked()", self.dlg.reject)
	
	def setLayout(self):
		# set layout
		self.dlg.setLayout(self.layout)
		self.dlg.setWindowTitle("Shader Setup")

	def checkResult(self):
		self.result = self.dlg.exec_()

		if self.result == 1:
			# run script using input settings
			ss.shaderSetup(self.shaderTypeBox.currentText, self.diffuseTypeBox.currentText, self.specularTypeBox.currentText, self.subTypeBox.currentText, self.resBox.currentText, self.depthBox.currentText)
		if self.result == 0:
			print "Shader set up cancelled."
