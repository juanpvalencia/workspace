# Karatsuba Algorithm Performance Dataset

## Descripción del Dataset
El conjunto de datos está conformado por **40 registros experimentales**, donde cada registro representa una ejecución del algoritmo de multiplicación de números enteros de **Karatsuba**. 

El conjunto de datos ha sido estructurado y publicado utilizando un **grafo RDF serializado en formato Turtle (`.ttl`)**. Este dataset permite analizar el comportamiento del tiempo de ejecución en función del tamaño de los operandos, identificar posibles tendencias de rendimiento y realizar comparaciones entre algoritmos de multiplicación.

---
## Variables
| Variable | Tipo de Dato | Descripción | Ejemplo |
| :--- | :--- | :--- | :--- |
| `recordId` | integer / URI | Identificador único del registro en el dataset. | `1` |
| `operandX` | integer | Primer factor de multiplicación de entrada. | `483921` |
| `operandY` | integer | Segundo factor de multiplicación de entrada. | `928103` |
| `digitCountX` | integer | Longitud en dígitos del primer operando. | `6` |
| `digitCountY` | integer | Longitud en dígitos del segundo operando. | `6` |
| `executionTimeMs` | Decimal (Float) | Tiempo de ejecución de la función en milisegundos. | `0.0342` |
| `algorithmResult` | integer | Resultado de la operación. | `449128531863` |

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

## Repositorio
* **Código Fuente (GitHub):** [https://github.com/juanpvalencia/workspace](https://github.com/juanpvalencia/workspace)

## Publicación
El dataset final serializado en formato RDF/Turtle (`.ttl`) se encuentra permanentemente archivado y publicado en Zenodo bajo el siguiente DOI:

> **DOI:** [10.5281/zenodo.23629651](https://doi.org/10.5281/zenodo.23629651)

---

## Licencia
    Karatsuba Algorithm Performance Dataset  © 2026 by Juan Pablo Valencia Rosada and Jhony Arvey Muñoz Navia is licensed under CC BY-SA 4.0. To view a copy of this license, visit https://creativecommons.org/licenses/by-sa/4.0/


To view a copy of this license, visit [https://creativecommons.org/licenses/by-sa/4.0/](https://creativecommons.org/licenses/by-sa/4.0/)
