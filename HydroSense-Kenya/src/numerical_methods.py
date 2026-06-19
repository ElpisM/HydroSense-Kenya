"""
HydroSense-Kenya Numerical Methods Engine
Student: ELPIS MWANGI MAINA
Student Number: SCT211-0003/2024

Core numerical methods for scientific computing and irrigation optimization.
Implements root finding, numerical integration, and linear system solving.
"""

import numpy as np
from typing import Tuple, Dict, Callable, List


class RootFinding:
    """Root finding methods for solving f(x) = 0"""
    
    @staticmethod
    def bisection(f: Callable, a: float, b: float, tolerance: float = 1e-6, 
                  max_iterations: int = 100) -> Dict:
        """
        Bisection method for root finding.
        
        Parameters:
            f: Function to find root of
            a, b: Interval [a, b] containing the root
            tolerance: Convergence tolerance
            max_iterations: Maximum iterations
        
        Returns:
            Dictionary with root, iterations, error, converged status
        """
        iterations = 0
        x_prev = None
        
        for i in range(max_iterations):
            x_mid = (a + b) / 2.0
            f_mid = f(x_mid)
            
            if f_mid == 0:
                return {
                    'root': x_mid,
                    'iterations': i + 1,
                    'error': 0.0,
                    'converged': True
                }
            
            if f(a) * f_mid < 0:
                b = x_mid
            else:
                a = x_mid
            
            if x_prev is not None:
                error = abs(x_mid - x_prev)
                if error < tolerance:
                    return {
                        'root': x_mid,
                        'iterations': i + 1,
                        'error': error,
                        'converged': True
                    }
            
            x_prev = x_mid
            iterations = i + 1
        
        return {
            'root': x_mid,
            'iterations': max_iterations,
            'error': abs(x_mid - x_prev) if x_prev else float('inf'),
            'converged': False
        }
    
    @staticmethod
    def newton_raphson(f: Callable, df: Callable, x0: float, tolerance: float = 1e-6,
                       max_iterations: int = 100) -> Dict:
        """
        Newton-Raphson method for root finding.
        
        Parameters:
            f: Function to find root of
            df: Derivative of f
            x0: Initial guess
            tolerance: Convergence tolerance
            max_iterations: Maximum iterations
        
        Returns:
            Dictionary with root, iterations, error, converged status
        """
        x = x0
        
        for i in range(max_iterations):
            fx = f(x)
            dfx = df(x)
            
            if abs(dfx) < 1e-14:
                return {
                    'root': x,
                    'iterations': i + 1,
                    'error': float('inf'),
                    'converged': False
                }
            
            x_new = x - fx / dfx
            error = abs(x_new - x)
            
            if error < tolerance:
                return {
                    'root': x_new,
                    'iterations': i + 1,
                    'error': error,
                    'converged': True
                }
            
            x = x_new
        
        return {
            'root': x,
            'iterations': max_iterations,
            'error': error,
            'converged': False
        }
    
    @staticmethod
    def secant(f: Callable, x0: float, x1: float, tolerance: float = 1e-6,
               max_iterations: int = 100) -> Dict:
        """
        Secant method for root finding.
        
        Parameters:
            f: Function to find root of
            x0, x1: Two initial points
            tolerance: Convergence tolerance
            max_iterations: Maximum iterations
        
        Returns:
            Dictionary with root, iterations, error, converged status
        """
        for i in range(max_iterations):
            f0 = f(x0)
            f1 = f(x1)
            
            if abs(f1 - f0) < 1e-14:
                return {
                    'root': x1,
                    'iterations': i + 1,
                    'error': float('inf'),
                    'converged': False
                }
            
            x_new = x1 - f1 * (x1 - x0) / (f1 - f0)
            error = abs(x_new - x1)
            
            if error < tolerance:
                return {
                    'root': x_new,
                    'iterations': i + 1,
                    'error': error,
                    'converged': True
                }
            
            x0 = x1
            x1 = x_new
        
        return {
            'root': x1,
            'iterations': max_iterations,
            'error': error,
            'converged': False
        }


