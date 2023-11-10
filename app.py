from flask import Flask, render_template
import requests
from dotenv import load_dotenv,dotenv_values

app = Flask(__name__)

config = dotenv_values ('.env')

def get_weather_data(city):
    API_KEY = config['API_KEY']
    url=f'https://api.openweathermap.org/data/2.5/weather?q={ city }&appid={API_KEY}&units=metric&lang=es'
    r = requests.get(url).json()
    return r 

@app.route('/joseph')
def joseph():
    return get_weather_data('guayaquil')

@app.route('/about')
def about():
    return render_template('weather.html')

@app.route('/clima')
def clima():
    return 'obtener todo la informacion del clima'

if __name__ == '__main__':
    app.run(debug=True)













