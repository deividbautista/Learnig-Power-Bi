import os

def savDocDataP(df, folderName, fileName):

    if df.empty:
        print("Data frame empty")

    else:
        if not os.path.exists(folderName):
            # Creamos la carpeta
            os.makedirs(folderName)

        # Usamos la ruta de la carpeta y el nombre del archivo
        filePath = os.path.join(folderName, fileName)
        df.to_json(filePath, orient="records")

def savDocDataM(data, fileName):

    output_path = f"../data/{fileName}.json"

    # Crear directorio si no existe
    output_dir = os.path.dirname(output_path)
    os.makedirs(output_dir, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(data)
