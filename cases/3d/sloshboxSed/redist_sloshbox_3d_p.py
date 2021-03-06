from proteus import *
from proteus.default_p import *
from math import *
from sloshbox3d import *
from proteus.mprans import RDLS
"""
The redistancing equation in the sloshbox test problem.
"""
##
LevelModelType = RDLS.LevelModel

##\ingroup test
#\brief The redistancing equation in the sloshbox test problem.
#
if applyCorrection:
    coefficients = RDLS.Coefficients(applyRedistancing=applyRedistancing,
                                      epsFact=epsFact_redistance,
                                      nModelId=1,
                                      rdModelId=3)
else:
    coefficients = RDLS.Coefficients(applyRedistancing=applyRedistancing,
                                      epsFact=epsFact_redistance,
                                      nModelId=1,
                                      rdModelId=2)

#now define the Dirichlet boundary conditions

def getDBC_rd(x,flag):
    pass
    
dirichletConditions = {0:getDBC_rd}

if freezeLevelSet:
    if LevelModelType == RDLS.LevelModel:
        #weakDirichletConditions = {0:RDLS.setZeroLSweakDirichletBCs}
        weakDirichletConditions = {0:RDLS.setZeroLSweakDirichletBCsSimple}
    else:
        weakDirichletConditions = {0:coefficients.setZeroLSweakDirichletBCs}


class PerturbedSurface_phi:
    def __init__(self,waterLevel,slopeAngle):
        self.waterLevel=waterLevel
        self.slopeAngle=slopeAngle
    def uOfXT(self,x,t):
        if useShock:
            return shockSignedDistance(x)
        else:
            surfaceNormal = [-sin(self.slopeAngle),cos(self.slopeAngle)]
            signedDistance = (x[0] - 0.5)*surfaceNormal[0]+(x[2] - self.waterLevel)*surfaceNormal[1]
            return signedDistance
    
initialConditions  = {0:PerturbedSurface_phi(waterLevel,slopeAngle)}

fluxBoundaryConditions = {0:'noFlow'}

advectiveFluxBoundaryConditions =  {}

diffusiveFluxBoundaryConditions = {0:{}}
