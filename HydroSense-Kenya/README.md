# HydroSense-Kenya: Smart Irrigation System

**Student:** ELPIS MWANGI MAINA | SCT211-0003/2024
**Course:** ICS 2207 Scientific Computing (JKUAT) | June 2026

**Key Achievement:** 45% water reduction with <2% yield loss through responsive irrigation scheduling.

---

## Problem
Kenya's semi-arid agriculture faces water scarcity. Traditional "always irrigate" practices waste water, while lack of decision support leaves farmers guessing.

## Solution
Six-layer scientific computing system:

| Layer | Focus |
|-------|-------|
| 1 | Problem framing, real Kenya data |
| 2 | Vectorization (100-120x speedup), error analysis |
| 3 | Root finding, integration, linear systems |
| 4 | Data cleaning, 5 scientific visualizations |
| 5 | Euler simulation, Monte Carlo (1000 scenarios), optimization |
| 6 | Integration, 50+ unit tests, documentation |

---

## Project Structure
```
HydroSense-Kenya/
├── data/raw/              # Original datasets
├── data/processed/        # Cleaned datasets
├── notebooks/             # Level 1-6 Jupyter notebooks
├── src/numerical_methods.py
├── tests/test_numerical_methods.py
├── reports/               # Final report and slides
├── docs/                  # Supporting analysis docs
├── outputs/               # Simulation result CSVs
├── README.md
├── requirements.txt
└── AI_USE_LOG.md
```

---

## Key Results

**Strategy Comparison:**

| Strategy | Water (mm) | Stress Days | Cost |
|----------|-----------|-------------|------|
| Conservative (5mm/day) | 150 | 0 | High |
| **Optimal (responsive)** | **82** | **2–3** | **Moderate** |
| Minimal (none) | 0 | 15+ | Very low |

**Numerical Methods:**

| Method | Iterations | Time (μs) | Convergence |
|--------|-----------|-----------|-------------|
| Bisection | 24 | 45–60 | Linear |
| Newton-Raphson | 5 | 15–25 | Quadratic (2.3x faster) |
| Secant | 6 | 18–28 | Superlinear |

**Monte Carlo (1000 scenarios):** Mean moisture 27.1% ± 2.3%, stress probability 15% (acceptable).

---

## Water Balance Model
```
S(t+1) = S(t) + R(t) + I(t) - ET(t) - D(t)
ET = max(0, 0.12*T + 0.35*W + 2.4*Solar - 0.025*H)
D  = 0.18 * max(0, S - FC)     # FC = 45%
```

## Optimization
Minimize total irrigation. Constraint: S > 25% for ≥95% of days.
**Solution:** Irrigate when S < 25%, skip after heavy rain.

---

## Quick Start
```bash
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
pytest tests/ -v
jupyter notebook  # open notebooks in order Level_1 → Level_6
```

```python
import sys; sys.path.insert(0, 'src')
from numerical_methods import IrrigationOptimization
irrigation = IrrigationOptimization.irrigation_to_target(
    S_current=28, rainfall=5, ET=2.5,
    target_moisture=35, field_capacity=45, drainage_coeff=0.18)
```

---

## Key Findings
1. Rainfall CV=1.8 — highly episodic, irrigation essential
2. Temperature–humidity correlation r=−0.78; ET ranges 1.2–6.8 mm/day
3. Crop stress thresholds: Tomato 27%, Kale 24%, Maize 20%
4. Optimal point: 82mm water, 2–3 stress days, 98–99% yield
5. Responsive monitoring unlocks 45% water savings

## Deployment Decision Rules
- S < 25% → Irrigate 6–8mm
- S > 35% → Skip
- 7-day forecast rain > 20mm → Skip
- Visible stress → Emergency irrigation

---

## References
- FAO Irrigation Paper 56 (Allen et al., 1998) — ET methodology
- Burden & Faires (2010) — Numerical Analysis
- Boyd & Vandenberghe (2004) — Convex Optimization

## AI Usage
See AI_USE_LOG.md. AI used for code scaffolding only; all analysis 100% human.
