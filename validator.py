
from pathlib import Path

REQUIRED_KEYS = ("book", "audio", "video")


def _check_exists(p: str) -> None:
    if not Path(p).exists():
        raise FileNotFoundError(f"Файл не найден: {p}")


def validate_config(cfg: dict) -> None:
    for section in ("originals", "generated", "prompts", "workflow"):
        if section not in cfg:
            raise ValueError(f"{section}")

    for section in ("originals", "generated"):
        for key in REQUIRED_KEYS:
            if key not in cfg.get(section, {}):
                raise ValueError(f"In '{section}' hasn't '{key}'")

    audio_format = cfg["originals"]["audio"]["format"].lower()
    if audio_format not in ("cd", "vinyl"):
        raise ValueError("originals.audio.format must be CD or Vinyl")

    video_format = cfg["originals"]["video"]["format"].lower()
    if video_format not in ("dvd", "vhs"):
        raise ValueError("originals.video.format must be DVD or VHS")

    model = cfg["workflow"].get("model", {})
    if not model.get("name") or not model.get("version"):
        raise ValueError("workflow.model hasn't name or version")
    if not model.get("link"):
        raise ValueError("workflow.model.link")

    for key in REQUIRED_KEYS:
        if not cfg["prompts"].get(key):
            raise ValueError(f"prompts.{key} пустой")

    if "negative_prompts" not in cfg:
        raise ValueError("negative_prompts")
    for key in REQUIRED_KEYS:
        if not cfg["negative_prompts"].get(key):
            raise ValueError(f"negative_prompts.{key}")

    paths = [
        cfg["originals"]["book"]["image_path"],
        cfg["originals"]["audio"]["image_path"],
        cfg["originals"]["video"]["image_path"],
        cfg["generated"]["book"]["image_path"],
        cfg["generated"]["audio"]["image_path"],
        cfg["generated"]["video"]["image_path"],
        cfg["pipeline_screenshot_path"],
    ]
    for p in paths:
        _check_exists(p)