from flask import Flask, render_template_string, request
import folium

app = Flask(__name__)

# Initialize a variable
selected_value = "Default"


@app.route('/', methods=['GET', 'POST'])
def test():
    global selected_value

    if request.method == 'POST':
        # Update the variable based on the button clicked
        year = float(request.form.get('year'))
        # source =
        print(f"Selected Value: {selected_value}")

    # Create a Folium map
    m = folium.Map(location=[45.5236, -122.6750], zoom_start=13)

    # Add a marker with the current selected value
    folium.Marker(location=[45.5236, -122.6750], popup=selected_value).add_to(m)

    # Save the map to an HTML file
    m.save('static/map.html')

    # Render the HTML file with buttons
    return render_template_string('''
        <!doctype html>
        <html>
            <head>
                <title>Folium Map with Variable Control</title>
            </head>
            <body>
                <h1>Folium Map with Variable Control</h1>
                <form method="post">
                    <button name="year" value="2002">2002</button>
                    <button name="year" value="2003">2003</button>
                    <button name="year" value="2004">2004</button>
                </form>
                <div>
                    <iframe src="{{ url_for('static', filename='map.html') }}" height="500"></iframe>
                </div>
            </body>
        </html>
        ''')


if __name__ == '__main__':
    app.run(debug=True)
