# trace generated using paraview version 5.9.1

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'AMReX/BoxLib Grid Reader'
plt00050 = AMReXBoxLibGridReader(registrationName='plt00050', FileNames=['plt00050'])
plt00050.CellArrayStatus = []

# get animation scene
animationScene1 = GetAnimationScene()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# Properties modified on plt00050
plt00050.CellArrayStatus = ['phi']

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
plt00050Display = Show(plt00050, renderView1, 'AMRRepresentation')

# trace defaults for the display properties.
plt00050Display.Representation = 'Outline'
plt00050Display.ColorArrayName = [None, '']
plt00050Display.SelectTCoordArray = 'None'
plt00050Display.SelectNormalArray = 'None'
plt00050Display.SelectTangentArray = 'None'
plt00050Display.OSPRayScaleFunction = 'PiecewiseFunction'
plt00050Display.SelectOrientationVectors = 'None'
plt00050Display.ScaleFactor = 0.1
plt00050Display.SelectScaleArray = 'None'
plt00050Display.GlyphType = 'Arrow'
plt00050Display.GlyphTableIndexArray = 'None'
plt00050Display.GaussianRadius = 0.005
plt00050Display.SetScaleArray = [None, '']
plt00050Display.ScaleTransferFunction = 'PiecewiseFunction'
plt00050Display.OpacityArray = [None, '']
plt00050Display.OpacityTransferFunction = 'PiecewiseFunction'
plt00050Display.DataAxesGrid = 'GridAxesRepresentation'
plt00050Display.PolarAxes = 'PolarAxesRepresentation'
plt00050Display.ScalarOpacityUnitDistance = 0.04436647145156464

# reset view to fit data
renderView1.ResetCamera()

# get the material library
materialLibrary1 = GetMaterialLibrary()

# update the view to ensure updated data information
renderView1.Update()

# change representation type
plt00050Display.SetRepresentationType('Surface')

# set scalar coloring
ColorBy(plt00050Display, ('CELLS', 'phi'))

# rescale color and/or opacity maps used to include current data range
plt00050Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
plt00050Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'phi'
phiLUT = GetColorTransferFunction('phi')

# get opacity transfer function/opacity map for 'phi'
phiPWF = GetOpacityTransferFunction('phi')

# create a new 'Slice'
slice1 = Slice(registrationName='Slice1', Input=plt00050)
slice1.SliceType = 'Plane'
slice1.HyperTreeGridSlicer = 'Plane'
slice1.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice1.SliceType.Origin = [0.5, 0.5, 0.0625]

# init the 'Plane' selected for 'HyperTreeGridSlicer'
slice1.HyperTreeGridSlicer.Origin = [0.5, 0.5, 0.0625]

# Properties modified on slice1.SliceType
slice1.SliceType.Normal = [0.0, 0.0, 1.0]

