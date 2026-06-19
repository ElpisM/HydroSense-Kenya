# Convergence Comparison: Root Finding Methods

**Student:** ELPIS MWANGI MAINA | SCT211-0003/2024

**Problem:** Find irrigation I such that soil moisture reaches 35%
(Current S=28%, Rainfall=5mm, ET=2.5mm, FC=45%, drainage=0.18)

## Results

| Method | Iterations | Error | Time (μs) | Root (mm) |
|--------|-----------|-------|-----------|-----------|
| Bisection | 24 | 1.2e-7 | 45–60 | 12.5432 |
| Newton-Raphson | 5 | 3.4e-8 | 15–25 | 12.5433 |
| Secant | 6 | 8.9e-8 | 18–28 | 12.5432 |

**Speedup vs Bisection:** Newton-Raphson 2.3x, Secant 1.8x

## Method Summary

| Method | Convergence Rate | Pros | Cons |
|--------|-----------------|------|------|
| Bisection | Linear | Guaranteed, robust | Slow, needs bracket |
| Newton-Raphson | Quadratic | Fastest | Needs derivative, can diverge |
| Secant | Superlinear (~1.618) | No derivative needed | Can diverge |

## Recommendation
- **Real-time systems:** Newton-Raphson (derivative available analytically)
- **No derivative available:** Secant
- **Guaranteed convergence needed:** Bisection
