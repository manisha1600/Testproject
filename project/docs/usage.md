# Usage

This document shows simple usage examples for the project.

## Running the example
From PowerShell run:

```powershell
python "C:\Users\manisa2\OneDrive - Medtronic PLC\GIT2\project\app.py"
```

Output will appear on the console and log files will be created under `project/logs` (if writable).

## Logging configuration
You can call `get_logger(name, level, log_dir=...)` to customize the logger:

- `name` — logger name, e.g. `project.app`
- `level` — Python `logging` level (e.g., `logging.DEBUG`)
- `log_dir` — optional path where rotating logs are written

Example:

```python
from utils import get_logger
import logging

logger = get_logger("project.app", logging.DEBUG, log_dir=r"C:\temp\mylogs")
logger.info("Hello world")
```

## Notes
- The logger is idempotent: calling `get_logger` multiple times for the same name will not add duplicate handlers.
- If file logging cannot be created, the logger will still write to the console.
