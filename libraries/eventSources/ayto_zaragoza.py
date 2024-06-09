import requests


class AytoZaragoza:

    base_url = "https://www.zaragoza.es/sede/servicio/cultura/evento"
    prefix = "AZ"

    def __init__(self):
        """
        Inicializa el objeto.
        """


    def _add_prefix_to_id(self, event_id):
        """
        Añade la cabecera 'AZ-' al ID del evento.

        :param event_id: ID del evento.
        :return: ID del evento con la cabecera 'AZ-'.
        """
        return f"{self.prefix}-{event_id}"


    def _remove_prefix_from_id(self, event_id):
        """
        Elimina la cabecera 'AZ-' del ID del evento.

        :param event_id: ID del evento con la cabecera.
        :return: ID del evento sin la cabecera.
        """
        if event_id.startswith(f"{self.prefix}-"):
            return event_id[3:]
        return event_id

    def get_eventos(self, query="", rows=50, start=0):
        """
        Obtiene la lista de eventos a través de una consulta en formato SOLR.

        :param query: Consulta en formato SOLR para filtrar eventos.
        :return: Lista de eventos en formato JSON.
        """
        # Construye la URL completa con la query SOLR
        url = f"{self.base_url}/list.json?q={query}&rows={rows}&start={start}"

        # Realiza la petición GET al endpoint
        response = requests.get(url)



        # Verifica que la respuesta sea exitosa
        if response.status_code == 200:
            # Convierte la respuesta JSON a un diccionario de Python
            data = response.json()
            for result in data["result"]:
                result["id"] = self._add_prefix_to_id(result["id"])
            # Retorna los documentos de eventos
            return data
        else:
            # Maneja errores de la respuesta
            response.raise_for_status()

    def get_evento_by_id(self, event_id):
        """
        Obtiene un evento específico por su ID.

        :param event_id: ID del evento.
        :return: Evento en formato JSON.
        """
        # Construye la URL completa con la consulta por ID
        event_id = self._remove_prefix_from_id(event_id)
        url = f"{self.base_url}/{event_id}.json"

        # Realiza la petición GET al endpoint
        response = requests.get(url)

        # Verifica que la respuesta sea exitosa
        if response.status_code == 200:
            # Convierte la respuesta JSON a un diccionario de Python
            data = response.json()
            # Retorna el documento del evento
            docs = data.get('response', {}).get('docs', [])
            return docs[0] if docs else None
        else:
            # Maneja errores de la respuesta
            response.raise_for_status()
