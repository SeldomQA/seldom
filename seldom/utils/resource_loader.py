import json
from functools import lru_cache
from pathlib import Path
from typing import Any, Dict, Literal

from seldom.logging import log
from seldom.testdata.parameterization import find_file


def resource_file(
        file: str,
        key: str | None = None,
        base_dir: Path | None = None,
        *,
        return_type: Literal["gql", "json"] | None = None,
) -> str | Dict[str, Any]:
    """
    Load GraphQL or JSON resource file for test cases.

    :param file: Filename (e.g., 'query.gql', 'data.json')
    :param key: If JSON, extract nested value by key (dot-separated, e.g., 'user.profile')
    :param base_dir: Base directory to search from. If None, uses caller's directory.
    :param return_type: Explicitly specify expected type ('gql' or 'json') for better typing.
    :return: str (for GraphQL) or dict (for JSON)
    """
    if not file:
        raise ValueError("File name must not be empty.")

    # Determine base directory
    if base_dir is None:
        import inspect
        caller_frame = inspect.currentframe().f_back
        if caller_frame is None:
            raise RuntimeError("Unable to determine caller directory.")
        base_dir = Path(caller_frame.f_code.co_filename).parent.resolve()

    # Locate file
    file_path = Path(find_file(file, base_dir))
    if not file_path or not file_path.exists():
        raise FileNotFoundError(f"Resource file not found: {file}")

    # Determine format by suffix (robust)
    suffix = file_path.suffix.lower()[1:]  # e.g., 'gql', 'graphql', 'json'
    if return_type is None:
        if suffix in ("graphql", "gql"):
            return_type = "gql"
        elif suffix == "json":
            return_type = "json"
        else:
            raise ValueError(f"Unsupported file extension: {suffix}. Use .gql, .graphql, or .json.")

    # Load content
    content = _load_cached_file(file_path, is_json=(return_type == "json"))

    # Extract by key if needed (for JSON)
    if return_type == "json" and key:
        content = _get_nested_value(content, key)

    return content


@lru_cache(maxsize=128)
def _load_cached_file(file_path: Path, is_json: bool) -> str | Dict[str, Any]:
    """Cached file loader to avoid repeated I/O in parametrized tests."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            if is_json:
                return json.load(f)
            else:
                return f.read().strip()
    except Exception as e:
        log.error(f"Failed to load resource file {file_path}: {e}")
        raise


def _get_nested_value(data: Dict[str, Any], key_path: str) -> Any:
    """Support dot-notation key access: e.g., 'user.profile.name'."""
    keys = key_path.split('.')
    value = data
    for k in keys:
        if not isinstance(value, dict):
            raise KeyError(f"Cannot traverse into non-dict at key: {k}")
        if k not in value:
            raise KeyError(f"Key '{k}' not found in nested data. Full path: {key_path}")
        value = value[k]
    return value