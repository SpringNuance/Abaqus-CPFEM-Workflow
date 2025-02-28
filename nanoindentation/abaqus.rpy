# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2023.HF4 replay file
# Internal Version: 2023_07_21-20.45.57 RELr425 183702
# Run by nguyenb5 on Tue Feb  4 19:50:48 2025
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=231.796875, 
    height=125.986106872559)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
openMdb('D0014_Nanoindentation.cae')
#: A new model database has been created.
#: The model "Model-1" has been created.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#* MdbError: incompatible release number, expected 2023.HF4, got 2018
upgradeMdb(
    "C:/LocalUserData/User-data/nguyenb5/Abaqus-CPFEM-Workflow/nanoindentation/D0014_Nanoindentation-2018.cae", 
    "C:/LocalUserData/User-data/nguyenb5/Abaqus-CPFEM-Workflow/nanoindentation/D0014_Nanoindentation.cae", 
    )
#: The model database "C:\LocalUserData\User-data\nguyenb5\Abaqus-CPFEM-Workflow\nanoindentation\D0014_Nanoindentation_TEMP.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#: The model database has been saved to "C:\LocalUserData\User-data\nguyenb5\Abaqus-CPFEM-Workflow\nanoindentation\D0014_Nanoindentation.cae".
#: The model database "C:\LocalUserData\User-data\nguyenb5\Abaqus-CPFEM-Workflow\nanoindentation\D0014_Nanoindentation-2018.cae" has been converted.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
a = mdb.models['Model-1-Standard'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON, 
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=141.312, 
    farPlane=291.882, width=126.249, height=64.7015, viewOffsetX=35.019, 
    viewOffsetY=22.6842)
session.viewports['Viewport: 1'].view.setValues(nearPlane=143.807, 
    farPlane=289.387, width=128.478, height=65.8439, viewOffsetX=-1.57794, 
    viewOffsetY=0.655822)
session.viewports['Viewport: 1'].view.setValues(nearPlane=151.194, 
    farPlane=275.036, width=135.078, height=69.2259, cameraPosition=(-0.474048, 
    58.7522, -184.887), cameraUpVector=(-0.91878, 0.107035, 0.379983), 
    cameraTarget=(-0.712723, -4.34567, 22.316), viewOffsetX=-1.65899, 
    viewOffsetY=0.689508)
session.viewports['Viewport: 1'].view.setValues(nearPlane=144.462, 
    farPlane=280.732, width=129.063, height=66.1434, cameraPosition=(129.303, 
    10.507, -148.459), cameraUpVector=(-0.950888, 0.0013238, -0.309534), 
    cameraTarget=(-2.42672, -3.52382, 22.903), viewOffsetX=-1.58512, 
    viewOffsetY=0.658806)
session.viewports['Viewport: 1'].view.setValues(nearPlane=159.843, 
    farPlane=265.35, width=44.073, height=22.587, viewOffsetX=-1.45968, 
    viewOffsetY=7.96687)
session.viewports['Viewport: 1'].view.setValues(nearPlane=160.104, 
    farPlane=259.641, width=44.1448, height=22.6238, cameraPosition=(167.101, 
    -4.89455, -106.924), cameraUpVector=(-0.836164, 0.0149197, -0.548276), 
    cameraTarget=(-5.23553, -3.11557, 24.2676), viewOffsetX=-1.46206, 
    viewOffsetY=7.97986)
session.viewports['Viewport: 1'].view.setValues(nearPlane=160.004, 
    farPlane=261.783, width=44.1172, height=22.6097, cameraPosition=(153.947, 
    1.41374, -124.164), cameraUpVector=(-0.888285, -0.0125787, -0.459121), 
    cameraTarget=(-3.89525, -3.11372, 24.0906), viewOffsetX=-1.46115, 
    viewOffsetY=7.97487)
