import json #biblioteca para manipular JSON
import math #biblioteca para trabalhar com funções matemáticas
from apiopenweathermap import ApiOpenWeatherMap # importando classe criada para lógica do Open Weather Map
from apispotify import ApiSpotify # Importando a classe para manipular a api do Spotify
from flask import Flask ,render_template ,request #bibliotecas do Framework Flask

app = Flask(__name__,template_folder='html') #parâmetros da aplicação , template_folder é onde está o HTMl do sistema


@app.route('/') #rota principal
def index(): 
    return render_template('index.html')
    
@app.route('/process_data', methods = ['POST']) #rota de processamento de dados
#request.args.get('limit', default=20, type=int)
def process_data():
    openWeather = ApiOpenWeatherMap() #instancia da classe Open Weather Map
    spotify = ApiSpotify() #instancia da classe do Spotify
    
    if request.form.get('isLatLng') == 'Y': # verificando se usuário está entrando com Cidade Ou coordenadas
        temp = json.loads(openWeather.cityWeather(lat_lng = {"latitude":request.form.get("latitude") , "longitude":request.form.get("longitude")}))
    else:
        temp = json.loads(openWeather.cityWeather(name_of_city=request.form.get("cidade")))
        
    
    temp = temp["temp"] # obtendo valor float da temperatura
    
    genre = None # inicializando variável
    if math.floor(temp > 30): # verificando a temperatura para obter o gênero que será solicitado ao Spotify
        genre =  "party"
    elif math.floor(temp) >= 15 and math.floor(temp) <= 30:
        genre = "pop"
    elif math.floor(temp) >= 10 and math.floor(temp) <= 14:
        genre = "rock"
    elif math.floor(temp) < 10:
        genre =  "classical"
    
    playlist = spotify.getRecommendation(genre) #Obtendo a Playlist
    
    return { 'temperature': str(temp).replace(".",","), 'genre':genre , 'playlist':playlist } # Retorno para a requisição AJAX
    
    
    

if __name__ == '__main__':
    app.run(debug=True)