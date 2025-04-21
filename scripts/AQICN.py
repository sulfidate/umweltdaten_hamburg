import requests
import pandas as pd
from datetime import datetime

API_TOKEN = "5a018480b553ee583496128fe95decf8583e0fae"
API_URL = f"https://api.waqi.info/feed/A61000/?token={API_TOKEN}"
CSV_FILE = "aqi_hamburg_api.csv"

def fetch_data():
    response = requests.get(API_URL)
    data = response.json()

    if data["status"] != "ok":
        print("Fehlerhafte API-Antwort.")
        return

    d = data["data"]
    result = {
        "timestamp": pd.to_datetime(d["time"]["iso"]),
        "aqi": d.get("aqi"),
        "pm25": d.get("iaqi", {}).get("pm25", {}).get("v"),
        "pm10": d.get("iaqi", {}).get("pm10", {}).get("v"),
        "no2": d.get("iaqi", {}).get("no2", {}).get("v"),
        "co": d.get("iaqi", {}).get("co", {}).get("v"),
        "o3": d.get("iaqi", {}).get("o3", {}).get("v")
    }

    df = pd.DataFrame([result])
    try:
        old_df = pd.read_csv(CSV_FILE)
        df = pd.concat([old_df, df], ignore_index=True)
        df.drop_duplicates(subset=["timestamp"], inplace=True)
    except FileNotFoundError:
        pass

    df.to_csv(CSV_FILE, index=False)
    print(f"✅ Daten gespeichert: {result['timestamp']}")

if __name__ == "__main__":
    fetch_data()
