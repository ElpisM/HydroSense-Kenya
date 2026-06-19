# Visualization Interpretation Notes

**Student:** ELPIS MWANGI MAINA | SCT211-0003/2024

Five visualizations from Level_4_Data_Analysis_and_Visualization.ipynb.

---

## Viz 1: Rainfall Distribution
**Finding:** 25+ of 30 days have <5mm rain; mean 5.2mm/day; CV=1.8 (highly variable). Total: ~155mm — adequate but episodic.
**Implication:** Cannot rely on daily rainfall. Irrigation must cover 5+ consecutive dry days. Heavy rain days (20–85mm) create drainage losses.

---

## Viz 2: Temperature–Humidity Scatter
**Finding:** Strong negative correlation r=−0.78. Temp range 18–45.8°C; humidity 35–95%. Rain days cluster at low temp/high humidity. One outlier at 45.8°C.
**Implication:** ET highest on hot dry days (up to 6mm/day), lowest on cool humid days (~1mm/day). Outlier day requires emergency irrigation.

---

## Viz 3: Soil Moisture by Zone (30 days)
**Finding:**
- Zone A (Tomato): 28–35%, min ~27%
- Zone B (Kale): 25–32%, min ~23% (brief stress)
- Zone C (Maize): 20–28%, min ~18% (stress, recovers)
- All zones converge toward equilibrium by day 28–30

**Critical periods:** Day 8–10 (Zone A low), Day 14–16 (Zone B minimum), Day 20–22 (all zones low simultaneously).

---

## Viz 4: Pump Activity & Power
**Finding:** ~5–8 active pumping days of 30; peak 120 L/min, 2000W. Pump off on high-rainfall days (days 15, 25). Flow–power relationship is linear.
**Implication:** Responsive management already happening. Total extraction ~4500L/month — sustainable. System well-matched to crop needs.

---

## Viz 5: Multi-Parameter Weather Dashboard (2×2)
**Finding:** Wind 0.5–4.5 m/s (stable); Solar 0.2–0.95 (high variability); Temp mostly 20–30°C + one 45.8°C extreme; Humidity 35–95%.

**ET drivers by day type:**

| Day Type | Temp | Humidity | Solar | Est. ET | Action |
|----------|------|----------|-------|---------|--------|
| Hot/dry/sunny | >30°C | <50% | >0.8 | 5–6 mm | Irrigate daily |
| Cool/humid/cloudy | <22°C | >80% | <0.4 | 1–2 mm | Reduce/skip |
| Extreme | 45.8°C | low | high | 7–8 mm | Emergency irrigation |
