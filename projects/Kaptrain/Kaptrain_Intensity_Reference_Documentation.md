
# Kaptrain – Intensity Reference System Documentation

A comprehensive guide for developers to understand how Kaptrain defines and uses training intensity references across endurance, strength, and cognitive domains.

---

## 1. Overview

Training blocks in Kaptrain require an **intensity reference** (“Référence d’intensité”) so that prescriptions can be personalized according to the athlete’s physiological or subjective metrics.

This document explains the meaning of each intensity type, how to calculate target values, and provides examples used in the mobile app.

---

## 2. Intensity Reference Types

Below are all available reference types displayed in the Kaptrain mobile app during **block creation**.

### **2.1 Aucun (None)**
No structured intensity target.

**Use cases**
- Mobility
- Stretching
- Warm-up
- Technique drills

**Example**
```
Block: Mobility Sequence
Intensity: None
Prescription: 5–10 min light dynamic movements
```

---

### **2.2 FORCE (%RM)**
Intensity based on **percentage of 1RM (one‑rep max)**.

**Formula**
```
Target Load = 1RM × %RM
```

**Example**
```
Block: Back Squat Strength
Intensity: FORCE (%RM)
Prescription: 5 × 5 @ 80% RM
Athlete 1RM: 120 kg → Work weight = 96 kg
```

---

### **2.3 Cardiaque (%FC Max)**
Intensity based on **percentage of maximum heart rate**.

**Formula**
```
Target HR = FCmax × %
```

**Example**
```
Block: Zone 2 Endurance
Intensity: %FC Max
Prescription: 40 min @ 65–70% FC Max
Athlete FC Max: 190 bpm → Target = 124–133 bpm
```

---

### **2.4 Puissance (%PMA) – Cycling VO2Max Power**
Used in cycling for **Maximal Aerobic Power**.

**Formula**
```
Target Power = PMA × %
```

**Example**
```
Block: VO2 Intervals
Intensity: Puissance (%PMA)
Prescription: 6 × 3 min @ 120% PMA, 3 min rest
Athlete PMA: 300 W → Target = 360 W
```

---

### **2.5 Puissance (%FTP) – Cycling Threshold Power**
Used for cycling threshold sessions.

**Formula**
```
Target Power = FTP × %
```

**Example**
```
Block: Sweet Spot
Intensity: %FTP
Prescription: 2 × 20 min @ 88–92% FTP
Athlete FTP: 250 W → Target = 220–230 W
```

---

### **2.6 Vitesse (%VMA) – Running Speed**
Used for running interval training.

**Formula**
```
Target Speed = VMA × %
```

VMA = “Vitesse Maximale Aérobie”

**Example**
```
Block: Aerobic Endurance Z4 (~95% VMA)
Intensity: Vitesse (%VMA)
Prescription: 8 × 400 m @ 95% VMA, rest 1’30
Athlete VMA: 16 km/h → Target speed = 15.2 km/h
Expected lap time ≈ 1:35
```

---

### **2.7 Vitesse brute (Raw Speed)**
Uses absolute speed instead of physiological percentage.

**Example**
```
Block: Tempo Run
Intensity: Vitesse brute
Prescription: 20 minutes @ 11.5 km/h
```

Used when the athlete has no VMA test.

---

### **2.8 Ressenti (RPE Physique)**
Subjective **physical effort rating** (scale 1–10).

**Example**
```
Block: Moderate Endurance
Intensity: RPE Physique
Prescription: 30 min @ RPE 6/10
```

---

### **2.9 Ressenti (RPE Cognitif)**
Subjective **mental effort** rating.

**Example**
```
Block: Coordination Drills
Intensity: RPE Cognitif
Prescription: 15 min @ RPE cognitive 7/10
```

Used for complex technical sports or mentally demanding tasks.

---

## 3. Comparison Table

| Type | Domain | Data Needed | Use Case |
|------|--------|-------------|----------|
| Aucun | General | None | Warm-up, mobility |
| %RM | Strength | 1RM | Weightlifting blocks |
| %FC Max | Cardio | HR max | Running, intervals |
| %PMA | Cycling | PMA | VO2 training |
| %FTP | Cycling | FTP | Threshold training |
| %VMA | Running | VMA | Intervals, Z2–Z5 |
| Raw Speed | Running | Speed only | Tempo runs |
| RPE Physique | Subjective physical | Athlete rating | Recovery runs, skill |
| RPE Cognitif | Subjective mental | Athlete rating | Technical complexity |

---

## 4. Recommended Database Schema

### **Table: intensity_reference_types**
```
id (PK)
label (text)
code (enum: NONE, RM, FC_MAX, PMA, FTP, VMA, RAW_SPEED, RPE_PHYSICAL, RPE_COGNITIVE)
description (text)
unit (text)
```

### **Table: training_blocks**
```
id (PK)
workout_id (FK)
title
description
intensity_type_id (FK)
value (numeric)
value_min (numeric)
value_max (numeric)
duration_seconds
distance_meters
repetitions
rest_duration_seconds
created_at
updated_at
```

---

## 5. Developer Notes

### **When to use %‑based vs raw values**
- Use **%RM / %VMA / %PMA / %FTP / %FC Max** when personalization is required.
- Use **raw speed / raw power** when:
  - athlete has no test data  
  - coach wants fixed speed

### **App logic**
- When user selects an intensity reference → app loads appropriate input fields.
- Example:
  - %VMA → show fields: VMA value, zone, time/distance entry
  - %RM → show fields: RM test, reps, load calculation
  - RPE → show only slider + description

---

## 6. Real Block Example (Full JSON)

```json
{
  "title": "Aerobic Endurance Z4",
  "intensity_type": "VMA",
  "intensity_value": 0.95,
  "vma_user": 16,
  "sets": 8,
  "work_time_sec": 90,
  "rest_time_sec": 90,
  "calculated_speed_kmh": 15.2
}
```

---

## 7. Summary

This document ensures all developers understand:

- What each intensity reference means  
- How calculations work  
- When to use each type  
- How training blocks should be stored and computed  

It is part of the **Kaptrain Training Architecture** and should be used as a reference for app and backend implementation.

---

If you want, I can also generate:
- **ERD Diagram** for the full training system  
- **Technical Specification PDF**  
- **Swagger API models**  
- **Automated calculators for VMA/PMA/RM/etc.**
