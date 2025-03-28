
import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

# Set page config
st.set_page_config(page_title="Marine Dashboard", layout="wide")

st.title("🌊 Transocean Norge – Marine Operations Dashboard")

# Simuler data (48 timer)
np.random.seed(42)
times = [datetime.now() + timedelta(hours=i) for i in range(48)]
wave_heights = np.random.normal(loc=2.2, scale=0.6, size=48)
swell_heights = np.random.normal(loc=1.4, scale=0.4, size=48)
wind_speeds = np.random.normal(loc=10, scale=3, size=48)
headings = np.random.randint(0, 360, size=48)

df = pd.DataFrame({
    "Time": times,
    "Wave Height (m)": np.clip(wave_heights, 0, None),
    "Swell Height (m)": np.clip(swell_heights, 0, None),
    "Wind Speed (m/s)": np.clip(wind_speeds, 0, None),
    "Heading (°)": headings
})
df["Go/No-Go"] = np.where(df["Wave Height (m)"] > 3, "🚫 No-Go", "✅ Go")

# Plotting
fig, ax = plt.subplots(figsize=(14, 6))
below = df["Wave Height (m)"] <= 3
above = df["Wave Height (m)"] > 3

ax.plot(df["Time"][below], df["Wave Height (m)"][below], label="Wave Height ≤ 3m", color='blue')
ax.plot(df["Time"][above], df["Wave Height (m)"][above], label="Wave Height > 3m", color='red')
ax.plot(df["Time"], df["Swell Height (m)"], label="Swell Height", linestyle='--', color='green')
ax.plot(df["Time"], df["Wind Speed (m/s)"], label="Wind Speed", linestyle='-.', color='orange')

ax.set_xlabel("Time")
ax.set_ylabel("Value")
ax.set_title("Wave, Swell & Wind Forecast (Simulated)")
ax.legend()
ax.grid(True)
plt.xticks(rotation=45)

# Show plot
st.pyplot(fig)

# Go/No-Go Table
st.subheader("🚦 Go/No-Go Table (48h)")
st.dataframe(df[["Time", "Wave Height (m)", "Go/No-Go"]].set_index("Time"))
