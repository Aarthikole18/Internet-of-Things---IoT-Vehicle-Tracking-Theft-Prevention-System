import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from streamlit_autorefresh import st_autorefresh
from pandas.errors import EmptyDataError
from math import radians, sin, cos, sqrt, atan2
import os

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="IoT Vehicle Tracking System",
    page_icon="🚗",
    layout="wide"
)

# Auto Refresh
st_autorefresh(interval=2000, key="vehicle_refresh")

# -----------------------------
# CUSTOM CSS
# -----------------------------
st.markdown("""
<style>
.main {
    background-color: #0E1117;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# TITLE
# -----------------------------
st.title("🚗 IoT Vehicle Tracking & Theft Prevention System")
st.markdown("### Real-Time GPS Monitoring Dashboard")

# -----------------------------
# LOAD DATA SAFELY
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE = os.path.join(BASE_DIR, "data.csv")

try:
    df = pd.read_csv(CSV_FILE)

    if df.empty:
        st.warning("Waiting for GPS data...")
        st.stop()

except EmptyDataError:
    st.warning("Simulator updating data... Refreshing automatically.")
    st.stop()

except FileNotFoundError:
    st.error("data.csv not found.")
    st.stop()

except Exception as e:
    st.error(f"Error: {e}")
    st.stop()

# -----------------------------
# LATEST LOCATION
# -----------------------------
latest = df.iloc[-1]

lat = float(latest["Latitude"])
lon = float(latest["Longitude"])

# -----------------------------
# SAFE LOCATION
# -----------------------------
SAFE_LAT = 12.9716
SAFE_LON = 77.5946

# -----------------------------
# DISTANCE CALCULATION
# -----------------------------
def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6371

    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)

    a = (
        sin(dlat / 2) ** 2
        + cos(radians(lat1))
        * cos(radians(lat2))
        * sin(dlon / 2) ** 2
    )

    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return R * c

distance = calculate_distance(
    SAFE_LAT,
    SAFE_LON,
    lat,
    lon
)

status = "🚨 Theft Alert" if distance > 0.5 else "✅ Safe"

# -----------------------------
# METRICS
# -----------------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("Latitude", round(lat, 6))
col2.metric("Longitude", round(lon, 6))
col3.metric("Distance (km)", round(distance, 3))
col4.metric("Status", status)

# -----------------------------
# ALERT
# -----------------------------
if distance > 0.5:
    st.error("🚨 ALERT! Vehicle outside safe geofence.")
else:
    st.success("✅ Vehicle inside safe zone.")

# -----------------------------
# MAP
# -----------------------------
st.subheader("📍 Live Vehicle Location")

m = folium.Map(
    location=[lat, lon],
    zoom_start=16
)

folium.Marker(
    [lat, lon],
    popup="Vehicle"
).add_to(m)

folium.Marker(
    [SAFE_LAT, SAFE_LON],
    popup="Safe Zone"
).add_to(m)

if len(df) > 1:
    route = df[["Latitude", "Longitude"]].values.tolist()

    folium.PolyLine(
        route,
        weight=5
    ).add_to(m)

st_folium(m, width=1000, height=500)

# -----------------------------
# GOOGLE MAPS
# -----------------------------
st.markdown(
    f"[🌍 Open in Google Maps](https://www.google.com/maps?q={lat},{lon})"
)

# -----------------------------
# GPS HISTORY
# -----------------------------
st.subheader("📊 GPS History")

st.dataframe(
    df.tail(20),
    use_container_width=True
)

# -----------------------------
# DOWNLOAD
# -----------------------------
csv = df.to_csv(index=False)

st.download_button(
    "⬇ Download GPS Report",
    csv,
    "vehicle_tracking_report.csv",
    "text/csv"
)

# -----------------------------
# INFO
# -----------------------------
with st.expander("ℹ Project Information"):
    st.write("""
    • Real-Time GPS Tracking

    • Vehicle Monitoring

    • Theft Detection

    • Geofencing

    • CSV Logging

    • Interactive Maps

    • Google Maps Integration
    """)

st.success("✅ System Running Successfully")