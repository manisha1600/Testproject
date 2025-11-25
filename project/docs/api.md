# API Reference

## `models.py`

### `User`
- `id: int`
- `name: str`
- `email: str`

Methods:
- `is_valid_email() -> bool` — quick, heuristic email validation.

## `utils/logging_utils.py`

### `get_logger(name: str, level: int, *, log_dir: str | None)`
Returns a configured `logging.Logger` with:
- Console `StreamHandler` using a standard formatter
- `RotatingFileHandler` writing to `log_dir` (or `project/logs` by default)
- The function is safe to call multiple times for the same logger name (no duplicate handlers).

Example:

```python
from utils.logging_utils import get_logger
import logging
logger = get_logger("project.app", logging.DEBUG)
logger.info("Started")
```
