from proteus import *
from proteus.default_p import *
from beach_erosion_board_waves_3d import *
from proteus import VANS2P
from proteus.mprans import RANS2P#RANS2PV2
from proteus.mprans import VRANS2P
"""
Two-phase incompressible Navier-Stokes flow of air and water in a perturbed box
"""

## \page Tests Test Problems
#\ref twp_navier_stokes_ls_so_sloshbox_3d_p.py "Two-phase incompressible Navier-Stokes flow of air and water in a perturbed box"
# 

##\ingroup test
# \file twp_navier_stokes_ls_so_sloshbox_3d_p.py
# @{
#
# \brief Two-phase incompressible Navier-Stokes flow of air and water in a perturbed box
#
# The governing equations are described by the
# proteus::TransportCoefficients::TwophaseNavierStokes_LS_SO class. The
# domain is the unit square. The boundary conditions are slip and no
# flow on the whole boundary. The pressure is set (arbitrarily) to
# zero at the node in the top right corner. The free surface is
# initially described by the line
#\f[
#(\frac{1}{2}-x_0)\sin(\theta)+(y-y_0)\cos(\theta) = 0
#\f]
#where \f$\tan(\theta)\f$ is the slope of the free surface and and \f$(x_0,y_0)\f$ is a point on the free surface
# 
#\image html sloshbox_1.jpg
#\image html sloshbox_2.jpg
#
# <A href="https://adh.usace.army.mil/proteus-images/sloshbox.avi"> AVI Animation of velocity and pressure </A>
#
# <A href="https://adh.usace.army.mil/proteus-images/sloshbox_adh.avi"> AVI Animation of Richard Stockstill's moving mesh simulation with ADH</A>
#
if useVANS2P:
    #LevelModelType = VANS2P.OneLevelVANS2P
    #LevelModelType = RANS2PV2.OneLevelRANS2PV2
    #LevelModelType = RANS2P.LevelModel
    LevelModelType = VRANS2P.LevelModel
 

#coefficients = VolumeAveragedTwophaseNavierStokes(epsFact=epsFact_viscosity,
coefficients = VRANS2P.Coefficients(epsFact=epsFact_viscosity,
                                                sigma=sigma_01,
                                                rho_0 = rho_0,
                                                nu_0 = nu_0,
                                                rho_1 = rho_1,
                                                nu_1 = nu_1,
                                                g=g,
                                                nd=nd,
                                                LS_model=1,
                                                epsFact_density=epsFact_density,
                                                stokes=useStokes,
                                                sd = True,
                                                #turbulenceClosureFlag=turbulenceClosureFlag,
                                                #smagorinskyConstant_0=smagorinskyConstant_0,
                                                #smagorinskyConstant_1=smagorinskyConstant_1,
                                                setParamsFunc=spongeLayerFunc,
                                                meanGrainSize=spongeGrainSize,
                                                porosityTypes=porosityTypes,
                                                meanGrainSizeTypes=meanGrainSizeTypes,
                                                killNonlinearDrag = killNonlinearDragInSpongeLayer,
                                                waveFlag=waveFlag,
                                                waveHeight=waveHeight,
                                                waveCelerity=waveCelerity,
                                                waveFrequency=waveFrequency,
                                                waveNumber=waveNumber,
                                                waterDepth=waterLevelBase,
                                                Omega_s=Omega_s,
                                                epsFact_source=epsFact_source)



dirichletConditions = dirichletConditions_ns
fluxBoundaryConditions = fluxBoundaryConditions_ns
advectiveFluxBoundaryConditions = advectiveFluxBoundaryConditions_ns
diffusiveFluxBoundaryConditions = diffusiveFluxBoundaryConditions_ns
initialConditions = initialConditions_ns

