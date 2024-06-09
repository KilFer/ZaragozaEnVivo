import json
from libraries.eventSources.ayto_zaragoza import AytoZaragoza


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    zev = AytoZaragoza()

    eventos = zev.get_eventos(rows=10)

    print("Información de eventos:")
    print(json.dumps(eventos, indent=2, ensure_ascii=False))

