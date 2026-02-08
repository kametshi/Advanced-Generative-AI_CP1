import shutil
from pathlib import Path


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def safe_copy(src: Path, dst_dir: Path) -> Path:
    if not src.exists():
        raise FileNotFoundError(f"Source file not found: {src}")
    if src.is_dir():
        raise IsADirectoryError(f"Expected a file, got directory: {src}")

    ensure_dir(dst_dir)
    dst = dst_dir / src.name

    if src.resolve() == dst.resolve():
        return dst

    shutil.copy2(src, dst)
    return dst