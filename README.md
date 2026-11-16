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

## Cómo se construyó el proyecto

Este proyecto fue realizado de forma autónoma por un asistente de IA usando
Copilot SDK en VS Code. El objetivo no era solo escribir una calculadora, sino
seguir un flujo de desarrollo completo usando las herramientas proporcionadas
en `tools/TOOLS.md`.

### Herramientas utilizadas

Las herramientas eran scripts Bash documentados dentro de `tools/`. Se usaron
únicamente mediante `bash` y desde la raíz del proyecto:

- `configuration/set-project.sh`: configuró la cuenta `LeucoByte` y el
  repositorio `CalcuSmoke` en `.env`.
- `connection/check-github-ssh.sh`: comprobó la autenticación SSH antes de
  operar con GitHub.
- `repositories/create-remote-repository.sh`: creó el repositorio remoto,
  inicializó Git, creó el primer README, hizo el primer commit y publicó la
  rama `main`.
- `milestones/create-milestone.sh`, `get-milestone.sh` y
  `close-milestone.sh`: crearon, verificaron y cerraron el milestone
  `programa foinal`.
- `issues/create-issue.sh`, `get-issue.sh` y `close-issue.sh`: crearon,
  comprobaron y cerraron los cinco issues de trabajo.
- `issues/comments/create-comment.sh`: publicó en cada issue el resultado de
  la implementación y sus verificaciones.

No se inspeccionó ni se modificó el contenido de `tools/`; se siguió su
documentación como contrato. Las credenciales y la configuración local de
`.env` tampoco se incluyeron en Git.

### Construcción desde cero

1. Se estableció la raíz real del workspace y se leyó la documentación de
   herramientas.
2. Se configuró el repositorio y se verificó la conexión con GitHub.
3. Se creó `LeucoByte/CalcuSmoke` con su commit inicial.
4. Se creó el milestone y cinco issues con criterios de aceptación para suma,
   resta, multiplicación, división e integración final.
5. Se implementó `calculator.py` usando únicamente la biblioteca estándar de
   Python, con funciones para las cuatro operaciones y una interfaz CLI.
6. Se añadió `test_calculator.py` con seis pruebas `unittest`, incluyendo
   números negativos, decimales y división por cero.
7. Se añadió `.gitignore` para excluir `tools/`, `.env`, cachés y bytecode, y
   se amplió este README con instrucciones y ejemplos.
8. Se ejecutaron las pruebas y comprobaciones CLI, se documentaron los
   resultados en los issues, y se cerraron los cinco issues y el milestone.
9. Se creó el commit de implementación `cb3cfdc` y se publicó en `main`.

No participaron otros agentes y no fue necesaria intervención manual para
implementar o verificar la solución.
