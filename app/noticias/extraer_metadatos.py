from newspaper import Article

def extraer_metadatos(url:str):
    article = Article(url)
    article.download()
    article.parse()
    return {
        "titulo":article.title,
        "fecha_de_publicacion":article.publish_date,
        "nombre_del_autor":article.authors
    }