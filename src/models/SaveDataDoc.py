import os

def savDocData(df, folderName, fileName):

    if df.empty:
        print("Data frame empty")

    else:
        if not os.path.exists(folderName):
            # Creamos la carpeta
            os.makedirs(folderName)

        # Usamos la ruta de la carpeta y el nombre del archivo
        filePath = os.path.join(folderName, fileName)
        df.to_json(filePath, orient="records")
