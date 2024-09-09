# ****Curso de Python**: PIP y Entornos Virtuales**

# 1. Introducción

* 1. ## Python en tu propio entorno de desarrollo local

El objetivo de es crear y usar un entorno profesional de Python, gestionando dependencias y entornos virtuales.

* Comandos básicos en la terminal Unix.
    * **pwd**: Indica en qué ubicación estamos
    * **mkdir**: Crear una nueva carpeta
    * **ls**: Lista de archivos
    * **cd**: Nos permite abrir una carpeta
    * **clear**: Nos permite despejar la terminal
    * **git init**: Inicializar
    * **touch**: Crear archivos
* Otros comandos
    * **rm**: sirve para borrar archivos
    * **rmdir**: sirve para borrar directorios
    * **mv**: sirve para mover directorios
    * **df**: indica el espacio en disco, el disponible, usado y total

[Clase](https://platzi.com/home/clases/4261-python-pip/55120-python-en-tu-propio-entorno-de-desarrollo-local/)

2. ## Instalación en Windows (WSL) y Linux

Al igual que con cualquier lenguaje de programación serio, Python admite bibliotecas y marcos de terceros que puede instalar para evitar tener que reinventar la rueda con cada nuevo proyecto. Puede encontrarlos en un repositorio central llamado "PyPI" (Python Package Index).

Pero descargar, instalar y administrar estos paquetes a mano puede ser frustrante y llevar mucho tiempo, por lo que muchos desarrolladores de Python confían en una herramienta especial llamada PIP para que Python haga todo mucho más fácil y rápido.

¿Qué es PIP para Python?

PIP es un acrónimo que significa "Paquetes de instalación PIP" o "Programa de instalación preferida o Preferred Installer Program". Es una utilidad de línea de comandos que le permite instalar, reinstalar o desinstalar paquetes PyPI con un comando simple y directo: "pip".

Si alguna vez ha realizado algún trabajo de línea de comandos en Windows (con el símbolo del sistema) o Mac o Linux (con el Terminal y Bash), entonces te sentirás como en casa y puedes ir directamente a las instrucciones de instalación para su particular sistema operativo.

¿Se instala PIP con Python?
Si está utilizando Python 2.7.9 (o superior) o Python 3.4 (o superior), entonces PIP viene instalado con Python por defecto. Si está utilizando una versión anterior de Python, deberá seguir los pasos de instalación que se detallan a continuación. De lo contrario, salte a la parte inferior para aprender cómo comenzar a usar PIP.

Si está ejecutando Python en un entorno virtual creado con virtualenv o pyvenv, entonces PIP estará disponible para ese entorno independientemente de la versión de Python.

Comandos

    python | python3 --> ejecuta python, si no esta instalado lo instala
    exit() --> para salir de la interfaz de python
    python -V --> ver la version de python
    pip -V --> ver version de pip

[Clase](https://platzi.com/home/clases/4261-python-pip/55122-instalacion-en-windows-wsl-y-linux/)

* 3. ## Instalación en Mac

Comandos utilizados

* python o python3
* exit()

Normalmente viene instalado en Mac, en caso de que no lo tenga continuar con estos comandos 

Herramientas de codigo

* sudo xcode-select --install
* sudo xcode-select --reset

* brew install python3 --> Instalación de python
* python3  Verificar la Instalación

[Clase](https://platzi.com/home/clases/4261-python-pip/55123-instalacion-en-mac/)

* 4. ## Python con VSCode

Vamos a utilizar el editor de código más utilizado en este momento: Visual Studio Code.

Es un editor liviano en el cual podemos instalar extensiones a medida que necesitemos.

Extensiones a instalar:
1. Python
2. WSL (Windows Subsystem for Linux)

* 5. ## Python con Git y GitHub

* 6. ## Flujo de trabajo en Python

Para ejecutar un script de Python:

```bash
python script.py
```

En un repositorio en GitHub en el **README.md** debemos explicar **que es** el proyecto y **como ejecutarlo**. Documentar el proyecto.

* 7. ## ¿Qué es PIP?

Una de las cosas más interesantes de Python es su ecosistema de frameworks y librerías, que podemos usar para crear nuestros proyectos, así no reinventar la rueda para solucionar ciertos problemas en específico.

Todos estos paquetes los encontramos de forma pública en PyPI (Python Package Index)

**PIP: Preferred Installer Program**. Es una utilidad de línea de comandos que le permite instalar, reinstalar o desinstalar paquetes PyPI con un comando simple y directo: "pip".

    pip -V --> verificamos tener pip, que version

**PyPI** : https://pypi.org/
    
* Aca podemos buscar los paquetes, entrar y ver como se instalan. Suele ser de la forma:

        pip install package_name

Por ejemplo *matplotlib*: es una biblioteca integral para crear visualizaciones estáticas, animadas e interactivas en Python. Se instala:

    pip install matplotlib

### Comandos PIP

    pip freeze -> vemos los paquetes instalados en el entorno global de Python

* 8. ## Gráficas en Python con PIP

* 9. ## ¿Qué es un entorno virtual?

Instalar a nivel global puede causar distintos problemas al momento de manejar diferentes proyectos, por ejemplo para algunos proyectos necesitaras otro tipo de version, libreria o modulos y para solucionar esto se creo un ambiente virtual en python el cual encapsula cada proyecto y no lo deja de forma compartida.

<img src="./img/entornos_virtuales.png">

### **¿Qué es un entorno virtual en Python?**

Un entorno virtual (o ambiente virtual) en el contexto de Python es una herramienta que te permite **crear un espacio aislado** en tu sistema donde puedes **instalar paquetes y dependencias de Python sin afectar** el entorno global de Python en tu máquina.

### Beneficios de los entornos virtuales:

* **Aislamiento**: Cada entorno virtual es independiente y aísla las bibliotecas y paquetes que instalas en él.
* **Gestión de dependencias**: Facilita la especificación de dependencias necesarias para tu proyecto en un archivo requirements.txt.
* **Evitar conflictos**: Previene que las bibliotecas de un proyecto afecten a otros proyectos o al entorno global de Python.
* **Limpieza y organización**: Permite una gestión ordenada y eliminación de entornos virtuales no utilizados.

* 10. ## Usando entornos virtuales en Python

**READ** --> https://docs.python.org/3/library/venv.html

Para crear un entorno virtual ejecutamos el comando

    #              (venv_directory) --> contendra todo el venv
    python -m venv venv

Ahora tenemos que activar el ambiente

    source ./venv/Scripts/activate

Ahora podemos ver con ```pip freeze``` que no hay librerias instaladas y con which python que apunta al venv.
Tenemos un entorno aislado.

Para salir del ambiente virtual ejecutamos

    deactivate

* 11. ## requeriments.txt

El archivo requeriments.txt en un proyecto contiene las dependencias del proyecto y que versiones de estas dependencias.

Para crear este archivo:

    pip freeze > requeriments.txt

Para instalar la lista de dependencias:

    pip install -r requeriments.txt

* 12. ## Solicitudes HTTP con Requests

Una de las librerías mas usadas de Python es:

* **Requests**

    Se encarga de hacer peticiones a otro tipo de servidores web desde Python.

Empezamos un proyecto nuevo que consultará APIs llamado web-server.

1. Creamos el directorio:
        
        mkdir web-server

2. Creamos el entorno virtual y lo activamos:

        python -m venv venv
        source ./venv/Scripts/activate

3. Chequeamos que el proyecto quedo aislado y listo para empezar a instalar dependencias:

        pip freeze

4. Instalamos las dependencias necesarias:

        pip install requests

5. Listamos las dependencias en un archivo para mejorar la documentacióny divulgación del proyecto.

        pip freeze > requeriments.txt

6. No olvides hacer todo esto con un sistema de control de versiones como Git y documentar el proyecto.
