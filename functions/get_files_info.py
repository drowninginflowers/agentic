from pathlib import Path


def get_files_info(base_directory, relative_path="."):
    try:
        base_dir = Path(base_directory)
        resolved_base_dir = base_dir.resolve()

        if not resolved_base_dir.exists() or not resolved_base_dir.is_dir():
            return f'Error: "{base_directory}" is not a directory'

    except (OSError, RuntimeError):
        return f'Error: "{base_directory}" is not a resolveable directory'

    try:
        target_path = (base_dir / relative_path).resolve()

        if not target_path.exists() or not target_path.is_dir():
            return f'Error: "{relative_path}" is not a directory'

    except (OSError, RuntimeError):
        return f'Error: "{relative_path}" is not a resolveable directory'

    try:
        target_path.relative_to(resolved_base_dir)
    except ValueError:
        return f'Error: Cannot list "{relative_path}" as it is outside the permitted working directory'

    try:
        dir_info = []
        for content in target_path.iterdir():
            if content.name == "__pycache__":
                continue  # skip cache directories
            content_size = content.stat().st_size
            dir_info.append(
                f"- {content.name}: file_size={content_size} bytes, is_dir={content.is_dir()}"
            )

        return "\n".join(dir_info)
    except Exception as e:
        return f"Error: {e}"
