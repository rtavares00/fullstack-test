import requests #Biblioteca para requisições Web
import json #biblioteca para manipular JSON
class ApiOpenWeatherMap:
    
    def __init__(self):
        self.base_url = "http://api.openweathermap.org/data/2.5/weather?appid=46c1807d6408bcf74ce9937d90c6b743&lang=pt"
        #URL base para as requisições a API do Open Weather
        
    def cityWeather(self,name_of_city = None , lat_lng = None ): #método responsável por informar a temperatura de determinado local
        
        if name_of_city is not None: #testando se usuário informou nome do lugar ao invés de coordenadas
            city = name_of_city.replace(" ","+") #tratamento para substituir espaços no nome da cidade (se houve) por "+"
            full_url = self.base_url+"&q="+city
        
        if lat_lng is not None: #testando se usuário informou cordenadas ao invés do nome do lugar
            full_url = self.base_url+"&lat="+lat_lng["latitude"]+"&lon="+lat_lng["longitude"]
        
        _json = requests.get(full_url).json() #retorno da requisição a API em formato JSON

        if _json["cod"] == "404": #testando para saber se a consulta retornou um resultado válido
            return json.dumps( { 'temp':"Location not found"})
        
        return json.dumps( { 'temp': round(_json["main"]["temp"] - 273.15,1) } ) # retornando o valor da temperatura (convertido para CELSIUS)
        
        
        
        
            
        
    