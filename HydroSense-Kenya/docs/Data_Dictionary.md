# HydroSense-Kenya Data Dictionary

**Student:** ELPIS MWANGI MAINA | SCT211-0003/2024

## Weather Daily

| Variable | Unit | Range | Description |
|----------|------|-------|-------------|
| date | YYYY-MM-DD | 2026-03-04 to 2026-04-02 | Date of measurement |
| rainfall_mm | mm | 0.0–85.0 | Daily precipitation |
| temperature_c | °C | 18.0–45.8 | Mean air temperature |
| humidity_pct | % | 35.0–95.0 | Relative humidity |
| wind_speed_mps | m/s | 0.5–4.5 | Mean wind speed |
| solar_index | 0–1 | 0.2–0.95 | Solar radiation index |

## Soil Sensor Data

| Variable | Unit | Range | Description |
|----------|------|-------|-------------|
| timestamp | datetime | Daily noon | Measurement time |
| zone_id | string | Zone_A/B/C | Farm zone |
| soil_moisture_pct | % | 15.0–45.0 | Volumetric soil moisture |
| tank_level_liters | L | 3000–9900 | Water tank level |
| pump_flow_lpm | L/min | 0.0–150.0 | Pump flow rate |
| pump_power_watts | W | 0.0–2500.0 | Power consumed |
| sensor_status | string | OK/CHECK/ERROR | Sensor status |

## Crop Zone Parameters

| Variable | Unit | Range | Description |
|----------|------|-------|-------------|
| zone_id | string | Zone_A/B/C | Zone identifier |
| crop_type | string | Tomato/Kale/Maize | Crop species |
| area_m2 | m² | 1000–5000 | Zone area |
| min_moisture_pct | % | 20.0–24.0 | Stress threshold |
| target_moisture_pct | % | 30.0–35.0 | Optimal moisture |
| field_capacity_pct | % | 40.0–45.0 | Maximum storage |
| drainage_coefficient | — | 0.15–0.20 | Daily loss fraction |

*Missing values indicated with NA. Dataset includes intentional quality issues for educational purposes.*
