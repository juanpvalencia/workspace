import random
import sys
import time
import datetime
from rdflib import Graph, Literal, Namespace, RDF, XSD
from rdflib.namespace import (DCTERMS,)

# Aumentar el límite de conversión de enteros a cadenas en Python
sys.set_int_max_str_digits(10000)


def karatsuba(x: int, y: int) -> int:
  """Implementación del algoritmo de Karatsuba.

  Caso base: para números pequeños (ej. < 10), se usa multiplicación directa.
  """
  if x < 10 or y < 10:
    return x * y

  # Determinar la longitud del número más grande
  n = max(len(str(x)), len(str(y)))
  m = n // 2

  # Dividir x e y en partes alta (high) y baja (low)
  high1, low1 = divmod(x, 10**m)
  high2, low2 = divmod(y, 10**m)

  # 3 llamadas recursivas
  z0 = karatsuba(low1, low2)
  z1 = karatsuba(low1 + high1, low2 + high2)
  z2 = karatsuba(high1, high2)

  # Recombinación
  return (z2 * (10 ** (2 * m))) + ((z1 - z2 - z0) * (10**m)) + z0


def generate_dataset(num_records: int = 40):
  dataset = []
  random.seed(42)  # Semilla para que los resultados sean reproducibles

  # Generamos tamaños de dígitos distribuidos en un rango representativo
  # Desde 10 dígitos (control) hasta 1000 dígitos (gran escala)
  digit_steps = [int(x) for x in range(10, 1001, max(1, 1000 // num_records))]

  for i, digits in enumerate(digit_steps, start=1):
    digits_x = digits
    digits_y = digits

    x = random.randint(10 ** (digits_x - 1), (10**digits_x) - 1)
    y = random.randint(10 ** (digits_y - 1), (10**digits_y) - 1)

    # Medir tiempo con alta precisión usando time.perf_counter()
    start_time = time.perf_counter()
    resultado = karatsuba(x, y)
    end_time = time.perf_counter()

    execution_time_ms = (
        end_time - start_time
    ) * 1000  # Convertir a milisegundos

    record = {
        "id": i,
        "operand_x": x,
        "operand_y": y,
        "digits_x": digits_x,
        "digits_y": digits_y,
        "execution_time_ms": round(execution_time_ms, 4),
        "result": resultado,
    }
    dataset.append(record)

  return dataset


def export_dataset_to_ttl(dataset, filename="karatsuba_dataset.ttl"):
  print("Iniciando la serialización completa a RDF (Turtle)...")

  g = Graph()

  # Puedes cambiar este dominio por un repositorio institucional o tu GitHub personal
  MY_DOMAIN = "https://github.com/juanpvalencia/workspace"
  EX = Namespace(f"{MY_DOMAIN}/raw/main/karatsuba#")
  ONT = Namespace(f"{MY_DOMAIN}/ontology#")
  DCAT = Namespace("http://www.w3.org/ns/dcat#")

  # Vincular prefijos formales al grafo
  g.bind("ex", EX)
  g.bind("ont", ONT)
  g.bind("dcat", DCAT)
  g.bind("dcterms", DCTERMS)
  g.bind("xsd", XSD)

  # Metadatos con licencia CC BY-SA 4.0
  dataset_uri = EX["KaratsubaDataset"]
  g.add((dataset_uri, RDF.type, DCAT.Dataset))
  g.add(
      (
          dataset_uri,
          DCTERMS.title,
          Literal(
              "Karatsuba Algorithm Performance Dataset", datatype=XSD.string
          ),
      )
  )
  g.add(
      (
          dataset_uri,
          DCTERMS.description,
          Literal(
              "Dataset evaluating execution times, large operands, and"
              " results for the Karatsuba multiplication algorithm. Developed"
              " for a Data Publishing practice.",
              datatype=XSD.string,
          ),
      )
  )

  # Autores
  g.add(
      (
          dataset_uri,
          DCTERMS.creator,
          Literal("Juan Pablo Valencia Rosada", datatype=XSD.string),
      )
  )
  g.add(
      (
          dataset_uri,
          DCTERMS.creator,
          Literal("Jhony Arvey Muñoz Navia", datatype=XSD.string),
      )
  )

  # Afiliación institucional
  g.add(
      (
          dataset_uri,
          DCTERMS.publisher,
          Literal(
              "Universidad del Cauca - Maestría en Computación",
              datatype=XSD.string,
          ),
      )
  )

  # Fecha y Licencia oficial Creative Commons CC BY-SA 4.0
  g.add(
      (
          dataset_uri,
          DCTERMS.issued,
          Literal(datetime.date.today().isoformat(), datatype=XSD.date),
      )
  )
  g.add(
      (
          dataset_uri,
          DCTERMS.license,
          Literal(
              "https://creativecommons.org/licenses/by-sa/4.0/",
              datatype=XSD.anyURI,
          ),
      )
  )

  # 4. Iterar sobre cada registro y añadir TODOS los campos al grafo RDF
  for record in dataset:
    exec_uri = EX[f"ExecutionRecord_{record['id']}"]

    g.add((exec_uri, RDF.type, EX["AlgorithmExecution"]))
    g.add(
        (exec_uri, EX["recordId"], Literal(record["id"], datatype=XSD.integer))
    )
    g.add(
        (
            exec_uri,
            EX["operandX"],
            Literal(record["operand_x"], datatype=XSD.integer),
        )
    )
    g.add(
        (
            exec_uri,
            EX["operandY"],
            Literal(record["operand_y"], datatype=XSD.integer),
        )
    )
    g.add(
        (
            exec_uri,
            EX["digitCountX"],
            Literal(record["digits_x"], datatype=XSD.integer),
        )
    )
    g.add(
        (
            exec_uri,
            EX["digitCountY"],
            Literal(record["digits_y"], datatype=XSD.integer),
        )
    )
    g.add(
        (
            exec_uri,
            EX["executionTimeMs"],
            Literal(record["execution_time_ms"], datatype=XSD.float),
        )
    )
    g.add(
        (
            exec_uri,
            EX["algorithmResult"],
            Literal(record["result"], datatype=XSD.integer),
        )
    )

  # 5. Guardar el archivo en formato Turtle (.ttl)
  g.serialize(destination=filename, format="turtle")
  print(f"¡Éxito! Archivo RDF guardado en: '{filename}'")


if __name__ == "__main__":
  # Generar los 40 registros con tu algoritmo
  records = generate_dataset(num_records=40)
  print(f"Se han generado {len(records)} registros exitosamente.\n")

  # Exportar a formato RDF Turtle incluyendo todos los campos
  export_dataset_to_ttl(records, "karatsuba_dataset.ttl")
