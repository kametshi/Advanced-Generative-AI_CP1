from pathlib import Path

from config import CONFIG
from validator import validate_config
from file_utils import ensure_dir, safe_copy
from markdown_builder import build_markdown


def main():
    validate_config(CONFIG)

    out = Path(CONFIG["output_dir"])
    ensure_dir(out)

    img = out / "images"

    paths = {
        "orig_book": safe_copy(Path(CONFIG["originals"]["book"]["image_path"]), img / "originals/book"),
        "orig_audio": safe_copy(Path(CONFIG["originals"]["audio"]["image_path"]), img / "originals/audio"),
        "orig_video": safe_copy(Path(CONFIG["originals"]["video"]["image_path"]), img / "originals/video"),
        "gen_book": safe_copy(Path(CONFIG["generated"]["book"]["image_path"]), img / "generated/book"),
        "gen_audio": safe_copy(Path(CONFIG["generated"]["audio"]["image_path"]), img / "generated/audio"),
        "gen_video": safe_copy(Path(CONFIG["generated"]["video"]["image_path"]), img / "generated/video"),
        "pipeline": safe_copy(Path(CONFIG["pipeline_screenshot_path"]), img / "pipeline"),
    }

    rel = {k: str(v).replace("\\", "/") for k, v in paths.items()}
    report = build_markdown(CONFIG, rel)

    (out / "README.md").write_text(report, encoding="utf-8")

    print("Capstone Project 2 — ready!")
    print("Report:", (out / "README.md").resolve())
    print("Images root:", img.resolve())


if __name__ == "__main__":
    main()