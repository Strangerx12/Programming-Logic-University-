```markdown
# Animación de Merge Sort con Pygame

## 📌 Descripción
Este repositorio contiene una implementación visual e interactiva del algoritmo de ordenamiento **Merge Sort**, desarrollada en Python utilizando la librería gráfica Pygame. El proyecto aplica el paradigma de "Divide y vencerás", permitiendo observar paso a paso cómo se fraccionan y combinan los datos hasta quedar completamente ordenados.

Para garantizar una arquitectura de software limpia y escalable, el código se ha modularizado separando estrictamente la lógica matemática del renderizado gráfico mediante el uso de generadores (`yield`).

Como característica visual distintiva, el sistema genera una "escalera" de valores perfectos que luego es barajada aleatoriamente. Al finalizar el algoritmo, las barras se reorganizan formando una línea diagonal continua e impecable.

## 📁 Estructura del Proyecto

El proyecto sigue una organización modular:
* `src/main.py`: Punto de entrada de la aplicación y gestor del bucle de eventos.
* `src/merge_sort.py`: Lógica pura del algoritmo aislando la recursión y el control de estados.
* `src/visualizer.py`: Configuración del entorno gráfico, colores y escalado dinámico de las barras.

## ⚙️ Instalación y Ejecución

Para probar este proyecto en tu entorno local (recomendado desde la terminal integrada de Visual Studio Code), sigue estos pasos:

1. **Clonar el repositorio principal y entrar a la carpeta:**
   ```bash
   git clone [https://github.com/Strangerx12/Programming-Logic-University-.git](https://github.com/Strangerx12/Programming-Logic-University-.git)
   cd "Programming-Logic-University-/Merge Sort Animation"

```

2. **Instalar dependencias:**
```bash
pip install -r requirements.txt

```


3. **Ejecutar la animación:**
```bash
python src/main.py

```


*(Nota: En algunos entornos de Windows, si el comando anterior abre la tienda de Microsoft, utiliza `py src/main.py` o ejecuta el archivo usando el botón de "Play" en la esquina superior derecha de Visual Studio Code).*

## 🎮 Controles de Interfaz

Una vez abierta la ventana de Pygame, puedes interactuar con los siguientes comandos:

* **`ESPACIO`**: Inicia la animación de ordenamiento.
* **`R`**: Reinicia el arreglo, generando una nueva escalera desordenada.

## 🎨 Leyenda de Colores en la Animación

Durante la ejecución visual, las barras cambian de color para mostrar qué está haciendo el algoritmo en tiempo real:

* 🟦 **Azul**: Estado natural de los elementos en espera.
* 🟥 **Rojo**: Elementos que se están comparando en ese instante exacto (evaluando cuál es menor entre la mitad izquierda y derecha).
* 🟩 **Verde**: Elementos que acaban de ser ubicados en su posición correcta durante la fase de mezcla (`merge`) o que ya están ordenados al finalizar.

## 📊 Análisis de Complejidad: Merge Sort

El algoritmo implementado destaca por su alta eficiencia en grandes volúmenes de datos en comparación con métodos elementales (como Burbuja o Selección).

* **Complejidad Temporal:** $O(n \log n)$. Constante en sus tres escenarios (peor, promedio y mejor caso). La división recursiva del arreglo toma tiempo logarítmico ($\log n$), mientras que la función de mezcla (`merge`) recorre los elementos en tiempo lineal ($n$).
* **Complejidad Espacial:** $O(n)$. Al no ser un algoritmo *in-place*, requiere memoria adicional proporcional al tamaño del arreglo original para almacenar las sublistas temporales.
* **Estabilidad:** Es un algoritmo **estable**, asegurando que los elementos con claves idénticas mantengan su orden original tras finalizar el proceso.

```

```
