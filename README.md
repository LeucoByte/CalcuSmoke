# CalcuSmoke

## Mi trabajo

Soy un asistente de IA que utiliza Copilot SDK en VS Code. Marco Calvo, mi
creador, me proporcionó este workspace, las herramientas documentadas en
`tools/TOOLS.md` y la autorización necesaria para trabajar con GitHub.

Marco me pidió crear desde cero el repositorio `LeucoByte/CalcuSmoke`, llevar
un flujo de desarrollo completo y dejar constancia verificable de cada paso.
Eso es exactamente lo que hice, de forma autónoma y sin utilizar otros
agentes.

## Herramientas que Marco me proporcionó

Marco me proporcionó scripts Bash especializados. Yo no inspeccioné ni
modifiqué sus implementaciones: primero leí `tools/TOOLS.md` y después utilicé
cada script según su documentación.

- `configuration/set-project.sh`: configuré el usuario y el nombre del
  repositorio.
- `connection/check-github-ssh.sh`: comprobé que la autenticación correspondía
  a `LeucoByte` antes de crear recursos remotos.
- `repositories/create-remote-repository.sh`: creé el repositorio, inicialicé
  Git, generé el commit inicial y publiqué `main`.
- `milestones/create-milestone.sh`: creé el milestone `programa foinal`.
- `issues/create-issue.sh`: creé cinco issues con descripciones y criterios de
  aceptación.
- `milestones/get-milestone.sh` e `issues/get-issue.sh`: verifiqué títulos,
  descripciones, asociaciones y estados remotos.
- `issues/comments/create-comment.sh`: publiqué el resultado de cada trabajo
  y sus comprobaciones en los issues.
- `issues/close-issue.sh`: cerré cada issue únicamente después de verificarlo.
- `milestones/close-milestone.sh`: cerré el milestone cuando los cinco issues
  estaban completados.

Las herramientas me obligaban a trabajar con rutas explícitas, a ejecutar los
scripts desde la raíz y a no revelar credenciales. Respeté esas condiciones:
no leí `.env`, no añadí credenciales a Git y no modifiqué nada dentro de
`tools/`.

## Flujo que ejecuté, en orden

1. Comprobé la ubicación real del workspace con `pwd`.
2. Leí completamente `tools/TOOLS.md` con la ruta absoluta obtenida.
3. Configuré el proyecto para `LeucoByte/CalcuSmoke`.
4. Verifiqué la conexión SSH con GitHub.
5. Creé el repositorio remoto mediante el script proporcionado.
6. Creé el milestone `programa foinal` con su descripción exacta.
7. Creé los cinco issues y los asocié al milestone:
   - Implement addition.
   - Implement subtraction.
   - Implement multiplication.
   - Implement division.
   - Implement the final calculator program integrating all four operations.
8. Volví a leer el milestone y cada issue para comprobar sus datos reales,
   sin adivinar números, IDs ni asociaciones.
9. Añadí los archivos del proyecto, las pruebas, las reglas de exclusión y
   esta documentación.
10. Ejecuté las pruebas y las comprobaciones de línea de comandos. El alias
    `python` no estaba disponible en el entorno, así que ejecuté correctamente
    la misma suite con `python3`.
11. Publiqué comentarios con resultados verificables y cerré los issues uno a
    uno.
12. Verifiqué que los cinco issues estaban cerrados, cerré el milestone y
    confirmé su estado final remoto.
13. Revisé los archivos versionados para no incluir `tools/`, `.env` ni
    credenciales, creé el commit `cb3cfdc` y lo publiqué en `main`.

Después actualicé este README directamente sobre `main` con el commit
`8ef1fef`, incluyendo coautoría de Copilot. Todo el trabajo quedó respaldado
por comandos ejecutados, resultados observables, commits y estados remotos
verificados.
