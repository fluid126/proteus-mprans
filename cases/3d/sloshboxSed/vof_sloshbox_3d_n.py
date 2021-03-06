from proteus import *
from proteus.default_n import *
from sloshbox3d import *
from vof_sloshbox_3d_p import *



timeIntegration = BackwardEuler_cfl
stepController=Min_dt_controller
if timeOrder == 2:
    timeIntegration = VBDF
    stepController = Min_dt_cfl_controller
#timeIntegration = BackwardEuler
#stepController=FixedStep
if useHex:
    if spaceOrder == 1:
        femSpaces = {0:C0_AffineLinearOnCubeWithNodalBasis}
    elif spaceOrder == 2:
        femSpaces = {0:C0_AffineLagrangeOnCubeWithNodalBasis}
    elementQuadrature = CubeGaussQuadrature(nd,sloshbox_quad_order)
    elementBoundaryQuadrature = CubeGaussQuadrature(nd-1,sloshbox_quad_order)
else:
    if spaceOrder == 1:
        femSpaces = {0:C0_AffineLinearOnSimplexWithNodalBasis}
    elif spaceOrder == 2:
        femSpaces = {0:C0_AffineQuadraticOnSimplexWithNodalBasis}
    elementQuadrature = SimplexGaussQuadrature(nd,sloshbox_quad_order)
    elementBoundaryQuadrature = SimplexGaussQuadrature(nd-1,sloshbox_quad_order)

shockCapturing = ResGradQuad_SC(coefficients,nd,shockCapturingFactor=vof_shockCapturingFactor,lag=True)#linear
subgridError = Advection_ASGS(coefficients=coefficients,nd=nd,lag=False)
massLumping = False
numericalFluxType = Advection_DiagonalUpwind_IIPG_exterior

# timeOrder=1
# nStagesTime = timeOrder
# class SSPRKwrap(LinearSSPRKintegration):
#     """
#     wrap SSPRK so default constructor uses
#     the order I want and runCFL without
#     changing VectorTransport
#     """
#     def __init__(self,vt):
#         LinearSSPRKintegration.__init__(self,vt,timeOrder,runCFL)
#         return
# timeIntegration = SSPRKwrap 
# stepController=Min_dt_RKcontroller
# femSpaces = {0:DG_AffineP0_OnSimplexWithMonomialBasis}
# subgridError = None
# numericalFluxType = Advection_DiagonalUpwind
# shockCapturing = None
# subgridError = None
# massLumping = False

multilevelNonlinearSolver  = Newton

levelNonlinearSolver = Newton

nonlinearSmoother = NLGaussSeidel

fullNewtonFlag = True

tolFac = 0.0

nl_atol_res = 1.0e-4#0.001*he#1.0e-4

levelNonlinearSolverConvergenceTest='rits'
maxNonlinearIts = 2#it's linear so if it needs more than one our linear solver is not working

matrix = SparseMatrix

multilevelLinearSolver = LU

levelLinearSolver = LU

if usePETSc:
    multilevelLinearSolver = KSP_petsc4py
    levelLinearSolver = KSP_petsc4py
    linear_solver_options_prefix = 'vof_'
    #linearSmoother = None
    linearSmoother = StarILU
    linearSolverConvergenceTest = 'r-true'

linTolFac = 0.001

conservativeFlux = None
