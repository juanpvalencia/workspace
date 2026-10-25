# Karatsuba Algorithm Performance Dataset

## Descripción del Dataset
El conjunto de datos está conformado por **40 registros experimentales**, donde cada registro representa una ejecución del algoritmo de multiplicación de números enteros de **Karatsuba**. 

En cada registro se almacenan las siguientes variables semánticas:
* `recordId`: Identificador único del registro.
* `operandX` y `operandY`: Operadores de entrada utilizados en la multiplicación.
* `digitCountX` y `digitCountY`: Cantidad de dígitos de cada operador.
* `executionTimeMs`: Tiempo de ejecución requerido con alta precisión medido en milisegundos para completar la operación.
* `algorithmResult`: Resultado matemático obtenido de la multiplicación.

El conjunto de datos ha sido estructurado y publicado utilizando un **grafo RDF serializado en formato Turtle (`.ttl`)**. Este dataset permite analizar el comportamiento del tiempo de ejecución en función del tamaño de los operandos, identificar posibles tendencias de rendimiento y realizar comparaciones entre algoritmos de multiplicación.

---

## Contexto
El dataset fue desarrollado como parte de una actividad académica enfocada en la publicación de datasets en la Web para la **Maestría en Computación** de la **Universidad del Cauca**. 

Su propósito principal es analizar el comportamiento de un algoritmo que multiplica dos factores de tipo *divide y vencerás* frente a entradas de longitud variable (desde 10 hasta 1000 dígitos), permitiendo observar la relación entre el tamaño de los factores y el tiempo de procesamiento. Adicionalmente, se demuestra el proceso completo de transformación de datos generados mediante un script de Python hacia un modelo basado en tripletas RDF (Sujeto-Predicado-Objeto), incorporando metadatos estandarizados y tipado estricto de datos (`xsd:integer`, `xsd:float`, `xsd:string`).

---

## Autores y Afiliación
* **Juan Pablo Valencia Rosada**
* **Jhony Arvey Muñoz Navia**

**Institución:** Universidad del Cauca — Maestría en Computación

---

## Herramienta y Entorno de Generación
Los datos se generaron utilizando **Python 3.10.8** mediante un flujo de procesamiento automatizado:

* **Librerías nativas de Python:**
  * `random`: Para la generación seudoaleatoria de los factores con semillas controladas (`random.seed(42)`), garantizando la reproducibilidad exacta de los experimentos.
  * `time`: Empleada para la medición de tiempos de ejecución de alta precisión a nivel de microsegundos (`time.perf_counter()`).
  * `sys`: Utilizada para ampliar el límite de conversión de enteros a cadenas (`sys.set_int_max_str_digits`).
* **Librería de Web Semántica:**
  * `rdflib`: Empleada para la construcción del grafo RDF, definición de prefijos, asignación de tipados estrictos de datos y la exportación final del archivo en formato Turtle (`.ttl`).
* **Algoritmo:**
  * Implementación recursiva optimizada del algoritmo de Karatsuba para la multiplicación de enteros de gran escala.

---

## Estándar de Metadatos
El dataset hace uso del estándar **Dublin Core (`dcterms`)** combinado con **DCAT (`dcat:Dataset`)** para la descripción formal de recursos semánticos:
* `dcterms:title`
* `dcterms:description`
* `dcterms:creator`
* `dcterms:publisher`
* `dcterms:issued`
* `dcterms:license`
* `dcterms:identifier`

---

## Repositorio y Publicación
* **Código Fuente (GitHub):** [https://github.com/juanpvalencia/workspace](https://github.com/juanpvalencia/workspace)
* **Dataset Oficial y DOI:** Publicado permanentemente en Zenodo para garantizar su preservación a largo plazo y trazabilidad académica.

---

## Licencia
    Karatsuba Algorithm Performance Dataset  © 2026 by Juan Pablo Valencia Rosada and Jhony Arvey Muñoz Navia is licensed under CC BY-SA 4.0. To view a copy of this license, visit https://creativecommons.org/licenses/by-sa/4.0/


To view a copy of this license, visit [https://creativecommons.org/licenses/by-sa/4.0/](https://creativecommons.org/licenses/by-sa/4.0/)