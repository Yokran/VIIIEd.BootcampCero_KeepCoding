## proyecto Flask classic - MyCrypto

### PASOS PRE INSTALACIÓN:

A través del siguiente enlace accedemos a la pagina de descarga de la aplicación dbBruwser
https://download.sqlitebrowser.org/DB.Browser.for.SQLite-3.12.2-win32.msi

Descargamos la versión correspondiente con el Sistema Operativo que estemos utilizando.
Una vez descargado el instalador, lo ejecutamos y seguimos los pasos del asistente de instalación.

Nos dirigimos a la url https://coinmarketcap.com/api/ y seguimor los pasos indicados para obtener nuestra API KEY del sitio web de CoinMarketCap.

### INSTALACIÓN
Copiamos la carpeta que contiene este fichero en el directorio desde dónde deseamos ejecutar el programa.

Creamos la base de datos:
Abrimos el programa dbBrowser, desde Archivo, seleccionaremos la opción "Importar" y a continuación elegiremos hacerlo desde "base de datos de archivo SQL".
Elegiremos el archivo movimientos.sql, ubicado en la carpeta migrations del directorio raíz del programa.
En el directorio raíz del programa crearemos una nueva carpeta que nombraremos como queramos e importaremos en su interior la base de datos poniendole también el nombre que que elijamos.

        La instalación de la base de datos se puede llevar a cabo desde el terminal sin necesidad de utilizar dbBrowser e introduciendo la siguiente secuencia de comandos, pero el administrador considera oportuno servirse de la misma para una ejecución más amigable:
        cd <dir_app>
        mkdir data
        cd data
        sqlite3 movimientos.db
        .read ../migrations/movimientos.sql
        .tables
        .q

Situandonos en la ruta correspondiente, desde el terminal de comandos del sistema, ejecutamos la siguiente secuencia de comandos:
--> Creamos el entorno virtual:
- python -m venv venv
--> Activamos el entorno virtual
- venv\Scripts\activate (Windows)
- . venv/bin/activate (Linux/MacOS)
-->Instalamos las dependencias:
pip install -r requirements.txt

Creamos las variables de entorno renombrando el fichero .env_template como .env.
Dentro del fichero, elegimos si queremos que la versión del programa se ejecute en desarrollo o producción eliminando el resto de opciones.
Ejemplos:
FLASK_ENV=development          FLASK_ENV=production

Renombramos el fichero config_template.py como config.py. Dentro del fichero, informamos la SECRET_KEY (esta podrá ser cualquier combinación alfanumerica que elija), la API_KEY y la RUTA_BASE_DATOS, esta última con el nombre de la raíz correspondiente y el nombre de la carpeta y fichero con el que hallamos renombrado nuestra base de datos al importarla.

Desde el terminal, ejecutamos el siguiente comando:
- flask run

Abrimos el navegador e introducimos la url http://127.0.0.1:5000


Administrador y desarrollador, D. José David Ortiz Cruz Aka. Yokran