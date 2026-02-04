# 🏟️ Coliseo Interdimensional

## Tema Seleccionado
**Combates entre héroes de distintas dimensiones**

## 📖 Descripción del Proyecto
¡Prepárate para el espectáculo interdimensional definitivo! El villano **Mojo** ha adquirido una tecnología capaz de abrir agujeros interdimensionales. Usando este poder, ha capturado a héroes de distintas realidades y los ha forzado a combatir entre sí en su **Coliseo Interdimensional**. Esta aplicación te permite sumergirte en este universo, explorar a los héroes capturados y planificar los combates más épicos mientras respetas las estrictas reglas del coliseo.

## ✨ Características Principales

La aplicación web te permite gestionar todo el espectáculo del Coliseo Interdimensional:

*   **🏟️ Ver Información del Coliseo**: Conoce los detalles y la historia detrás de esta arena creada por Mojo.
*   **⚔️ Planificar un Combate**: ¡Crea el combate definitivo! Selecciona dos héroes de distintas dimensiones y define las reglas de su enfrentamiento.
*   **📋 Listar Combates Planificados**: Revisa todos los combates que has organizado y que están a la espera de comenzar.
*   **🗑️ Borrar un Combate**: Si un combate ya no es de tu interés o Mojo lo ha cancelado, puedes eliminarlo de la lista.
*   **🦸 Ver Héroes Disponibles**: Explora el catálogo completo de héroes capturados por Mojo.

## ⚖️ Reglas del Coliseo (Restricciones del Sistema)

Para mantener cierta "equidad" y espectáculo en sus juegos, Mojo ha establecido reglas inquebrantables que la aplicación hace cumplir:

### Restricción de Co-requisito
*   **Regla**: Un **héroe sin poderes necesita de un arma para combatir**.
*   **Explicación**: Los héroes que carecen de habilidades sobrehumanas dependen por completo de herramientas y armamento tecnológico o físico para tener una oportunidad en la arena. No se les permite luchar sin un arma equipada.

### Restricción de Exclusión Mutua
*   **Regla**: Un **héroe con poderes no puede usar armas para combatir**.
*   **Explicación**: Mojo cree que el uso de habilidades innatas y el uso de armas externas son filosofías de combate mutuamente excluyentes. Los héroes dotados con poderes deben confiar solo en ellos, ya que el uso de un arma podría desestabilizar o interferir con su flujo de energía natural.

### Otras Restricciones
*   **Regla**: **Héroes con poderes no pueden combatir con héroes sin poderes, y viceversa**.
*   **Explicación**: Para evitar combates "desbalanceados" y aburridos para el público interdimensional, Mojo categoriza las luchas. Los combates de "poderes vs. poderes" son espectáculos de fuerza bruta y energía, mientras que los de "tecnología vs. tecnología" son muestras de habilidad, ingenio y precisión. Estas categorías nunca se mezclan.

## 🚀 Comenzando

Sigue estos pasos para clonar y ejecutar el Coliseo Interdimensional en tu máquina local.

### Prerrequisitos

Asegúrate de tener instalado en tu sistema:
*   **Python 3.7 o superior**
*   **Git**
*   **pip** (generalmente viene con Python)

### Instalación y Ejecución

1.  **Clonar el Repositorio**
    ```bash
    git clone https://github.com/diegosct11/Coliseo-Interdimensional.git
    cd Coliseo-Interdimensional
    ```

2.  **Crear y Activar un Entorno Virtual (Recomendado)**
    Es buena práctica aislar las dependencias del proyecto.
    *   **En Windows:**
        ```bash
        python -m venv venv
        venv\Scripts\activate
        ```
    *   **En macOS/Linux:**
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

3.  **Instalar las Dependencias**
    Con el entorno virtual activado, instala las librerías necesarias:
    ```bash
    pip install streamlit pandas
    ```
    *(Opcional)* Si existe un archivo `requirements.txt`, puedes usarlo:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Ejecutar la Aplicación**
    ¡Lanza la aplicación web de Streamlit y entra al coliseo!
    ```bash
    streamlit run main.py
    ```
    Automáticamente se abrirá una pestaña en tu navegador predeterminado (generalmente en `http://localhost:8501`) mostrando la aplicación.

## 📁 Estructura del Proyecto

```
Coliseo-Interdimensional/
├── main.py                     # Archivo principal de la aplicación Streamlit
├── core.py                     # Algunas funciones de la app
├── requirements.txt            # Lista de dependencias para instalación fácil
├── data/                       # Posible carpeta para archivos de datos (CSV, JSON)
│   ├── recursos.json           # Registro de los recursos disponibles
│   └── combates.json           # Registro de combates planificados
├── images/                     # Imágenes de la app
├── pages/                      # Páginas de la app
└── README.md                   # Este archivo
```

## 🛠️ Tecnologías Utilizadas

*   **[Streamlit](https://streamlit.io/)**: Framework para crear aplicaciones web interactivas en Python de manera rápida.
*   **[Pandas](https://pandas.pydata.org/)**: Biblioteca para manipulación y análisis de datos, ideal para gestionar listas de héroes y combates.
*   **Python**: Lenguaje de programación principal.

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si deseas mejorar el Coliseo Interdimensional:

1.  Haz un Fork del proyecto.
2.  Crea una rama para tu funcionalidad (`git checkout -b feature/NuevaFuncionalidad`).
3.  Realiza tus cambios y haz commit (`git commit -m 'Añadir NuevaFuncionalidad'`).
4.  Sube tus cambios (`git push origin feature/NuevaFuncionalidad`).
5.  Abre un Pull Request.

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

---

**¡Que comiencen los juegos interdimensionales!** Si encuentras algún problema al ejecutar la aplicación o tienes ideas para nuevas funcionalidades, no dudes en contactarte con el equipo de desarrollo.