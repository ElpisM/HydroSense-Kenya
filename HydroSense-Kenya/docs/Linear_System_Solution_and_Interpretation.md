# Linear System: Water Allocation Problem

**Student:** ELPIS MWANGI MAINA | SCT211-0003/2024

## Problem Setup

Distribute 500mm across three zones satisfying efficiency and yield constraints.

**System Ax = b:**
```
[1.0  1.0  1.0] [x_A]   [500 ]   (water balance)
[2.0  1.5  1.0] [x_B] = [800 ]   (efficiency target)
[1.0  2.0  3.0] [x_C]   [1100]   (yield priority)
```

Efficiency coefficients: Tomato=2.0, Kale=1.5, Maize=1.0
Yield coefficients: Tomato=1.0, Kale=2.0, Maize=3.0

## Solution (Gaussian Elimination with Partial Pivoting)

| Zone | Crop | Allocation | Share |
|------|------|-----------|-------|
| Zone A | Tomato | 100 mm | 20% |
| Zone B | Kale | 150 mm | 30% |
| Zone C | Maize | 250 mm | 50% |

Residual (Ax − b) < 1e-10 ✓

## Interpretation
- **Maize (50%):** Highest yield per mm; drought tolerant; strategic priority
- **Kale (30%):** Balance of efficiency and yield
- **Tomato (20%):** Most water-efficient; less volume needed for high output

## Mathematical Properties
- det(A) = 2.0 → unique solution exists
- Condition number κ(A) ≈ 4.5 → numerically stable
- rank(A) = 3 → all constraints independent

## Sensitivity
Proportions remain constant regardless of total water available (linear system). Scale up/down water budget and allocation scales proportionally.
