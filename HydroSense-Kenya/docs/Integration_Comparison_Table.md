# Integration Comparison: Numerical Integration Methods

**Student:** ELPIS MWANGI MAINA | SCT211-0003/2024

**Problem:** Cumulative ET over 30 days
`ET(day) = 0.12*T + 0.35*W + 2.4*Solar - 0.025*H`

## Results

| Method | n=10 | n=30 | n=100 | Convergence |
|--------|------|------|-------|-------------|
| Trapezoidal | 155.8 mm | 156.2 mm | 156.4 mm | O(h²) |
| Simpson's | 156.1 mm | 156.3 mm | 156.3 mm | O(h⁴) |

Simpson's converges by n=20; Trapezoidal still drifting at n=50.

## Efficiency Comparison

| Method | n=30 Time | Accuracy at n=30 | Cost/Accuracy |
|--------|-----------|-----------------|---------------|
| Trapezoidal | ~5 μs | ±0.2 mm | High (worse) |
| Simpson's | ~8 μs | ±0.0 mm | Low (better) |

Despite slightly higher per-call cost, Simpson's is more efficient for any given accuracy target due to 4th-order convergence.

## Recommendation
**Always use Simpson's rule.** Use n=10 for real-time, n=30 for daily planning, n=100 for archival records.
Trapezoidal only for non-smooth/discontinuous data or legacy systems.
