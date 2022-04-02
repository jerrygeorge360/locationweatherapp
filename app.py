from flask import Flask, render_template, request
import math

from weatherapi import Getweather, runWeather

app = Flask(__name__)
app.debug = True
@app.context_processor
def universal():


    return dict()

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    global data
    weatherdata = runWeather
    if request.method == 'POST':

        try:

            cityname = request.form['city_name']
            statename = request.form['state_code']
            data = weatherdata(cityname, statename)
            firstpart = [
                f'longitude: {data["coordinates"].get("lon")}',
                f'latitude:{data["coordinates"].get("lat")}',
                f'temperature max: {int(data["main"].get("temp_max"))-273.1} degrees',
                f'temperature min: {int(data["main"].get("temp_min"))-273.1} degrees',
                f'pressure: {data["main"].get("pressure")}',
                f'humidity: {data["main"].get("humidity")}',
                f'wind speed: {data["wind"].get("speed")}',
                f'station: {data["base"]}',
                f'wind gust: {data["wind"].get("gust")}'

            ]

            secondpart = [
                f'city: {cityname}',
                f'weather:{data["weather"].get("main")}',
                f'description: {data["weather"].get("description")}',
                f'{data["weather"].get("icon")}',
                f'temperature: {int(data["main"].get("temp"))-273.15} degrees',
                f'visibility: {data["visibility"]}'
            ]



        except Exception as err:
            print(f' error from line 42 :{err}')
            return f'No internet service'

        return render_template('weather.html', firstd=firstpart, secondd=secondpart ,data=data)
    return render_template('weather.html')


if __name__ == '__main__':
    app.run()
