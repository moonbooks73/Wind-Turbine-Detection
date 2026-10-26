import pandas as pd

# Data should be saved in data as telemetry_data.csv
df = pd.read_csv("data/telemetry_data.csv")

# Groups the turbines with the same IDs, then applies aggregate functions
# Mean for temperature and the maximum for vibration
summary = (
    df.groupby("turbine_id").agg(
          avg_temp=("temperature_c", "mean"),
          max_vibration=("vibration_mm_s", "max")))

# Then filter for the turbines with temperature for than 85 or vibration more than 15
failing_turbines = summary[
    (summary["avg_temp"] > 85.0) |
    (summary["max_vibration"] > 15.0)].index.tolist()

print(failing_turbines)

if failing_turbines:
    pd.DataFrame(failing_turbines, columns=["turbine_id"]) \
      .to_csv("data/failing_turbines.csv", index=False)
    
else:
    print("No failing turbines detected")