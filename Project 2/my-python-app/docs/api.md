# API Reference

## `src.app.greet(name: str = "World") -> str`

Return a greeting string for `name`.

Parameters:
- `name` (str): Name to include in the greeting. Defaults to `"World"`.

Returns:
- `str`: Greeting, e.g. `"Hello, Alice!"`.

Example:

```py
from src.app import greet
greet('Alice')  # 'Hello, Alice!'
```
