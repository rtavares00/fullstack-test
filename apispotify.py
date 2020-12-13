import json #biblioteca para manipular JSON
import spotipy #biblioteca para trabalhar com requisições a api do spotify
from spotipy.oauth2 import SpotifyClientCredentials

#https://github.com/plamere/spotipy/blob/master/README.md
class ApiSpotify:

    def getRecommendation(self,genre): # método responsável por processar as recomendações baseado em gênero
               
        
        sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="2d3d0bfc4b30464790f87ac326aca91f",
                                               client_secret="e43563d9212d47c49f0bae8f838e90d3"
                                               )) # parâmetros para autenticar na api do spotify

        """
        {'genres': ['acoustic', 'afrobeat', 'alt-rock', 'alternative', 'ambient', 'anime', 'black-metal', 'bluegrass', 'blues', 'bossanova', 'brazil', 'breakbeat', 'british', 'cantopop', 'chicago-house', 'children', 'chill', 'classical', 'club', 'comedy', 'country', 'dance', 'dancehall', 'death-metal', 'deep-house', 'detroit-techno', 'disco', 'disney', 'drum-and-bass', 'dub', 'dubstep', 'edm', 'electro', 'electronic', 'emo', 'folk', 'forro', 'french', 'funk', 'garage', 'german', 'gospel', 'goth', 'grindcore', 'groove', 'grunge', 'guitar', 'happy', 'hard-rock', 'hardcore', 'hardstyle', 'heavy-metal', 'hip-hop', 'holidays', 'honky-tonk', 'house', 'idm', 'indian', 'indie', 'indie-pop', 'industrial', 'iranian', 'j-dance', 'j-idol', 'j-pop', 'j-rock', 'jazz', 'k-pop', 'kids', 'latin', 'latino', 'malay', 'mandopop', 'metal', 'metal-misc', 'metalcore', 'minimal-techno', 'movies', 'mpb', 'new-age', 'new-release', 'opera', 'pagode', 'party', 'philippines-opm', 'piano', 'pop', 'pop-film', 'post-dubstep', 'power-pop', 'progressive-house', 'psych-rock', 'punk', 'punk-rock', 'r-n-b', 'rainy-day', 'reggae', 'reggaeton', 'road-trip', 'rock', 'rock-n-roll', 'rockabilly', 'romance', 'sad', 'salsa', 'samba', 'sertanejo', 'show-tunes', 'singer-songwriter', 'ska', 'sleep', 'songwriter', 'soul', 'soundtracks', 'spanish', 'study', 'summer', 'swedish', 'synth-pop', 'tango', 'techno', 'trance', 'trip-hop', 'turkish', 'work-out', 'world-music']}
        """
        
        tracks = [] #inicializando variável de retorno
        _tracks = sp.recommendations(seed_genres=[genre],limit=10) #obtendo a playlist baseado no gênero
        
        for track in _tracks['tracks']:
            tracks.append( {'song': track['name'] , 'artist': track['artists'][0]['name'] , 'link': track['href']} )
            #alimentando lista com informações referente as faixas e o nome do artista.
        return tracks