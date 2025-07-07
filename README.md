# 🪐 Astrology ZR Timeline Generator

A Flask web app for generating personalized astrological period tables using traditional timing techniques.

## ✨ Features

- **Zodiacal Releasing** of Fortune and Spirit (L1–L3)
- **Firdaria** (Major and Minor periods)
- **Annual Profections** based on Ascendant
- **Uranus, Neptune, Pluto** transit sign tracking
- Excel file download with color-coded rows and symbols

## 📝 Input

- Birth date & time (Year, Month, Day, Hour, Minute)
- Latitude and Longitude
- Timezone (e.g., 9 for Korea)

## 📥 Output

- Downloadable `.xlsx` file containing:
  - Date & Age
  - ZR (Fortune & Spirit, L1–L3)
  - Firdaria periods
  - Annual Profection sign
  - Outer planet signs

## 🚀 How to Run Locally

```bash
pip install -r requirements.txt
python app.py
```

Then open your browser to [http://localhost:5000](http://localhost:5000)

## 🌐 Deploy on Render

1. Fork or clone this repo
2. Create a new Web Service on [Render](https://render.com/)
3. Use this repo and ensure the `render.yaml` file is present
4. Render will auto-deploy the app from GitHub

---

Built with ❤️ using Flask, Pandas, Swiss Ephemeris, and OpenPyXL
