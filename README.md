# Py2DMaker  

**Py2DMaker** es una herramienta diseñada para facilitar la creación de mapas de videojuegos en 2D. Permite cargar personajes y sus respectivos sprites, gestionar elementos y posicionarlos en el mundo de forma intuitiva. Con una integración avanzada con **Pygame**, los desarrolladores pueden usar esta plantilla para construir y probar juegos sin necesidad de comenzar desde cero.  

## **Características principales**  

1. **Gestión de personajes y recursos gráficos**:  
   - Carga de personajes y sprites desde la carpeta `assets/`.  
   - Organización de recursos gráficos, incluyendo fondos y otros elementos.  

2. **Modo construir**:  
   - Herramienta visual para agregar personajes, jugadores y otros assets al mapa.  
   - Edición de posiciones y características de los objetos directamente en la interfaz gráfica.  

3. **Integración con Pygame**:  
   - Corre el mundo creado en un entorno Pygame para probar la interacción de los elementos en tiempo real.  

4. **Exportación del mapa**:  
   - Guardado de las posiciones y configuraciones de los elementos en la carpeta `saves/`.  
   - Carga y edición de mapas previamente creados.  

## **Estructura del proyecto**  

```
Py2DMaker/  
│  
├── main.py                    # Punto de entrada de la aplicación  
│  
├── assets/                    # Recursos gráficos y multimedia  
│   ├── characters/            # Sprites de personajes  
│   ├── backgrounds/           # Sprites de fondos  
│   └── icons/                 # Íconos y otros recursos visuales  
│  
├── saves/                     # Guardado de posiciones y partidas  
│  
├── gui/                       # Interfaz gráfica  
│   ├── main_window.py         # Ventana principal  
│   ├── assets_window.py       # Ventana de gestión de assets  
│   └── build_mode_window.py   # Ventana o clase para el modo construir  
│  
├── utils/                     # Funciones adicionales  
│   ├── file_manager.py        # Manejo de archivos  
│   ├── preview_loader.py      # Carga y previsualización de sprites  
│   ├── colors.py              # Constantes de colores  
│   ├── metodos.py             # Métodos adicionales y utilidades  
│   └── test/                  # Pruebas y notificaciones  
│       └── notify.py          # Notificaciones de éxito, error, etc.  
│  
├── DATA/                      # Gestión de datos  
│   ├── DB/                    # Archivos de base de datos (SQLite)  
│   ├── DAO/                   # Capa de acceso a datos  
│   │   └── database_manager.py # Gestión de la base de datos  
│   └── migrations/            # Scripts SQL de migración  
│  
├── tests/                     # Pruebas unitarias y funcionales  
│   ├── keys.key               # Archivo de claves para pruebas  
│   └── test_main.py           # Archivo de pruebas de la GUI  
│  
├── .vscode/                   # Configuración de Visual Studio Code  
│   └── launch.json            # Configuración de lanzamiento para depuración  
│  
├── README.md                  
├── requirements.txt           # Dependencias del proyecto  
├── LICENSE                    # Licencia del proyecto  
└── .gitignore                 
```  

## **Requisitos del sistema**  

- **Python**: 3.10 o superior.  
- **Dependencias principales**:  
  - [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter): Para la interfaz gráfica.  
  - [Pygame](https://www.pygame.org/): Para la ejecución de los mapas creados.  
- **Sistema operativo compatible**: Windows, Linux, macOS.  

Para instalar las dependencias, utiliza el archivo `requirements.txt`:  
```bash  
pip install -r requirements.txt  
```  

## **Uso del proyecto**  

1. **Inicio del programa**:  
   Ejecuta el archivo `main.py` para iniciar la aplicación.  
   ```bash  
   python main.py  
   ```  

2. **Gestión de assets**:  
   - Carga los sprites de personajes, fondos o íconos en las carpetas correspondientes dentro de `assets/`.  
   - Utiliza la ventana de gestión de assets para asignar sprites a personajes.  

3. **Modo construir**:  
   - Accede al modo construir para agregar elementos al mapa.  
   - Organiza personajes, jugadores y otros elementos gráficamente.  

4. **Prueba del mapa**:  
   - Ejecuta el mundo creado en Pygame para interactuar con él.  
   - Ajusta y guarda las configuraciones necesarias para reutilizarlas.  

5. **Guardado y carga**:  
   - Guarda el mapa en formato compatible con Pygame en la carpeta `saves/`.  
   - Carga mapas previamente creados para editarlos o continuarlos.  

## **Cómo colaborar**  

1. **Clona el repositorio**:  
   ```bash  
   git clone https://github.com/Dekstro999/Py2DMaker  
   cd Py2DMaker  
   ```  

2. **Instala las dependencias**:  
   ```bash  
   pip install -r requirements.txt  
   ```  

3. **Explora las tareas pendientes**:  
   - Revisa la lista de *issues* en el repositorio de GitHub.  
   - Contribuye en áreas como:  
     - Mejoras en el diseño del modo construir.  
     - Integración avanzada con Pygame.  
     - Implementación de exportaciones de mapas.  
     - Implementación de pruebas unitarias y funcionales.  

4. **Usa el depurador**:  
   Recomendamos usar el depurador configurado en `launch.json` para depurar el proyecto desde Visual Studio Code.  
   ```  
   Depurador de Python: Py2DMaker (main.py)  
   ```  

5. **Envía un pull request**:  
   - Trabaja en una nueva rama con tu mejora o funcionalidad.  
   - Envía tu PR detallando los cambios realizados.  

## **Roadmap**  

### Fase 1: Configuración inicial y estructura del proyecto  
- [X] Creación de la estructura de carpetas del proyecto.  
- [X] Configuración inicial de la base de datos.  
- [X] Implementación básica de la interfaz gráfica.  
- [X] Sistema de notificaciones.  

### Fase 2: Gestión de personajes y recursos  
- [X] Implementación de la funcionalidad para agregar personajes.  
- [ ] Implementación de la funcionalidad para agregar sprites a los personajes.  
- [ ] Implementación de la funcionalidad para agregar objetos al mapa.  
- [ ] Implementación de la previsualización de sprites.  

### Fase 3: Modo construir y edición de mapas  
- [ ] Implementación del modo construir.  
- [ ] Herramientas para posicionar y editar personajes y objetos en el mapa.  
- [ ] Guardado de posiciones y configuraciones del mapa.  
- [ ] Carga de mapas desde archivos guardados.  

### Fase 4: Integración y pruebas  
- [ ] Generar entornos Pygame para probar los mapas.  
- [ ] Implementación de pruebas unitarias y funcionales.  
- [ ] Compatibilidad con diferentes resoluciones y configuraciones.  

### Fase 5: Ampliación y documentación  
- [ ] Soporte para expansiones/modificaciones externas.  
- [ ] Documentación avanzada para desarrolladores.  
- [ ] Tutoriales y ejemplos de uso.  

---  
