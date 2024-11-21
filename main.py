from flask import Flask, render_template, request
from functions import get_weather, get_periodo_dia

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    error_message = None
    periodo_dia = get_periodo_dia()

    if request.method == 'POST':
        city_name = request.form['city_name']
        weather_data = get_weather(city_name)
        
        if weather_data is None:
            error_message = "Cidade não encontrada. Verifique o nome e tente novamente."
            
    return render_template('clima.html', weather_data=weather_data, error_message=error_message, periodo_dia=periodo_dia)

if __name__ == "__main__":
    app.run(debug=True)
