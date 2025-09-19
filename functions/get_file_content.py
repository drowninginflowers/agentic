from pathlib import Path


def get_file_content(base_directory, file_path):
    try:
        base_dir = Path(base_directory)
        resolved_base_dir = base_dir.resolve()

        if not resolved_base_dir.exists() or not resolved_base_dir.is_dir():
            return f'Error: "{base_directory}" is not a directory'

    except (OSError, RuntimeError):
        return f'Error: "{base_directory}" is not a resolveable directory path'

    try:
        target_file = (base_dir / file_path).resolve()

        if not target_file.exists() or target_file.is_dir():
            return f'Error: File not found or is not a regular file: "{file_path}"'

    except (OSError, RuntimeError):
        return f'Error: "{file_path}" is not a resolveable path'

    try:
        target_file.relative_to(resolved_base_dir)
    except ValueError:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    try:
        with open(target_file, encoding="utf-8") as f:
            read_data = f.read()
        return read_data
    except Exception as e:
        return f"Error: {e}"
