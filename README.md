# 🪐 Astrology ZR Timeline Generator

A Flask web app for generating personalized astrological period tables using traditional timing techniques.

## ✨ Features

- Zodiacal Releasing of Fortune and Spirit (L1–L3)
- Firdaria (Major and Minor periods)
- Annual Profections based on Ascendant
- Uranus, Neptune, Pluto transit sign tracking
- Excel file download with color-coded rows and symbols

## 📥 Input

- Birth date & time (Year, Month, Day, Hour, Minute)
- Latitude and Longitude
- Timezone (e.g., 9 for Korea)

## 📤 Output

- Excel file (`.xlsx`) with:
  - Date & Age
  - ZR (Fortune & Spirit, L1–L3)
  - Firdaria periods
  - Annual Profection sign
  - Outer planet signs

## 🚀 Local Dev

```bash
pip install -r requirements.txt
python app.py
