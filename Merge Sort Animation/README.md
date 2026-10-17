# Animación de Merge Sort con Pygame

## 📌 Descripción
Este repositorio contiene una implementación visual e interactiva del algoritmo de ordenamiento **Merge Sort**, desarrollada en Python utilizando la librería gráfica Pygame. El proyecto aplica el paradigma de "Divide y vencerás", permitiendo observar paso a paso cómo se fraccionan y combinan los datos hasta quedar completamente ordenados.

Para garantizar una arquitectura de software limpia y escalable, el código se ha modularizado separando estrictamente la lógica matemática del renderizado gráfico mediante el uso de generadores (`yield`).

## 📁 Estructura del Proyecto

El repositorio sigue una organización modular:
* `src/main.py`: Punto de entrada de la aplicación y gestor del bucle de eventos.
* `src/merge_sort.py`: Lógica pura del algoritmo aislando la recursión y el control de estados.
* `src/visualizer.py`: Configuración del entorno gráfico, colores y escalado dinámico de las barras.

## ⚙️ Instalación y Ejecución

Para probar este proyecto en tu entorno local (recomendado desde la terminal integrada de Visual Studio Code), sigue estos pasos:

1. **Clonar el repositorio:**
   ```bash
   git clone <AQUÍ_PONES_EL_LINK_DE_TU_REPO>
   cd merge_sort_animation