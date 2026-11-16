# CalcuSmoke

CalcuSmoke is a minimal Python command-line calculator supporting addition,
subtraction, multiplication, and division for positive, negative, and decimal
numbers.

## Run the calculator

```bash
python calculator.py add 2 3
```

The command prints `5.0`. Use `subtract`, `multiply`, or `divide` for the
other operations:

```text
$ python calculator.py divide 7 2
3.5
```

Invalid input and division by zero produce a clear error message without a
traceback.

## Run the tests

```bash
python -m unittest -v
```

## Trabajo realizado

Este proyecto fue realizado de forma autónoma por mí, un asistente de IA que
utiliza Copilot SDK en VS Code. No participaron otros agentes ni se necesitó
intervención manual para implementar la solución.

El trabajo incluyó:

- Configurar el repositorio remoto `LeucoByte/CalcuSmoke`.
- Crear el hito `programa foinal` y cinco issues para las operaciones y la
  integración final.
- Implementar suma, resta, multiplicación y división con números positivos,
  negativos y decimales.
- Gestionar la división por cero y las entradas inválidas con mensajes claros.
- Añadir seis pruebas automatizadas con `unittest`.
- Documentar el uso del programa y las pruebas.
- Añadir las reglas de `.gitignore`, crear el commit de implementación y
  publicarlo en la rama `main`.
- Verificar y cerrar los cinco issues y el hito tras pasar las pruebas y las
  comprobaciones de línea de comandos.
