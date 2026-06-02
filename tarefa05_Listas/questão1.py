from datetime import datetime, timedelta
class Treino:
    def __init__(self, id, data, distancia, tempo):
        self.__id = id
        self.__data = data
        self.__distancia = distancia
        self.__tempo = tempo

    def get_id(self):
        return self.__id

    def get_data(self):
        return self.__data

    def get_distancia(self):
        return self.__distancia

    def get_tempo(self):
        return self.__tempo

    def set_data(self, data):
        self.__data = data

    def set_distancia(self, distancia):
        self.__distancia = distancia

    def set_tempo(self, tempo):
        self.__tempo = tempo

    def pace(self):
        segundos_totais = self.__tempo.total_seconds()
        pace_segundos = segundos_totais / self.__distancia
        return timedelta(seconds=pace_segundos)