"""
Unit tests for HydroSense-Kenya numerical methods module.
Student: ELPIS MWANGI MAINA (SCT211-0003/2024)

Tests for RootFinding, NumericalDifferentiation, NumericalIntegration, 
LinearSystems, and IrrigationOptimization classes.
"""

import pytest
import numpy as np
import sys
sys.path.insert(0, '../src')
from numerical_methods import (RootFinding, NumericalDifferentiation, 
                              NumericalIntegration, LinearSystems, 
                              IrrigationOptimization)


class TestRootFinding:
    """Test root finding methods"""
    
    def test_bisection_linear_function(self):
        """Test bisection on f(x) = x - 5"""
        def f(x):
            return x - 5
        
        result = RootFinding.bisection(f, 0, 10)
        assert result['converged'] == True
        assert abs(result['root'] - 5.0) < 1e-5
        assert result['iterations'] < 30
    
    def test_bisection_quadratic_function(self):
        """Test bisection on f(x) = x^2 - 4"""
        def f(x):
            return x**2 - 4
        
        result = RootFinding.bisection(f, 0, 5)
        assert result['converged'] == True
        assert abs(result['root'] - 2.0) < 1e-5
    
    def test_bisection_exponential(self):
        """Test bisection on f(x) = e^x - 10"""
        def f(x):
            return np.exp(x) - 10
        
        result = RootFinding.bisection(f, 0, 5)
        assert result['converged'] == True
        assert abs(result['root'] - np.log(10)) < 1e-5
    
    def test_newton_raphson_linear(self):
        """Test Newton-Raphson on f(x) = x - 5"""
        def f(x):
            return x - 5
        def df(x):
            return 1
        
        result = RootFinding.newton_raphson(f, df, x0=0)
        assert result['converged'] == True
        assert abs(result['root'] - 5.0) < 1e-6
        assert result['iterations'] < 10
    
    def test_newton_raphson_quadratic(self):
        """Test Newton-Raphson on f(x) = x^2 - 9"""
        def f(x):
            return x**2 - 9
        def df(x):
            return 2*x
        
        result = RootFinding.newton_raphson(f, df, x0=5)
        assert result['converged'] == True
        assert abs(result['root'] - 3.0) < 1e-6
    
    def test_secant_method(self):
        """Test secant method on f(x) = x^3 - 2"""
        def f(x):
            return x**3 - 2
        
        result = RootFinding.secant(f, 1, 2)
        assert result['converged'] == True
        assert abs(result['root'] - 2**(1/3)) < 1e-5
    
    def test_bisection_irrigation_problem(self):
        """Test bisection on actual irrigation water balance"""
        def water_balance(irrigation):
            S_current = 28
            rainfall = 5
            ET = 2.5
            target = 35
            available = S_current + rainfall + irrigation
            drainage = 0.18 * max(0, available - 45)
            S_next = available - ET - drainage
            return S_next - target
        
        result = RootFinding.bisection(water_balance, 0, 50)
        assert result['converged'] == True
        assert result['root'] > 0
        assert result['root'] < 50


class TestNumericalDifferentiation:
    """Test numerical differentiation methods"""
    
    def test_forward_difference_linear(self):
        """Test forward difference on f(x) = 2x + 3"""
        def f(x):
            return 2*x + 3
        
        df = NumericalDifferentiation.forward_difference(f, 5.0)
        assert abs(df - 2.0) < 1e-4
    
    def test_backward_difference_linear(self):
        """Test backward difference on f(x) = 3x"""
        def f(x):
            return 3*x
        
        df = NumericalDifferentiation.backward_difference(f, 5.0)
        assert abs(df - 3.0) < 1e-4
    
    def test_central_difference_quadratic(self):
        """Test central difference on f(x) = x^2"""
        def f(x):
            return x**2
        
        # At x=3, df/dx should be 6
        df = NumericalDifferentiation.central_difference(f, 3.0)
        assert abs(df - 6.0) < 1e-4
    
    def test_central_difference_cubic(self):
        """Test central difference on f(x) = x^3"""
        def f(x):
            return x**3
        
        # At x=2, df/dx should be 12
        df = NumericalDifferentiation.central_difference(f, 2.0)
        assert abs(df - 12.0) < 1e-3
    
    def test_central_difference_more_accurate(self):
        """Test that central difference is more accurate than forward"""
        def f(x):
            return np.sin(x)
        
        x = np.pi / 4
        exact_df = np.cos(x)
        
        df_forward = NumericalDifferentiation.forward_difference(f, x)
        df_central = NumericalDifferentiation.central_difference(f, x)
        
        # Central should be closer to exact
        assert abs(df_central - exact_df) < abs(df_forward - exact_df)


