from flask_restful import Resource, reqparse
from models.hotel import HotelModel
hoteis = [
        {
        'hotel_id': 'alpha',
        'nome': 'Alpha HOtel',
        'estrelas': 4.3,
        'diaria': 420.00,
        'cidade': 'Barcelona2'
        },
        {
        'hotel_id': 'beta',
        'nome': 'Beta HOtel',
        'estrelas': 5,
        'diaria': 1500.00,
        'cidade': 'Madrid2'
        },
        {
        'hotel_id': 'gama',
        'nome': 'Gama HOtel2',
        'estrelas': 4.0,
        'diaria': 350.00,
        'cidade': 'Puno'
        },
        {
        'hotel_id': 'rota',
        'nome': 'Rota Hotel',
        'estrelas': 3.5,
        'diaria': 300.00,
        'cidade': 'Rio de Janeiro2'
        }
]
     
class Hoteis(Resource):
    def get(self):
        return {'hoteis': hoteis} #dicionário
    
class Hotel(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('estrelas')
    argumentos.add_argument('diaria')
    argumentos.add_argument('cidade')
    
    def find_hotel(hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return None
    
    def get(self, hotel_id):
        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            return hotel            
        return {'message': 'HOTEL NOT FOUND'}, 404     
    
    def post(self, hotel_id):    
        dados = Hotel.atributos.parse_args()
        hotel_objeto = HotelModel{'hotel_id': hotel_id, **dados}
        novo_hotel = hotel_objeto.json()        
        hoteis.append(novo_hotel)#adicionando novo hotel na lista
        return novo_hotel, 201
        
    def put(self, hotel_id):
        dados = Hotel.atributos.parse_args()
        hotel_objeto = HotelModel(hotel_id, **dados)            
        novo_hotel = hotel_objeto.json()        
        hotel = Hotel.find_hotel(hotel_id)
        #se o hotel existir atualize!
        if hotel:
            hotel.update(novo_hotel)
            return novo_hotel, 200 #OK
        #se o hotel não existir
        hoteis.append(novo_hotel)
        return novo_hotel, 201 #created hotel    
    
    def delete(self, hotel_id):
        global hoteis
        hoteis = [hotel for hotel in hoteis if hotel['hotel_id'] != hotel_id]
        return {'message': 'Hotel deleted.'}
        