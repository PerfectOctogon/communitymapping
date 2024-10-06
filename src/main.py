import folium
from folium.plugins import HeatMap
import pandas as pd
from flask import Flask, app, request,render_template, jsonify

app = Flask(__name__, template_folder="templates")
global m
m = folium.Map(location=[56.1304, -106.3468], tiles="OpenStreetMap", zoom_start=4)

def get_province_data():
    data = pd.DataFrame({
        'lon': [
            -84.3478,
            -105.0008,
            -123.3656,
            -66.4619,
            -63.1340,
            -97.5500,
            -58.0000,
            -115.5834,
            -135.0000,
            -119.4900,
            -62.8600
        ],
        'lat': [
            50.0000,
            55.0000,
            53.7267,
            46.5653,
            46.5107,
            53.7609,
            53.1355,
            55.0000,
            64.2823,
            64.8255,
            45.0000
        ],
        'name': [
            'Ontario',
            'Saskatchewan',
            'British Columbia',
            'New Brunswick',
            'Prince Edward Island',
            'Manitoba',
            'Newfoundland and Labrador',
            'Alberta',
            'Yukon',
            'Northwest Territories',
            'Nova Scotia'
        ],
        'value': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]
    })
    return data

data = get_province_data()

for i in range(len(data)):
    folium.Marker(
        location=[data.iloc[i]['lat'], data.iloc[i]['lon']],
        popup=f"{data.iloc[i]['name']} - Value: {data.iloc[i]['value']}"
    ).add_to(m)

@app.route("/", methods=['GET', 'POST'])

def index():

   if request.method == 'POST':
      year = int(request.form.get('year'))
      source = "Agriculture" #request.form.get('source')

      generate_heatmap(year, source)
 
   m.save('src/static/map.html')

   # You can now use that value as any other in your template.
   # Also, I would suggest renaming "data"
   # To someone who reads your code, it looks like this variable contains
   # data, when it's actually just a boolean to show/hide the data.
   return render_template('index.html')

def generate_heatmap(year, source):
    df = pd.read_csv("src/res/carbonemissions.csv")
    #test source and year
    print(year)
    filtered_rows = df.loc[(df["Source"] == source)
                       & (df["Year"] == year)
                       & (df["Total"] == "y")
                       & (df["Region"] != "Canada")  # Exclude rows where Region is Canada
    ]                                                    #total = y is the total of all sub sectors
    co2eq_values = filtered_rows["CO2eq"].values
    #change datatype to float
    co2eq_values = [float(num) for num in co2eq_values]
    max_co2 = max(co2eq_values)
    #create a loop that iterates through co2 values, finds the associated "Region" and gets the 'lon' and 'lat' value from
    # the coordinates dataFrame and adds it as a new list into the heat map data list
    heatmap_data = []

    for index, row in filtered_rows.iterrows():
        region_name = row["Region"]

        # Find the corresponding coordinates for the region
        coord_row = data[data['name'] == region_name]

        if not coord_row.empty:  # Check if a matching region was found and parse it to a numeric value
            lat = float(coord_row['lat'].values[0])
            lon = float(coord_row['lon'].values[0])
            value = float(row["CO2eq"])/max_co2 #divide by the max value to get our opacity value between 0 and 1

            # Add the data to heatmap_data
            heatmap_data.append([lat, lon, value])  # Append [latitude, longitude, CO2 value]

    HeatMap(heatmap_data, radius=50, blur=40, min_opacity=0.2).add_to(m)


if __name__ == '__main__':
    app.run(debug=True)
