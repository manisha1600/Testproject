# Project

Small example project demonstrating a `User` dataclass and a simple logging utility.

## Requirements
- Python 3.8+
- No third-party packages required (standard library only)

## Quickstart (PowerShell)
```powershell
python "C:\Users\manisa2\OneDrive - Medtronic PLC\GIT2\project\app.py"
```

The script prints a short message and also writes logs to `project/logs` (created automatically).

## Files
- `app.py` — small runnable example showing usage.
- `models.py` — `User` dataclass.
- `utils/logging_utils.py` — `get_logger()` helper (console + rotating file handlers).
- `utils/__init__.py` — convenience export.
- `requirements.txt` — dependency list (may be empty for stdlib-only projects).
- `docs/` — usage and API documentation.

## Next steps
- Add unit tests (optional)
- Add packaging or CI (optional)
