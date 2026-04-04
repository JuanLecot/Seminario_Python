def obtener_tendencias(posts):
    lista_palabras =[]
    for post in posts:
        lista_palabras += post.split()
    lista_de_hashtags = [words for words in lista_palabras if "#" in words]
    contar_unicos = 0
    lista_trend = []
    for trend in lista_de_hashtags:
        if lista_de_hashtags.count(trend) > 1:
            lista_trend.append((trend,lista_de_hashtags.count(trend)))
        else:
            contar_unicos+=1
    lista_trend.append(("Total de Hashtags únicos: ",contar_unicos))

    return set(lista_trend)