# show data in view
slice1Display = Show(slice1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
slice1Display.Representation = 'Surface'
slice1Display.ColorArrayName = ['CELLS', 'phi']
slice1Display.LookupTable = phiLUT
slice1Display.SelectTCoordArray = 'None'
slice1Display.SelectNormalArray = 'None'
slice1Display.SelectTangentArray = 'None'
slice1Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice1Display.SelectOrientationVectors = 'None'
slice1Display.ScaleFactor = 0.1
slice1Display.SelectScaleArray = 'None'
slice1Display.GlyphType = 'Arrow'
slice1Display.GlyphTableIndexArray = 'None'
slice1Display.GaussianRadius = 0.005
slice1Display.SetScaleArray = [None, '']
slice1Display.ScaleTransferFunction = 'PiecewiseFunction'
slice1Display.OpacityArray = [None, '']
slice1Display.OpacityTransferFunction = 'PiecewiseFunction'
slice1Display.DataAxesGrid = 'GridAxesRepresentation'
slice1Display.PolarAxes = 'PolarAxesRepresentation'

# hide data in view
Hide(plt00050, renderView1)

# show color bar/color legend
slice1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'XML Partitioned Polydata Reader'
ebpvtp = XMLPartitionedPolydataReader(registrationName='eb.pvtp', FileName=['eb.pvtp'])

# Properties modified on ebpvtp
ebpvtp.TimeArray = 'None'

# show data in view
ebpvtpDisplay = Show(ebpvtp, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
ebpvtpDisplay.Representation = 'Surface'
ebpvtpDisplay.ColorArrayName = [None, '']
ebpvtpDisplay.SelectTCoordArray = 'None'
ebpvtpDisplay.SelectNormalArray = 'None'
ebpvtpDisplay.SelectTangentArray = 'None'
ebpvtpDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
ebpvtpDisplay.SelectOrientationVectors = 'None'
ebpvtpDisplay.ScaleFactor = 0.019999998807907107
ebpvtpDisplay.SelectScaleArray = 'None'
ebpvtpDisplay.GlyphType = 'Arrow'
ebpvtpDisplay.GlyphTableIndexArray = 'None'
ebpvtpDisplay.GaussianRadius = 0.0009999999403953552
ebpvtpDisplay.SetScaleArray = [None, '']
ebpvtpDisplay.ScaleTransferFunction = 'PiecewiseFunction'
ebpvtpDisplay.OpacityArray = [None, '']
ebpvtpDisplay.OpacityTransferFunction = 'PiecewiseFunction'
ebpvtpDisplay.DataAxesGrid = 'GridAxesRepresentation'
ebpvtpDisplay.PolarAxes = 'PolarAxesRepresentation'

# update the view to ensure updated data information
renderView1.Update()

# create a new 'AMReX/BoxLib Particles Reader'
plt00050_1 = AMReXBoxLibParticlesReader(registrationName='plt00050', FileNames=['plt00050'])
plt00050_1.PointArrayStatus = ['id', 'cpu', 'real_comp0', 'real_comp1', 'real_comp2', 'real_comp3']

# show data in view
plt00050_1Display = Show(plt00050_1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
plt00050_1Display.Representation = 'Surface'
plt00050_1Display.ColorArrayName = [None, '']
plt00050_1Display.SelectTCoordArray = 'None'
plt00050_1Display.SelectNormalArray = 'None'
plt00050_1Display.SelectTangentArray = 'None'
plt00050_1Display.OSPRayScaleArray = 'cpu'
plt00050_1Display.OSPRayScaleFunction = 'PiecewiseFunction'
plt00050_1Display.SelectOrientationVectors = 'None'
plt00050_1Display.ScaleFactor = 0.05042795565134475
plt00050_1Display.SelectScaleArray = 'None'
plt00050_1Display.GlyphType = 'Arrow'
plt00050_1Display.GlyphTableIndexArray = 'None'
plt00050_1Display.GaussianRadius = 0.0025213977825672374
plt00050_1Display.SetScaleArray = ['POINTS', 'cpu']
plt00050_1Display.ScaleTransferFunction = 'PiecewiseFunction'
plt00050_1Display.OpacityArray = ['POINTS', 'cpu']
plt00050_1Display.OpacityTransferFunction = 'PiecewiseFunction'
plt00050_1Display.DataAxesGrid = 'GridAxesRepresentation'
plt00050_1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
plt00050_1Display.ScaleTransferFunction.Points = [-2147483646.0, 0.0, 0.5, 0.0, 2130706435.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
plt00050_1Display.OpacityTransferFunction.Points = [-2147483646.0, 0.0, 0.5, 0.0, 2130706435.0, 1.0, 0.5, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(plt00050_1Display, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
plt00050_1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'vtkBlockColors'
vtkBlockColorsLUT = GetColorTransferFunction('vtkBlockColors')

# get opacity transfer function/opacity map for 'vtkBlockColors'
vtkBlockColorsPWF = GetOpacityTransferFunction('vtkBlockColors')

# create a new 'Glyph'
glyph1 = Glyph(registrationName='Glyph1', Input=plt00050_1,
    GlyphType='Arrow')
glyph1.OrientationArray = ['POINTS', 'No orientation array']
glyph1.ScaleArray = ['POINTS', 'No scale array']
glyph1.ScaleFactor = 0.05042795565134475
glyph1.GlyphTransform = 'Transform2'

# hide data in view
Hide(plt00050_1, renderView1)

# Properties modified on glyph1
glyph1.GlyphType = 'Sphere'
glyph1.ScaleFactor = 0.009077032017242056
glyph1.GlyphMode = 'Every Nth Point'
glyph1.Stride = 100

# show data in view
glyph1Display = Show(glyph1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
glyph1Display.Representation = 'Surface'
glyph1Display.ColorArrayName = [None, '']
glyph1Display.SelectTCoordArray = 'None'
glyph1Display.SelectNormalArray = 'Normals'
glyph1Display.SelectTangentArray = 'None'
glyph1Display.OSPRayScaleArray = 'Normals'
glyph1Display.OSPRayScaleFunction = 'PiecewiseFunction'
glyph1Display.SelectOrientationVectors = 'None'
glyph1Display.ScaleFactor = 0.05095917880535126
glyph1Display.SelectScaleArray = 'None'
glyph1Display.GlyphType = 'Arrow'
glyph1Display.GlyphTableIndexArray = 'None'
glyph1Display.GaussianRadius = 0.002547958940267563
glyph1Display.SetScaleArray = ['POINTS', 'Normals']
glyph1Display.ScaleTransferFunction = 'PiecewiseFunction'
glyph1Display.OpacityArray = ['POINTS', 'Normals']
glyph1Display.OpacityTransferFunction = 'PiecewiseFunction'
glyph1Display.DataAxesGrid = 'GridAxesRepresentation'
glyph1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
glyph1Display.ScaleTransferFunction.Points = [-0.9749279022216797, 0.0, 0.5, 0.0, 0.9749279022216797, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
glyph1Display.OpacityTransferFunction.Points = [-0.9749279022216797, 0.0, 0.5, 0.0, 0.9749279022216797, 1.0, 0.5, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(glyph1Display, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
glyph1Display.SetScalarBarVisibility(renderView1, True)

# turn off scalar coloring
ColorBy(glyph1Display, None)

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(vtkBlockColorsLUT, renderView1)

# get color legend/bar for phiLUT in view renderView1
phiLUTColorBar = GetScalarBar(phiLUT, renderView1)

# change scalar bar placement
phiLUTColorBar.WindowLocation = 'AnyLocation'
phiLUTColorBar.Position = [0.8640054127198917, 0.12100611828687968]
phiLUTColorBar.ScalarBarLength = 0.33

# get layout
layout1 = GetLayout()

# layout/tab size in pixels
layout1.SetSize(1478, 1471)

# current camera placement for renderView1
renderView1.CameraPosition = [1.1119917869852012, 0.5834022145841244, 2.734750929884983]
renderView1.CameraFocalPoint = [0.4999999999999997, 0.4999999999999997, 0.062499999999999986]
renderView1.CameraViewUp = [-0.009868453339547676, 0.9995325562417275, -0.028935836631468405]
renderView1.CameraParallelScale = 0.7098635432250342

# save animation
SaveScreenshot('test_img.png', renderView1, ImageResolution=[1478, 1471])

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1478, 1471)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [1.1119917869852012, 0.5834022145841244, 2.734750929884983]
renderView1.CameraFocalPoint = [0.4999999999999997, 0.4999999999999997, 0.062499999999999986]
renderView1.CameraViewUp = [-0.009868453339547676, 0.9995325562417275, -0.028935836631468405]
renderView1.CameraParallelScale = 0.7098635432250342

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
