from proteus import *
from proteus.default_n import *
from curvature_beach_erosion_board_waves_3d_p import *
from beach_erosion_board_waves_3d import *

timeIntegration = NoIntegration
#timeIntegration = PsiTCtte
timeIntegrator = SteadyStateIntegrator
#DT = None

femSpaces = {0:C0_AffineLinearOnSimplexWithNodalBasis}
#femSpaces = {0:DG_AffineP0_OnSimplexWithMonomialBasis}

elementQuadrature = SimplexGaussQuadrature(nd,sloshbox_quad_order)

elementBoundaryQuadrature = SimplexGaussQuadrature(nd-1,sloshbox_quad_order)

#elementQuadrature = SimplexLobattoQuadrature(nd,1)
#
#elementBoundaryQuadrature = SimplexLobattoQuadrature(nd-1,1)

subgridError = None
shockCapturing = None
massLumping = False
reactionLumping=False
numericalFluxType = None
#numericalFluxType = Advection_Diagonal_average
#numericalFluxType = Advection_DiagonalUpwind_Diffusion_IIPG_exterior
numericalFluxType = Curvature_exterior
multilevelNonlinearSolver  = Newton
fullNewtonFlag = False
tolFac = 0.0
nl_atol_res = 1.0e-8 #1e-4
maxNonlinearIts = 100
matrix = SparseMatrix
if usePETSc:
    multilevelLinearSolver = PETSc
    levelLinearSolver = PETSc
    nLayersOfOverlapForParallel = nOverlap#2
    parallelPartitioningType = partitioningType#MeshParallelPartitioningTypes.node
    #parallelPartitioningType = MeshParallelPartitioningTypes.element
else:
    multilevelLinearSolver = LU
    levelLinearSolver = LU

linTolFac = 0.001
conservativeFlux = None
