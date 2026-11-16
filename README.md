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
