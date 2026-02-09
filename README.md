# Actividad 4.2 - Ejercicios de Programación

Este repositorio contiene la implementación de tres ejercicios de programación en Python, cumpliendo con el estándar PEP-8 y sin errores de pylint.

## Estructura del Repositorio

```
actividad_4_2/
├── P1/                    # Programming Exercise 1: Estadísticas
│   ├── source/           # Código fuente
│   ├── tests/            # Casos de prueba
│   └── results/          # Resultados de ejecución
├── P2/                    # Programming Exercise 2: Conversión de números
│   ├── source/           # Código fuente
│   ├── tests/            # Casos de prueba
│   └── results/          # Resultados de ejecución
└── P3/                    # Programming Exercise 3: Contador de palabras
    ├── source/           # Código fuente
    ├── tests/            # Casos de prueba
    └── results/          # Resultados de ejecución
```

## Ejercicios Implementados

### P1: Compute Statistics (compute_statistics.py)
Programa que lee datos numéricos de un archivo y calcula estadísticas descriptivas:
- Media (Mean)
- Mediana (Median)
- Moda (Mode)
- Desviación Estándar Poblacional
- Varianza Poblacional

**Uso:**
```bash
python compute_statistics.py fileWithData.txt
```

**Características:**
- Manejo de errores para datos inválidos
- Cálculo de estadísticas usando algoritmos básicos (sin librerías especializadas)
- Medición de tiempo de ejecución
- Salida en consola y archivo (StatisticsResults.txt)

### P2: Convert Numbers (convert_numbers.py)
Programa que lee números decimales y convierte los últimos dos dígitos a binario y hexadecimal.

**Uso:**
```bash
python convert_numbers.py fileWithData.txt
```

**Características:**
- Conversión usando algoritmos básicos (sin funciones built-in)
- Manejo de datos inválidos
- Medición de tiempo de ejecución
- Salida en consola y archivo (ConvertionResults.txt)

### P3: Word Count (word_count.py)
Programa que cuenta la frecuencia de palabras distintas en un archivo de texto.

**Uso:**
```bash
python word_count.py fileWithData.txt
```

**Características:**
- Conteo insensible a mayúsculas/minúsculas
- Ordenamiento alfabético usando algoritmo básico (bubble sort)
- Manejo de errores
- Medición de tiempo de ejecución
- Salida en consola y archivo (WordCountResults.txt)

## Estándares de Calidad

### PEP-8 Compliance
Todos los programas siguen el estándar PEP-8:
- Nombres de funciones y variables en snake_case
- Líneas de máximo 79 caracteres
- Docstrings para módulos, clases y funciones
- Espaciado apropiado
- Importaciones al inicio del archivo

### Pylint Verification
Los programas han sido verificados para asegurar:
- ✓ Sin errores (E)
- ✓ Sin warnings (W)
- ✓ Sin refactors (R)
- ✓ Sin convenciones violadas (C)
- ✓ Sin errores fatales (F)

## Casos de Prueba

Cada ejercicio incluye múltiples casos de prueba:

### P1 (Estadísticas)
- TC1: 400 números
- TC2: 1,977 números
- TC3: 12,624 números
- TC4: 12,624 números decimales
- TC5: 307 números
- TC6: 3,000 números grandes
- TC7: 12,767 números grandes

### P2 (Conversión)
- TC1: 200 números
- TC2: 200 números
- TC3: 200 números (incluye negativos y cero)
- TC4: 200 números (incluye datos inválidos)

### P3 (Contador de Palabras)
- TC1: 100 palabras
- TC2: 184 palabras
- TC3: 500 palabras
- TC4: 1,000 palabras
- TC5: 5,000 palabras

## Resultados

Todos los casos de prueba se ejecutaron exitosamente y los resultados se encuentran en las carpetas `results/` de cada ejercicio.

## Requisitos

- Python 3.6 o superior
- No se requieren bibliotecas externas

## Autor

Implementado para la Actividad 4.2 - Pruebas y Calidad de Software

## Notas Adicionales

- Los algoritmos implementados son básicos y no utilizan funciones o librerías especializadas
- Cada programa incluye manejo robusto de errores
- Los resultados incluyen medición precisa del tiempo de ejecución
- La documentación sigue el estilo de docstrings de Google