class TestNumericalIntegration:
    """Test numerical integration methods"""
    
    def test_trapezoidal_linear(self):
        """Test trapezoidal rule on f(x) = x from 0 to 10"""
        def f(x):
            return x
        
        result = NumericalIntegration.trapezoidal(f, 0, 10, n=100)
        # Integral of x from 0 to 10 is 50
        assert abs(result - 50.0) < 1.0
    
    def test_trapezoidal_constant(self):
        """Test trapezoidal rule on f(x) = 5 from 0 to 20"""
        def f(x):
            return 5
        
        result = NumericalIntegration.trapezoidal(f, 0, 20, n=100)
        # Integral of 5 from 0 to 20 is 100
        assert abs(result - 100.0) < 0.1
    
    def test_simpson_constant(self):
        """Test Simpson's rule on constant function"""
        def f(x):
            return 3
        
        result = NumericalIntegration.simpson(f, 0, 10, n=100)
        # Integral should be 30
        assert abs(result - 30.0) < 0.1
    
    def test_simpson_linear(self):
        """Test Simpson's rule on linear function"""
        def f(x):
            return 2*x
        
        result = NumericalIntegration.simpson(f, 0, 10, n=100)
        # Integral of 2x from 0 to 10 is 100
        assert abs(result - 100.0) < 0.5
    
    def test_simpson_quadratic(self):
        """Test Simpson's rule on quadratic (exact for degree 3)"""
        def f(x):
            return x**2
        
        result = NumericalIntegration.simpson(f, 0, 10, n=100)
        # Integral of x^2 from 0 to 10 is 1000/3
        assert abs(result - 1000/3) < 1.0
    
    def test_simpson_more_accurate_than_trap(self):
        """Test that Simpson's is more accurate than trapezoidal"""
        def f(x):
            return np.sin(x)
        
        trap_result = NumericalIntegration.trapezoidal(f, 0, np.pi, n=100)
        simp_result = NumericalIntegration.simpson(f, 0, np.pi, n=100)
        
        # Integral of sin from 0 to pi is 2
        exact = 2.0
        assert abs(simp_result - exact) < abs(trap_result - exact)


class TestLinearSystems:
    """Test linear system solver"""
    
    def test_gaussian_elimination_2x2(self):
        """Test 2x2 system"""
        A = np.array([[2, 1], [1, 3]])
        b = np.array([5, 6])
        
        x = LinearSystems.gaussian_elimination(A, b)
        
        # Verify solution
        residual = np.linalg.norm(A @ x - b)
        assert residual < 1e-10
    
    def test_gaussian_elimination_3x3(self):
        """Test 3x3 system"""
        A = np.array([[1, 2, 3], [2, -1, 1], [1, 1, -1]])
        b = np.array([14, 5, 2])
        
        x = LinearSystems.gaussian_elimination(A, b)
        
        # Verify solution
        residual = np.linalg.norm(A @ x - b)
        assert residual < 1e-10
    
    def test_gaussian_elimination_identity(self):
        """Test identity matrix"""
        A = np.eye(3)
        b = np.array([1, 2, 3])
        
        x = LinearSystems.gaussian_elimination(A, b)
        
        # Solution should be same as b
        assert np.allclose(x, b)
    
    def test_gaussian_elimination_water_allocation(self):
        """Test actual water allocation problem"""
        A = np.array([[1.0, 1.0, 1.0],
                     [2.0, 1.5, 1.0],
                     [1.0, 2.0, 3.0]])
        b = np.array([500.0, 800.0, 1100.0])
        
        x = LinearSystems.gaussian_elimination(A, b)
        
        # Verify solution
        residual = np.linalg.norm(A @ x - b)
        assert residual < 1e-8
        
        # Solution should be non-negative (physical constraint)
        assert np.all(x >= 0)
    
    def test_gaussian_elimination_singular_detection(self):
        """Test detection of singular matrix"""
        A = np.array([[1, 2], [2, 4]])  # Linearly dependent rows
        b = np.array([3, 6])
        
        with pytest.raises(ValueError):
            LinearSystems.gaussian_elimination(A, b)


