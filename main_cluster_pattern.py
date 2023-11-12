import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


gd_sp_data = "gd_sp_data.csv"
data_r = pd.read_csv(gd_sp_data)

scaler = StandardScaler()
scaled_data = scaler.fit_transform(data_r)

klastr = KMeans(n_clusters=1)
data_r["cluster"] = klastr.fit_predict(scaled_data)
center = scaler.inverse_transform(klastr.cluster_centers_)

center_f = []
data_name = ["fall_asleep", "wakeup", "length", "light_sleep", "deep_sleep", "REM", "wakeup_count"]

for list1 in center:
    for data in list1:
        data = round(data)
        center_f.append(data)
