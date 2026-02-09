# P1: Compute Statistics

## Descripción
Programa que calcula estadísticas descriptivas sobre conjuntos de datos numéricos.

## Requisitos Implementados

1. ✓ Invocación desde línea de comandos
2. ✓ Recibe archivo como parámetro
3. ✓ Calcula 5 medidas estadísticas:
   - Media (Mean)
   - Mediana (Median)
   - Moda (Mode)
   - Desviación Estándar Poblacional
   - Varianza Poblacional
4. ✓ Resultados en pantalla y archivo
5. ✓ Algoritmos básicos (sin librerías estadísticas)
6. ✓ Manejo de datos inválidos
7. ✓ Nombre: compute_statistics.py
8. ✓ Formato de invocación mínimo
9. ✓ Maneja cientos a miles de datos
10. ✓ Incluye tiempo de ejecución
11. ✓ Cumple con PEP-8

## Uso

```bash
python compute_statistics.py fileWithData.txt
```

## Ejemplo de Salida

```
Processing file: P1_TC1.txt

==================================================
DESCRIPTIVE STATISTICS REPORT
==================================================
Count: 400
Mean: 242.32
Median: 239.50
Mode: 393.0
Population Std Dev: 145.258106830565566
Population Variance: 21152.799598997491557
==================================================
Elapsed Time: 0.000672 seconds
==================================================

Results saved to StatisticsResults.txt
```

## Casos de Prueba Ejecutados

| Test Case | Cantidad de Datos | Estado |
|-----------|------------------|---------|
| TC1       | 400             | ✓ PASS  |
| TC2       | 1,977           | ✓ PASS  |
| TC3       | 12,624          | ✓ PASS  |
| TC4       | 12,624          | ✓ PASS  |
| TC5       | 307             | ✓ PASS  |
| TC6       | 3,000           | ✓ PASS  |
| TC7       | 12,767          | ✓ PASS  |

**Resultado: 7/7 casos de prueba correctos (100%)**

## Algoritmos Implementados

### Media Aritmética
```python
mean = sum(data) / len(data)
```

### Mediana
- Ordena los datos
- Si n es par: promedio de los dos valores centrales
- Si n es impar: valor central

### Moda
- Cuenta frecuencia de cada valor
- Retorna el primer valor con máxima frecuencia

### Desviación Estándar Poblacional
```python
std_dev = sqrt(sum((x - mean)^2) / n)
```

### Varianza Poblacional
```python
variance = sum((x - mean)^2) / (n - 1)
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
- Datos inválidos en el archivo
- Archivo vacío
- Errores de escritura

## Archivos Generados

- `StatisticsResults.txt`: Contiene todas las estadísticas calculadas
- `TC*_execution.log`: Logs de cada ejecución de prueba
- `TC*_StatisticsResults.txt`: Resultados específicos de cada caso de prueba