class TestIrrigationOptimization:
    """Test irrigation optimization"""
    
    def test_irrigation_to_target_simple(self):
        """Test irrigation calculation to reach target"""
        irrigation = IrrigationOptimization.irrigation_to_target(
            S_current=28, rainfall=5, ET=2.5, 
            target_moisture=35, field_capacity=45, drainage_coeff=0.18
        )
        
        # Should need positive irrigation
        assert irrigation > 0
        assert irrigation < 100
    
    def test_irrigation_already_at_target(self):
        """Test when already at target"""
        irrigation = IrrigationOptimization.irrigation_to_target(
            S_current=35, rainfall=5, ET=2.5,
            target_moisture=32, field_capacity=45, drainage_coeff=0.18
        )
        
        # May need less irrigation
        assert irrigation >= 0
    
    def test_irrigation_high_rainfall(self):
        """Test with high rainfall"""
        irrigation = IrrigationOptimization.irrigation_to_target(
            S_current=28, rainfall=20, ET=2.5,
            target_moisture=35, field_capacity=45, drainage_coeff=0.18
        )
        
        # Should need less irrigation with high rainfall
        assert irrigation >= 0


class TestEdgeCases:
    """Test edge cases and boundary conditions"""
    
    def test_division_by_zero_protection(self):
        """Test that division by zero is handled"""
        def f(x):
            return x
        def df(x):
            return 0  # Derivative is zero
        
        result = RootFinding.newton_raphson(f, df, x0=1)
        # Should not crash, should return non-converged
        assert result['converged'] == False
    
    def test_negative_step_size_integration(self):
        """Test integration with negative direction"""
        def f(x):
            return x**2
        
        result_pos = NumericalIntegration.trapezoidal(f, 0, 10, n=100)
        result_neg = NumericalIntegration.trapezoidal(f, 10, 0, n=100)
        
        # Should have opposite signs
        assert result_pos * result_neg < 0
    
    def test_very_high_precision_requirement(self):
        """Test convergence with tight tolerance"""
        def f(x):
            return x - np.pi
        
        result = RootFinding.bisection(f, 0, 5, tolerance=1e-12)
        assert result['error'] < 1e-12
        assert abs(result['root'] - np.pi) < 1e-11


class TestIntegration:
    """Integration tests combining multiple components"""
    
    def test_full_water_balance_simulation(self):
        """Test complete water balance calculation"""
        # Simulate soil moisture for 10 days
        S = 35.0
        ET_daily = 2.5
        rainfall_daily = 5.0
        
        for day in range(10):
            # Simple water balance
            available = S + rainfall_daily
            drainage = 0.18 * max(0, available - 45)
            S = available - ET_daily - drainage
            S = max(0, min(100, S))
        
        # Should stabilize
        assert 20 < S < 40
    
    def test_optimization_convergence(self):
        """Test that optimization finds reasonable solution"""
        # Find irrigation to maintain 30% moisture
        irrigation = IrrigationOptimization.irrigation_to_target(
            S_current=25, rainfall=3, ET=3.5,
            target_moisture=30, field_capacity=45, drainage_coeff=0.18
        )
        
        # Verify result by simulating forward
        available = 25 + 3 + irrigation
        drainage = 0.18 * max(0, available - 45)
        S_next = available - 3.5 - drainage
        
        # Should be close to target
        assert abs(S_next - 30) < 1


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
