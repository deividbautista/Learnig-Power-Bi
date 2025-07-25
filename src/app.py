from models.ctoMongo import ConMongo
from models.SaveDataDoc import savDocDataM

def main():

    print("iniciando")
    SfileName = input("Por favor ingrese con que nombre desea guardar el archivo .json: \n")

    try:
        data=ConMongo() 
        fileName = SfileName # Nota los paréntesis para llamar a la función        
        savDocDataM(data, fileName)

    except Exception as e:
        print(f"Error al iniciar la aplicación: {str(e)}")
        # Podrías agregar logging aquí: logging.error(f"Error: {str(e)}")
if __name__ == "__main__":
    main()