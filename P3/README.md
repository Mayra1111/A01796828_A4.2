# P3: Word Count

## Descripción
Programa que cuenta la frecuencia de palabras distintas en un archivo de texto.

## Requisitos Implementados

1. ✓ Invocación desde línea de comandos
2. ✓ Recibe archivo como parámetro
3. ✓ Identifica palabras distintas y su frecuencia
4. ✓ Resultados en pantalla y archivo
5. ✓ Algoritmos básicos (sin librerías especializadas)
6. ✓ Manejo de datos inválidos
7. ✓ Nombre: word_count.py
8. ✓ Formato de invocación mínimo
9. ✓ Maneja cientos a miles de palabras
10. ✓ Incluye tiempo de ejecución
11. ✓ Cumple con PEP-8

## Uso

```bash
python word_count.py fileWithData.txt
```

## Ejemplo de Salida

```
Processing file: P3_TC1.txt

============================================================
WORD FREQUENCY REPORT
============================================================
Word                          Frequency      
------------------------------------------------------------
achievement                   1              
adequate                      1              
adventures                    1              
anal                          1              
andrews                       1              
assessed                      1              
bedding                       1              
blues                         1              
buying                        1              
cartridge                     1              
... and 90 more
============================================================
Total words: 100
Distinct words: 99
Elapsed Time: 0.000234 seconds
============================================================
```

## Casos de Prueba Ejecutados

| Test Case | Palabras Totales | Palabras Distintas | Estado |
|-----------|-----------------|-------------------|---------|
| TC1       | 100            | 99                | ✓ PASS  |
| TC2       | 184            | 144               | ✓ PASS  |
| TC3       | 500            | 487               | ✓ PASS  |
| TC4       | 1,000          | 949               | ✓ PASS  |
| TC5       | 5,000          | 3,750             | ✓ PASS  |

**Resultado: 5/5 casos de prueba correctos (100%)**

## Algoritmos Implementados

### Conteo de Frecuencias
```python
def count_word_frequencies(words):
    frequency = {}
    for word in words:
        word_lower = word.lower()
        frequency[word_lower] = frequency.get(word_lower, 0) + 1
    return frequency
```

### Ordenamiento Alfabético (Bubble Sort)
```python
def sort_word_frequencies(frequency):
    items = list(frequency.items())
    n = len(items)
    for i in range(n):
        for j in range(0, n - i - 1):
            if items[j][0] > items[j + 1][0]:
                items[j], items[j + 1] = items[j + 1], items[j]
    return items
```

## Características del Programa

### Procesamiento de Palabras
- Lectura línea por línea
- División por espacios en blanco
- Conversión a minúsculas (case-insensitive)
- Conteo de frecuencias

### Ordenamiento
- Bubble sort para ordenamiento alfabético
- No utiliza funciones built-in de ordenamiento
- Complejidad O(n²)

### Salida
- Palabras ordenadas alfabéticamente
- Frecuencia de cada palabra
- Estadísticas totales:
  - Total de palabras
  - Palabras distintas
  - Tiempo de ejecución

## Ejemplo de Análisis

Entrada:
```
apple banana apple orange banana apple
```

Salida:
```
Word                          Frequency      
apple                         3              
banana                        2              
orange                        1              

Total words: 6
Distinct words: 3
```

## Verificación PEP-8

El código cumple con todos los lineamientos de PEP-8:
- ✓ Nombres de funciones en snake_case
- ✓ Líneas menores a 79 caracteres
- ✓ Docstrings completos
- ✓ Espaciado apropiado
- ✓ Importaciones organizadas

## Manejo de Errores

- Archivo no encontrado
- Líneas con errores de procesamiento
- Archivo vacío
- Errores de escritura
- Caracteres especiales

## Archivos Generados

- `WordCountResults.txt`: Contiene el reporte completo de frecuencias
- `TC*_execution.log`: Logs de cada ejecución de prueba
- `TC*_WordCountResults.txt`: Resultados específicos de cada caso de prueba

## Complejidad

- Lectura: O(n) donde n es el número de palabras
- Conteo: O(n)
- Ordenamiento: O(m²) donde m es el número de palabras distintas
- Complejidad total: O(n + m²)
