#!/bin/bash
# Script de verificación completa para Actividad 4.2
# Este script ejecuta todos los casos de prueba y verifica los resultados

echo "=================================================="
echo "  VERIFICACIÓN ACTIVIDAD 4.2"
echo "  Ejercicios de Programación Python"
echo "=================================================="
echo ""

# Colores para output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Contadores
total_tests=0
passed_tests=0
failed_tests=0

# Función para verificar un programa
verify_program() {
    local program_path=$1
    local test_file=$2
    local test_name=$3
    
    echo -n "Testing $test_name... "
    
    if python3 "$program_path" "$test_file" > /dev/null 2>&1; then
        echo -e "${GREEN}✓ PASS${NC}"
        ((passed_tests++))
    else
        echo -e "${RED}✗ FAIL${NC}"
        ((failed_tests++))
    fi
    
    ((total_tests++))
}

# Verificar P1
echo "=================================================="
echo "P1: COMPUTE STATISTICS"
echo "=================================================="
cd P1/source
for tc in ../tests/P1_TC*.txt; do
    test_name=$(basename $tc)
    verify_program "compute_statistics.py" "$tc" "$test_name"
done
cd ../..
echo ""

# Verificar P2
echo "=================================================="
echo "P2: CONVERT NUMBERS"
echo "=================================================="
cd P2/source
for tc in ../tests/P2_TC*.txt; do
    test_name=$(basename $tc)
    verify_program "convert_numbers.py" "$tc" "$test_name"
done
cd ../..
echo ""

# Verificar P3
echo "=================================================="
echo "P3: WORD COUNT"
echo "=================================================="
cd P3/source
for tc in ../tests/P3_TC*.txt; do
    # Skip result files
    if [[ $tc != *"Results"* ]]; then
        test_name=$(basename $tc)
        verify_program "word_count.py" "$tc" "$test_name"
    fi
done
cd ../..
echo ""

# Resumen
echo "=================================================="
echo "  RESUMEN DE VERIFICACIÓN"
echo "=================================================="
echo "Total de pruebas:     $total_tests"
echo -e "Pruebas exitosas:     ${GREEN}$passed_tests${NC}"
echo -e "Pruebas fallidas:     ${RED}$failed_tests${NC}"

if [ $failed_tests -eq 0 ]; then
    echo ""
    echo -e "${GREEN}✓ TODOS LOS TESTS PASARON${NC}"
    echo -e "${GREEN}✓ ACTIVIDAD COMPLETADA EXITOSAMENTE${NC}"
    exit 0
else
    echo ""
    echo -e "${RED}✗ ALGUNOS TESTS FALLARON${NC}"
    exit 1
fi
