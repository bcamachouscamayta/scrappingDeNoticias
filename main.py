from app.noticias.extraer_metadatos import extraer_metadatos
def main():
    noticia=extraer_metadatos("https://www.lanacion.com.ar/economia/dolar/dolar-caen-las-cotizaciones-oficiales-tras-los-anuncios-de-bessent-nid13102025/")
    print(noticia)

if __name__=="__main__":
    main()
