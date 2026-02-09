# P2: Convert Numbers

## Descripción
Programa que extrae los últimos dos dígitos decimales de números y los convierte a binario y hexadecimal.

## Requisitos Implementados

1. ✓ Invocación desde línea de comandos
2. ✓ Recibe archivo como parámetro
3. ✓ Convierte números a binario y hexadecimal
4. ✓ Resultados en pantalla y archivo
5. ✓ Algoritmos básicos (sin funciones built-in)
6. ✓ Manejo de datos inválidos
7. ✓ Nombre: convert_numbers.py
8. ✓ Formato de invocación mínimo
9. ✓ Maneja cientos a miles de datos
10. ✓ Incluye tiempo de ejecución
11. ✓ Cumple con PEP-8

## Uso

```bash
python convert_numbers.py fileWithData.txt
```

## Ejemplo de Salida

```
Processing file: P2_TC1.txt

======================================================================
NUMBER CONVERSION REPORT
======================================================================
Index   Decimal        Last 2    Binary         Hex       
----------------------------------------------------------------------
1       6980368        68        1000100        44        
2       5517055        55        110111         37        
3       1336159        59        111011         3B        
4       6750185        85        1010101        55        
5       1771937        37        100101         25        
... and 195 more
======================================================================
Total numbers processed: 200
Elapsed Time: 0.001234 seconds
======================================================================
```

## Casos de Prueba Ejecutados

| Test Case | Cantidad de Datos | Características | Estado |
|-----------|------------------|-----------------|---------|
| TC1       | 200             | Números positivos | ✓ PASS  |
| TC2       | 200             | Números positivos | ✓ PASS  |
| TC3       | 200             | Incluye negativos y cero | ✓ PASS  |
| TC4       | ~197            | Datos inválidos | ✓ PASS  |

**Resultado: 4/4 casos de prueba correctos (100%)**

## Algoritmos Implementados

### Conversión a Binario
```python
def decimal_to_binary(num):
    binary = ""
    while num > 0:
        remainder = num % 2
        binary = str(remainder) + binary
        num = num // 2
    return binary
```

### Conversión a Hexadecimal
```python
def decimal_to_hexadecimal(num):
    hex_digits = "0123456789ABCDEF"
    hexadecimal = ""
    while num > 0:
        remainder = num % 16
        hexadecimal = hex_digits[remainder] + hexadecimal
        num = num // 16
    return hexadecimal
```

### Extracción de Últimos Dos Dígitos
```python
last_two = abs(number) % 100
```

## Lógica del Programa

1. Lee cada número del archivo
2. Extrae los últimos dos dígitos decimales usando módulo 100
3. Convierte esos dos dígitos a binario
4. Convierte esos dos dígitos a hexadecimal
5. Guarda y muestra los resultados

## Ejemplo de Conversión

Número: 6980368
- Últimos 2 dígitos: 68
- 68 en binario: 1000100
- 68 en hexadecimal: 44

## Verificación PEP-8

El código cumple con todos los lineamientos de PEP-8:
- ✓ Nombres de funciones en snake_case
- ✓ Líneas menores a 79 caracteres
- ✓ Docstrings completos
- ✓ Espaciado apropiado
- ✓ Importaciones organizadas

## Manejo de Errores

- Archivo no encontrado
- Datos no numéricos (ej: "ABC", "ERR")
- Archivo vacío
- Errores de escritura
- Números negativos (maneja el valor absoluto)

## Archivos Generados

- `ConvertionResults.txt`: Contiene todas las conversiones
- `TC*_execution.log`: Logs de cada ejecución de prueba
- `TC*_ConvertionResults.txt`: Resultados específicos de cada caso de prueba
