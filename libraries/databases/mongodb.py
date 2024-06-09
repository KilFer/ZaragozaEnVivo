from pymongo import MongoClient


class MongoDB:

    db_name = "ZaragozaEnVivo"

    def __init__(self, uri):
        """
        Inicializa la instancia y se conecta a la base de datos MongoDB.

        :param uri: URI de conexión a MongoDB.
        :param db_name: Nombre de la base de datos.
        """
        self.client = MongoClient(uri)
        self.db = self.client[self.db_name]
        self.events_collection = self.db["events"]

    def guardar_evento(self, evento):
        """
        Guarda un evento en la base de datos.

        :param evento: Diccionario con los datos del evento.
        :return: ID del documento insertado.
        """
        result = self.events_collection.insert_one(evento)
        return result.inserted_id

    def obtener_evento_por_id(self, event_id):
        """
        Obtiene un evento por su ID.

        :param event_id: ID del evento.
        :return: Diccionario con los datos del evento, o None si no se encuentra.
        """
        return self.events_collection.find_one({"id": event_id})

    def obtener_eventos_por_ids(self, event_ids):
        """
        Obtiene una lista de eventos por sus IDs.

        :param event_ids: Lista de IDs de los eventos.
        :return: Lista de diccionarios con los datos de los eventos.
        """
        return list(self.events_collection.find({"id": {"$in": event_ids}}))
