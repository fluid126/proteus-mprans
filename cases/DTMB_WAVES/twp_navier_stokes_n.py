from proteus import *
from proteus.default_n import *
from DTMB import *
from twp_navier_stokes_p import *

timeIntegration = BackwardEuler_cfl
stepController = FixedStep
                     
femSpaces = {0:C0_AffineLinearOnSimplexWithNodalBasis,
             1:C0_AffineLinearOnSimplexWithNodalBasis,
             2:C0_AffineLinearOnSimplexWithNodalBasis,
             3:C0_AffineLinearOnSimplexWithNodalBasis}

elementQuadrature = SimplexGaussQuadrature(nd,quad_order)
elementBoundaryQuadrature = SimplexGaussQuadrature(nd-1,quad_order)

subgridError = NavierStokesASGS_velocity_pressure_opt(coefficients,nd,lag=False,delayLagSteps=1,hFactor=1.0)

numericalFluxType = NavierStokes_Advection_DiagonalUpwind_Diffusion_SIPG_exterior #need weak for parallel and global conservation

massLumping = False

shockCapturing = NavierStokes_SC_opt(coefficients,nd,ns_shockCapturingFactor,lag=False)


multilevelNonlinearSolver  = NewtonNS
levelNonlinearSolver = NewtonNS

maxNonlinearIts = 10
maxLineSearches = 0

nonlinearSmoother = None

fullNewtonFlag = True

tolFac = 1e-3

nl_atol_res = 0.0

matrix = SparseMatrix

multilevelLinearSolver = PETSc
levelLinearSolver = PETSc
linear_solver_options_prefix = 'rans2p_'
linearSmoother=None

nonlinearSolverConvergenceTest = 'rits'
levelNonlinearSolverConvergenceTest = 'rits'

linTolFac = 0.001

