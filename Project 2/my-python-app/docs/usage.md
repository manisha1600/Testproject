# Usage

Simple usage examples for the example application.

Python REPL / script:

```py
from src.app import greet

print(greet())            # Hello, World!
print(greet("Alice"))   # Hello, Alice!
```

Command line:

```powershell
# from repository root
python -c "from src.app import greet; print(greet('Bob'))"
```