session.viewports['Viewport: 1'].view.setValues(nearPlane=162.162, 
    farPlane=259.624, width=33.7104, height=17.2762, viewOffsetX=-0.616955, 
    viewOffsetY=14.9654)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, interactions=OFF, constraints=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=143.547, 
    farPlane=278.239, width=146.679, height=75.1714, viewOffsetX=16.8265, 
    viewOffsetY=-9.67188)
session.viewports['Viewport: 1'].view.setValues(nearPlane=150.331, 
    farPlane=295.109, width=153.611, height=78.7243, cameraPosition=(187.524, 
    -64.9266, -81.7179), cameraUpVector=(-0.629059, 0.447752, -0.635455), 
    cameraTarget=(11.3233, 1.05604, 25.5839), viewOffsetX=17.6218, 
    viewOffsetY=-10.129)
session.viewports['Viewport: 1'].view.setValues(nearPlane=178.795, 
    farPlane=325.922, width=182.696, height=93.63, cameraPosition=(79.0146, 
    -208.46, 140.934), cameraUpVector=(-0.163838, -0.281198, -0.945561), 
    cameraTarget=(25.9374, -35.2197, 22.2556), viewOffsetX=20.9583, 
    viewOffsetY=-12.0468)
session.viewports['Viewport: 1'].view.setValues(nearPlane=179.252, 
    farPlane=333.432, width=183.162, height=93.8691, cameraPosition=(-10.4006, 
    -151.924, 227.945), cameraUpVector=(-0.0780848, -0.615713, -0.784092), 
    cameraTarget=(13.2968, -38.8635, 44.7239), viewOffsetX=21.0118, 
    viewOffsetY=-12.0776)
session.viewports['Viewport: 1'].view.setValues(nearPlane=169.902, 
    farPlane=327.85, width=173.608, height=88.9728, cameraPosition=(181.167, 
    -142.375, -79.518), cameraUpVector=(-0.541871, 0.301451, -0.78454), 
    cameraTarget=(31.2009, -0.705118, -13.5311), viewOffsetX=19.9158, 
    viewOffsetY=-11.4476)
session.viewports['Viewport: 1'].view.setValues(nearPlane=194.447, 
    farPlane=303.306, width=39.7648, height=20.3791, viewOffsetX=15.2453, 
    viewOffsetY=-0.755871)
session.viewports['Viewport: 1'].view.setValues(nearPlane=196.083, 
    farPlane=308.337, width=40.0993, height=20.5505, cameraPosition=(184.787, 
    -113.602, -112.473), cameraUpVector=(-0.606482, 0.387364, -0.694355), 
    cameraTarget=(30.6242, 4.14022, -16.1143), viewOffsetX=15.3735, 
    viewOffsetY=-0.76223)
session.viewports['Viewport: 1'].view.setValues(nearPlane=194.97, 
    farPlane=309.449, width=43.4937, height=22.2901, viewOffsetX=11.4453, 
    viewOffsetY=1.56128)
session.viewports['Viewport: 1'].view.setValues(nearPlane=194.581, 
    farPlane=284.798, width=43.4068, height=22.2455, cameraPosition=(131.664, 
    -201.102, -1.47023), cameraUpVector=(-0.330122, 0.19415, -0.923756), 
    cameraTarget=(26.2113, -11.9101, -2.17936), viewOffsetX=11.4224, 
    viewOffsetY=1.55816)
session.viewports['Viewport: 1'].view.setValues(nearPlane=193.766, 
    farPlane=289.653, width=43.225, height=22.1523, cameraPosition=(134.554, 
    -198.143, -22.1047), cameraUpVector=(-0.283738, 0.316523, -0.905155), 
    cameraTarget=(26.4267, -11.4712, -2.6975), viewOffsetX=11.3745, 
    viewOffsetY=1.55163)
session.viewports['Viewport: 1'].view.setValues(nearPlane=174.5, 
    farPlane=308.92, width=162.773, height=83.4196, viewOffsetX=12.8208, 
    viewOffsetY=-3.15626)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF, adaptiveMeshConstraints=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON, 
    adaptiveMeshConstraints=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, interactions=OFF, constraints=OFF, 
    engineeringFeatures=OFF)
