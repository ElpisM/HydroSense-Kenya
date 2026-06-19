# Error Propagation Plot Analysis

**Student:** ELPIS MWANGI MAINA | SCT211-0003/2024

## Key Findings

**Plot 1: Standard vs Reduced Precision (30-day simulation)**
- Max cumulative error: 0.3–0.4% soil moisture (occurring ~day 25–30)
- Error accumulates gradually and approximately linearly

**Plot 2: Cumulative Precision Error Growth**
| Period | Error |
|--------|-------|
| Day 1–10 | <0.05% (negligible) |
| Day 11–20 | 0.05–0.2% (growing) |
| Day 21–30 | 0.2–0.4% (noticeable) |

## Measurement Error Sensitivity

| Variable | Perturbation | Moisture Error | Priority |
|----------|-------------|----------------|----------|
| Temperature | ±2°C | 0.35–0.45% | **High** |
| Rainfall | ±2mm | 0.05–0.15% | Medium |
| Humidity | ±5% | 0.02–0.08% | Low |

## Conclusions
- Measurement error dominates over numerical precision error — invest in accurate temperature sensors
- 0.4% error is acceptable for 30-day irrigation decisions; longer simulations accumulate proportionally more
- Include 5% safety margin in irrigation recommendations to account for uncertainty
- The 100x vectorization speedup allows real-time analysis without adding computational error
