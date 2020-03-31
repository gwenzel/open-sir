import numpy as np # Numerical computing
from scipy.integrate import odeint # ODE system numerical integrator

ABSERR = 1.0e-8
RELERR = 1.0e-6
SECS=7*3600*24
NUMPOINTS=250

def sir(w, t, p):
    """ SIR: Simple model of disease spread
    inputs:
    w: vector of state variables [S,I,R]
    where 
        S: Fraction of the population susceptible to the infection
        I: Fraction on the population infected
        R: Fraction of the population recovered
    t: Current time
    p: vector of parameters
    
    returns:
    f: right hand side of the system of differential equations
    """
    # Unpack state variables
    S, I, R = w
    # Unpack parameters
    alpha, beta = p
    dS_dt = -alpha*S*I
    dI_dt =  alpha*S*I - beta*I
    dR_dt = beta * I
    
    f = [dS_dt, dI_dt, dR_dt]
    return f


def sirx(w, t, p):
    """ SIR-X: Dynamic outbreaks with temporally increasing
    interventions
    
    inputs:
    w: vector of state variables [S,I,R,X]
    where 
        S: Fraction of the population susceptible to the infection
        I: Fraction on the population infected
        R: Fraction of the population that recovered
        X: Fraction of the population that is quarantined
        
    t: time
    p: vector of parameters
    
    returns:
    f: right hand side of the system of differential equations
    """
    # Unpack state variables
    S, I, R, X = w
    # Unpack parameters
    alpha, beta, kappa_0, kappa = p
    dS_dt = -alpha*S*I - kappa_0*S
    dI_dt =  alpha*S*I - beta*I - kappa_0*I - kappa*I
    dR_dt = kappa_0*S + beta * I
    dX_dt = (kappa_0 + kappa) * I
    
    
    f = [dS_dt, dI_dt, dR_dt, dX_dt]
    return f


def _solve(func, p, w0, t, numpoints):
    # Call the ODE solver.
    """
    
    The integrating routine *odeint* requires for parameters that were previously defined:
    * func: function to be integrated.
    * y0: vector of initial conditions of the state variables.
    * t: discrete time-steps where the solution is going to be evaluated.
    * args = (): Extra arguments to pass to function. In our case, is the vector of parameters **p**
    """
    sol = odeint(func, w0, t, args=(p,), atol=ABSERR, rtol=RELERR)
    return np.insert(sol, 0, t, axis=1)


def solve_sir(p, w0, t=SECS, numpoints=NUMPOINTS):
    """ Solve the SIR system for given parameters and initial conditions.

    inputs:
    p: vector of parameters [alpha, beta]
    w0: initial conditions [S0, I0, R0]
    secs: number of seconds to simulate
    numpoints: number of points.
    """
    return _solve(sir, p, w0, t, numpoints)


def solve_sirx(p, w0, t=SECS, numpoints=NUMPOINTS):
    """ Solve the SIR-X system for given parameters and initial conditions.

    inputs:
    p: vector of parameters [alpha, beta, kappa_0, kappa]
    w0: initial conditions [S0, I0, R0, X0]
    secs: number of seconds to simulate
    numpoints: number of points.
    """
    return _solve(sirx, p, w0, t, numpoints)