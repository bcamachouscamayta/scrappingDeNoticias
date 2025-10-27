from app.noticias.extraer_metadatos import extraer_metadatos

def test_extraer_titulo():
    respuesta = extraer_metadatos("https://www.lanacion.com.ar/economia/dolar/dolar-caen-las-cotizaciones-oficiales-tras-los-anuncios-de-bessent-nid13102025/")
    assert respuesta["titulo"] == "Tras los anuncios de Bessent, el dólar perforó los $1400 y las acciones subieron hasta 20%"