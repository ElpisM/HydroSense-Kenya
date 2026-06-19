# HydroSense-Kenya: Final Scientific Report

**Student:** ELPIS MWANGI MAINA | SCT211-0003/2024
**Course:** ICS 2207 Scientific Computing, JKUAT | June 2026

---

## Executive Summary

HydroSense-Kenya is a science-based irrigation optimization system combining numerical methods, data analysis, and stochastic simulation. Responsive irrigation scheduling reduces water use by **45%** while maintaining yield within **2%** of conservative strategies.

---

## 1. Introduction

Kenya's semi-arid agriculture faces water scarcity. Traditional irrigation has three failures: overwatering, poor timing, and no decision support. This project uses scientific computing to find the efficient frontier where water conservation and crop health improve together.

---

## 2. Methodology

### 2.1 Computational Layers

| Layer | Focus | Key Output |
|-------|-------|------------|
| 1 | Problem framing, Kenya data | Baseline model |
| 2 | Vectorization, error analysis | 100–120x speedup |
| 3 | Root finding, integration, linear systems | numerical_methods.py |
| 4 | Data cleaning, 5 visualizations | Cleaned datasets |
| 5 | Euler simulation, Monte Carlo, optimization | Optimal schedule |
| 6 | Integration, 50+ tests, documentation | Deployable system |

### 2.2 Water Balance Model
```
S(t+1) = S(t) + R(t) + I(t) - ET(t) - D(t)
ET = max(0, 0.12*T + 0.35*W + 2.4*Solar - 0.025*H)
D  = 0.18 * max(0, S - FC)     # FC = 45%
```

### 2.3 Optimization
Minimize total irrigation subject to S > 25% for ≥95% of days.
Method: Parameterize I=[I₁..I₃₀], simulate forward, apply Nelder-Mead simplex.

---

## 3. Data

**Weather (30 days: Mar 4 – Apr 2, 2026):**
- Temperature: 18.2–45.8°C (mean 27.3°C)
- Rainfall: 0–85.4mm (mean 5.2mm, CV=1.8)
- Humidity: 35–95% (mean 65%)
- Wind: 0.5–4.5 m/s | Solar: 0.2–0.95

**Soil Sensors (90 observations, 3 zones × 30 days):**
- Zone A (Tomato): 28–35% | Zone B (Kale): 25–32% | Zone C (Maize): 20–28%

**Data Quality Issues Resolved:**
1. Missing rainfall day 8 → interpolated from neighbours
2. Temperature outlier 45.8°C → retained (physically plausible)
3. Missing Zone B moisture → interpolated within zone
4. Tank spike 9900L → capped at physical maximum

---

## 4. Results

### 4.1 Numerical Methods

| Method | Iterations | Error | Time (μs) |
|--------|-----------|-------|-----------|
| Bisection | 24 | 1.2e-7 | 45–60 |
| Newton-Raphson | 5 | 3.4e-8 | 15–25 |
| Secant | 6 | 8.9e-8 | 18–28 |

Integration (cumulative ET, 30 days): Trapezoidal O(h²) → 156.4mm; Simpson's O(h⁴) → 156.3mm at n=30.

### 4.2 Strategy Comparison

| Strategy | Water (mm) | Stress Days | Yield | Cost |
|----------|-----------|-------------|-------|------|
| Conservative | 150 | 0 | 100% | High |
| **Optimal** | **82** | **2–3** | **98–99%** | **~50% less** |
| Minimal | 0 | 15+ | 30–50% | Very low |

### 4.3 Monte Carlo (1000 scenarios)
- Mean final moisture: 27.1% ± 2.3%
- 95% CI: 22.6%–31.6%
- Stress probability: 15% (acceptable)

---

## 5. Key Findings

1. **Rainfall CV=1.8** — episodic, extended dry periods require irrigation
2. **ET range 1.2–6.8 mm/day** driven by T (0.12mm/°C), W (0.35mm/ms), Solar (2.4/index)
3. **Crop thresholds:** Tomato 27%, Kale 24%, Maize 20%
4. **Non-linear trade-off:** Conservative→Optimal saves 45% water for only 2–3 marginal stress days
5. **Monitoring enables efficiency:** Responsive management unlocks savings that static rules cannot

---

## 6. Limitations
- 30-day single season (multi-year would strengthen patterns)
- Single location (different rainfall = different schedule)
- Fixed crop parameters (no phenological variation)
- Simplified uniform soil model

---

## 7. Implementation

**Decision Rules:**
- S < 25% → Irrigate 6–8mm
- S > 35% → Skip
- 7-day forecast rain >20mm → Skip
- Visible stress → Emergency irrigation

**Cost-Benefit:**
- Sensor + infrastructure: ~60,000–110,000 KES
- Annual water savings: ~20,000 KES (45% pumping reduction)
- Payback: 3–4 years

---

## 8. Conclusions

1. Responsive scheduling achieves 45% water reduction with <2% yield loss
2. Numerical methods enable quantitative agricultural optimization
3. 15% stress probability is acceptable with monitoring
4. Smart agriculture requires information and decision-making, not just technology
5. Model applicable to thousands of Kenyan smallholder farmers

---

## References
- Allen et al. (1998). FAO Irrigation Paper 56 — ET methodology
- Burden & Faires (2010). Numerical Analysis (9th Ed.)
- Boyd & Vandenberghe (2004). Convex Optimization
- Nocedal & Wright (1999). Numerical Optimization
