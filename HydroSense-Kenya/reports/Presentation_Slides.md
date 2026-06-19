# HydroSense-Kenya: Capstone Presentation

**ELPIS MWANGI MAINA | SCT211-0003/2024 | ICS 2207 JKUAT**

---

## Slide 1: Problem
Water scarcity threatens Kenyan semi-arid agriculture. Farmers use inefficient "always irrigate" approach — wasting water, high cost, no science-based decision support.
**Goal:** Smart system that optimises water-yield trade-off.

---

## Slide 2: Solution — 6 Layers
| Layer | What | Key Result |
|-------|------|-----------|
| 1 | Problem framing, real Kenya data | Baseline established |
| 2 | Vectorization vs loops | 100–120x speedup |
| 3 | Root finding, integration, linear algebra | numerical_methods.py |
| 4 | Data cleaning + 5 visualizations | Patterns identified |
| 5 | Simulation + Monte Carlo + optimization | Optimal schedule found |
| 6 | Integration + 50+ tests | Deployable system |

---

## Slide 3: Key Innovation
Rather than choosing water conservation **OR** crop health — find the **efficient frontier where both improve together** through responsive, data-driven irrigation.

---

## Slide 4: Results

| Strategy | Water | Stress Days | Yield | Cost |
|----------|-------|-------------|-------|------|
| Conservative | 150mm | 0 | 100% | High |
| **Optimal** | **82mm** | **2–3** | **98–99%** | **~50% less** |
| Minimal | 0mm | 15+ | 30–50% | Very low |

---

## Slide 5: Algorithms

| Method | Iterations | Time (μs) | Rate |
|--------|-----------|-----------|------|
| Bisection | 24 | 45–60 | Linear |
| Newton-Raphson | 5 | 15–25 | Quadratic (2.3x faster) |
| Secant | 6 | 18–28 | Superlinear |

Simpson's integration converges at O(h⁴) vs Trapezoidal O(h²).

---

## Slide 6: Data Findings
- Rainfall CV=1.8 — episodic, irrigation essential
- Temperature–humidity: r=−0.78 (hot days = dry = high ET)
- Crop stress thresholds: Tomato 27%, Kale 24%, Maize 20%
- ET range: 1.2–6.8 mm/day

---

## Slide 7: Uncertainty
**Monte Carlo, 1000 scenarios:** Mean 27.1% ± 2.3%, stress probability 15% — manageable with monitoring.

---

## Slide 8: Farmer Decision Rules
1. Measure soil moisture 2×/week
2. **S < 25%** → Irrigate 6–8mm
3. **S > 35%** → Skip
4. 7-day forecast rain >20mm → Skip
5. Visible stress → Emergency irrigation
6. Record and adjust monthly

---

## Slide 9: Economics
- Investment: ~60,000–110,000 KES (sensor + infrastructure)
- Annual savings: ~20,000 KES (45% pumping reduction)
- Yield maintained: 98–99%
- **Payback: 3–4 years**

---

## Slide 10: Impact & Future
**Now:** 45% water reduction, <2% yield loss, deployable today.
**Next 2 years:** Field validation, mobile app, farmer training.
**Long-term:** Expand to multiple crops/regions, integrate forecasting, climate adaptation.

---

## Slide 11: Technical Summary
- **Code:** 400+ lines numerical methods, 50+ tests, >95% coverage
- **Documentation:** 6 notebooks, scientific report, AI log
- **Quality:** PEP 8, docstrings, type hints, all tests pass

---

## Slide 12: Key Takeaway
> Water conservation and crop health are not competing objectives — **intelligent responsive management enables both to improve together.**

---

## Technical Reference

**Water Balance:**
```
S(t+1) = S(t) + R(t) + I(t) - ET(t) - D(t)
ET = max(0, 0.12T + 0.35W + 2.4Solar - 0.025H)
D  = 0.18 * max(0, S - 45%)
```

**Optimization:**
```
Minimise: Σ I(t)
Subject to: S(t) > 25% for ≥95% of days, I(t) ≥ 0
```

**Data:** 30-day weather + 90 soil observations (3 zones). 4 anomalies resolved. 99.5% complete.

**Tests:** Root finding (12), differentiation (5), integration (6), linear systems (5), integration workflows (5+).
