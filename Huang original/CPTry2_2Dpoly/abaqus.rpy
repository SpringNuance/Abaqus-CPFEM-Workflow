# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2023.HF4 replay file
# Internal Version: 2023_07_21-20.45.57 RELr425 183702
# Run by nguyenb5 on Mon Jan 27 17:32:22 2025
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=231.796875, 
    height=148.547454833984)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
openMdb('CPTry2_2Dpoly.cae')
#: A new model database has been created.
#: The model "Model-1" has been created.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#* MdbError: incompatible release number, expected 2023.HF4, got 6.12-1
upgradeMdb(
    "C:/LocalUserData/User-data/nguyenb5/Abaqus-Strain-Gradient-Plasticity-Nanoindentation-Project/Huang original/CPTry2_2Dpoly/CPTry2_2Dpoly-6.12-1.cae", 
    "C:/LocalUserData/User-data/nguyenb5/Abaqus-Strain-Gradient-Plasticity-Nanoindentation-Project/Huang original/CPTry2_2Dpoly/CPTry2_2Dpoly.cae", 
    )
#: The model database "C:\LocalUserData\User-data\nguyenb5\Abaqus-Strain-Gradient-Plasticity-Nanoindentation-Project\Huang original\CPTry2_2Dpoly\CPTry2_2Dpoly_TEMP.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#: The model database has been saved to "C:\LocalUserData\User-data\nguyenb5\Abaqus-Strain-Gradient-Plasticity-Nanoindentation-Project\Huang original\CPTry2_2Dpoly\CPTry2_2Dpoly.cae".
#: The model database "C:\LocalUserData\User-data\nguyenb5\Abaqus-Strain-Gradient-Plasticity-Nanoindentation-Project\Huang original\CPTry2_2Dpoly\CPTry2_2Dpoly-6.12-1.cae" has been converted.
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
p1 = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
