shaderSetup
===========

A tool for MARI 2.0 and above to set up diffuse, bump, and specular channels and connect them to appropriate inputs in a specified type of shader. Bump and spec channels are created with a base color of 50% gray. The diffuse channel resolution and depth are set to match the newly created bump and spec channels. Multiple shaders can be created if the tool is used again. In this case, channels will not be created again.

How to use:

1. Copy and paste shaderSetup.py, shaderSetupGui.py, and shaderSetupGuiLoader.py to your /Mari/Scripts folder, or create a new folder for these scripts and add the path to your MARI_SCRIPT_PATH in your bash file.
2. Open Mari. If you already had Mari open, close it and open it again for the new scripts to take effect.
3. Create a new project in Mari.
4. In your toolbar, you should see a monkey icon. Click it to open the Shader Setup tool. 
5. Select the type of shader you would like to create, and the resolution and bit depth you would like your new diffuse, bump and spec channels to have. 
6. You can use the Shader Setup tool again if you would like to have multiple shaders. Shaders will be created with default names to help you remember what type of shader it is. Make sure to use the same resolution and depth settings as the first time you created a shader using Shader Setup. 

Future changes:

1. I would like the Diffuse Type and Specular Type drop-downs to be enabled only when the "Diffuse Specular" Shader Type is selected. When the "Standalone" Shader Type is selected, Subtype should be enabled. Channel Resolution and Channel Depth should always be enabled when Shader Setup is used for the first time. 
2. When using Shader Setup multiple times, it should check the resolution and depth of existing channels and set the settings to match this. Then , these settings could also be disabled so that the user does not waste time adjusting them.
3. Create a pretty icon that relates to what the tool does. Create a banner for the GUI that matches this icon. 
4. Add tooltips to different options.
5. Add information to help (?) button.

