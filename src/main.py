# from flask import Flask, render_template_string, request
# import pandas as pd
# import folium
# app = Flask(__name__)
#
# # Initialize a variable
# selected_value = "Default"
#
#
# @app.route('/', methods=['GET', 'POST'])
# def index():
#     global selected_value
#
#     if request.method == 'POST':
#         # Update the variable based on the button clicked
#         selected_value = request.form.get('value')
#         print(f"Selected Value: {selected_value}")
#
#     # Create a Folium map
#     m = folium.Map(location=[45.5236, -122.6750], zoom_start=13)
#
#     # Add a marker with the current selected value
#     folium.Marker(location=[45.5236, -122.6750], popup=selected_value).add_to(m)
#
#     # Save the map to an HTML file
#     m.save('map.html')
#
#     # Render the HTML file with buttons
#     return render_template_string('''
#     <!doctype html>
#     <html>
#         <head>
#             <title>Folium Map with Variable Control</title>
#         </head>
#         <body>
#             <h1>Folium Map with Variable Control</h1>
#             <form method="post">
#                 <button name="value" value="Option 1">Select Option 1</button>
#                 <button name="value" value="Option 2">Select Option 2</button>
#                 <button name="value" value="Option 3">Select Option 3</button>
#             </form>
#             <div>
#                 <iframe src="map.html" width="100%" height="500"></iframe>
#             </div>
#         </body>
#     </html>
#     ''')
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
#
# data = pd.DataFrame({
#     'lon': [
#         -84.3478,
#         -105.0008,
#         -123.3656,
#         -66.4619,
#         -63.1340,
#         -97.5500,
#         -58.0000,
#         -115.5834,
#         -135.0000,
#         -119.4900,
#         -62.8600
#     ],
#     'lat': [
#         50.0000,
#         55.0000,
#         53.7267,
#         46.5653,
#         46.5107,
#         53.7609,
#         53.1355,
#         55.0000,
#         64.2823,
#         64.8255,
#         45.0000
#     ],
#     'name': [
#         'Ontario',
#         'Saskatchewan',
#         'British Columbia',
#         'New Brunswick',
#         'Prince Edward Island',
#         'Manitoba',
#         'Newfoundland and Labrador',
#         'Alberta',
#         'Yukon',
#         'Northwest Territories',
#         'Nova Scotia'
#     ],
#     'value': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]
# })
