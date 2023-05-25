def crearTabla(dataframe,nombre):
    archivoHTML=dataframe.to_html()
    archivo=open(f"./tablas/{nombre}.html","w")
    archivo.write('''
    <!DOCTYPE html>
    <html>
    <head>
    <title>Tabla con Bootstrap</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0/dist/css/bootstrap.min.css">
    </head>
    <body>
    ''')
    archivo.write(archivoHTML)
    archivo.write('''
    </body>
    </html>
    ''')
    archivo.close()