class NumericalDifferentiation:
    """Numerical differentiation methods"""
    
    @staticmethod
    def forward_difference(f: Callable, x: float, h: float = 1e-5) -> float:
        """
        Forward difference approximation of derivative.
        f'(x) ≈ (f(x+h) - f(x)) / h
        """
        return (f(x + h) - f(x)) / h
    
    @staticmethod
    def backward_difference(f: Callable, x: float, h: float = 1e-5) -> float:
        """
        Backward difference approximation of derivative.
        f'(x) ≈ (f(x) - f(x-h)) / h
        """
        return (f(x) - f(x - h)) / h
    
    @staticmethod
    def central_difference(f: Callable, x: float, h: float = 1e-5) -> float:
        """
        Central difference approximation of derivative.
        f'(x) ≈ (f(x+h) - f(x-h)) / (2h)
        """
        return (f(x + h) - f(x - h)) / (2.0 * h)


class NumericalIntegration:
    """Numerical integration methods"""
    
    @staticmethod
    def trapezoidal(f: Callable, a: float, b: float, n: int = 100) -> float:
        """
        Trapezoidal rule for integration.
        Approximates area under curve with trapezoids.
        """
        h = (b - a) / n
        result = 0.5 * (f(a) + f(b))
        
        for i in range(1, n):
            x = a + i * h
            result += f(x)
        
        return result * h
    
    @staticmethod
    def simpson(f: Callable, a: float, b: float, n: int = 100) -> float:
        """
        Simpson's rule for integration.
        Uses parabolic approximations, more accurate than trapezoidal.
        """
        if n % 2 == 1:
            n += 1
        
        h = (b - a) / n
        result = f(a) + f(b)
        
        for i in range(1, n, 2):
            x = a + i * h
            result += 4.0 * f(x)
        
        for i in range(2, n, 2):
            x = a + i * h
            result += 2.0 * f(x)
        
        return result * h / 3.0


class LinearSystems:
    """Gaussian elimination for solving Ax = b"""
    
    @staticmethod
    def gaussian_elimination(A: np.ndarray, b: np.ndarray) -> np.ndarray:
        """
        Solve Ax = b using Gaussian elimination with partial pivoting.
        
        Parameters:
            A: Coefficient matrix (n x n)
            b: Right-hand side vector (n,)
        
        Returns:
            Solution vector x
        """
        n = len(b)
        
        # Create augmented matrix
        Ab = np.column_stack([A.astype(float), b.astype(float)])
        
        # Forward elimination with partial pivoting
        for i in range(n):
            # Find pivot
            max_row = i + np.argmax(np.abs(Ab[i:, i]))
            Ab[[i, max_row]] = Ab[[max_row, i]]
            
            # Check for zero pivot
            if abs(Ab[i, i]) < 1e-10:
                raise ValueError("Matrix is singular")
            
            # Eliminate column
            for j in range(i + 1, n):
                factor = Ab[j, i] / Ab[i, i]
                Ab[j, i:] -= factor * Ab[i, i:]
        
        # Back substitution
        x = np.zeros(n)
        for i in range(n - 1, -1, -1):
            x[i] = Ab[i, n]
            for j in range(i + 1, n):
                x[i] -= Ab[i, j] * x[j]
            x[i] /= Ab[i, i]
        
        return x


class IrrigationOptimization:
    """Optimization methods applied to irrigation problems"""
    
    @staticmethod
    def irrigation_to_target(S_current: float, rainfall: float, ET: float,
                           target_moisture: float, field_capacity: float,
                           drainage_coeff: float) -> float:
        """
        Calculate irrigation needed to reach target soil moisture.
        
        Solves: S_target = S_current + rainfall + irrigation - ET - drainage
        Using bisection method.
        """
        def water_balance(irrigation):
            available = S_current + rainfall + irrigation
            drainage = drainage_coeff * max(0, available - field_capacity)
            S_next = available - ET - drainage
            return S_next - target_moisture
        
        # Find irrigation amount
        result = RootFinding.bisection(water_balance, 0, 100)
        return max(0, result['root'])

