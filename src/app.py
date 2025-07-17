from models.GetAllData import getAllData

def main():
    try:
        # Obtener datos
        data = getAllData()  # Nota los paréntesis para llamar a la función
        
        # Procesar datos
        processed_data = process_data(data)
        
        # Mostrar/iniciar aplicación con los datos
        start_application(processed_data)
        
    except Exception as e:
        print(f"Error al iniciar la aplicación: {str(e)}")
        # Podrías agregar logging aquí: logging.error(f"Error: {str(e)}")

def process_data(raw_data):
    """Función para procesar los datos obtenidos"""
    # Aquí iría tu lógica de procesamiento
    processed = raw_data  # Ejemplo básico
    return processed

def start_application(data):
    """Función principal que inicia la aplicación"""
    print("Aplicación iniciada con los siguientes datos:")
    print(data)  # En una app real, aquí iniciarías tu interfaz o proceso principal

if __name__ == "__main__":
    main()