# Numerical Reliability Discussion

**Student:** ELPIS MWANGI MAINA | SCT211-0003/2024

## Key Insights

### Vectorization
NumPy provides 100–120x speedup over Python loops — not from approximation, but from C-level execution and optimised memory access. Enables real-time analysis and practical Monte Carlo at scale.

### Floating Point Precision
- 30-day accumulated error: 0.3–0.4% soil moisture — measurable but acceptable
- Measurement error (sensors) dominates over numerical precision error
- Longer simulations accumulate proportionally more error (linear growth)

### Error Hierarchy
| Source | Magnitude | Priority |
|--------|-----------|----------|
| Temperature sensor (±2°C) | 0.35–0.45% moisture | **Highest** |
| Numerical precision | 0.3–0.4% moisture | Medium |
| Humidity sensor (±5%) | 0.02–0.08% moisture | Lowest |

**Conclusion:** Improving sensor accuracy matters more than improving numerical precision.

## Best Practices

1. **Quantify error sources** — know which variable drives uncertainty
2. **Use vectorization** — efficiency without sacrificing accuracy
3. **Include safety margins** — 5% buffer in irrigation recommendations
4. **Validate against field data** — model errors > numerical errors
5. **Document assumptions** — soil uniformity, fixed parameters, data gaps
6. **Match precision to measurement** — no point computing to 10 decimal places if sensors are ±1mm

## For HydroSense-Kenya
- Use NumPy for all computation
- Invest in accurate temperature sensors (highest sensitivity)
- Calibrate model regularly against field measurements
- Combine automated suggestions with farmer judgment
