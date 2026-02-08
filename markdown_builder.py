def build_markdown(cfg: dict, paths: dict) -> str:
    s = cfg["student"]
    o = cfg["originals"]
    g = cfg["generated"]
    wf = cfg["workflow"]
    tech = wf["technical"]
    hw = wf["hardware"]
    m = wf["model"]
    p = cfg["prompts"]
    n = cfg.get("negative_prompts", {})

    return f"""# Generative AI — Capstone Project 2 (Art)

**Student:** {s["first_name"]} {s["last_name"]}

## Original works (iconic media)

### Book — "{o["book"]["title"]}" by {o["book"]["author"]}
![Book Original]({paths["orig_book"]})

### Audio — {o["audio"]["artist"]} — "{o["audio"]["album"]}" ({o["audio"]["format"]})
![Audio Original]({paths["orig_audio"]})

### Video — "{o["video"]["title"]}" ({o["video"]["format"]})
![Video Original]({paths["orig_video"]})

## AI-generated alternative variations (3)

### Book (AI)
**Idea:** {g["book"]["idea"]}
![Book AI]({paths["gen_book"]})

### Audio (AI)
**Idea:** {g["audio"]["idea"]}
![Audio AI]({paths["gen_audio"]})

### Video (AI)
**Idea:** {g["video"]["idea"]}
![Video AI]({paths["gen_video"]})

## Workflow

### Tools
- **WebUI:** {wf["webui"]}
- **Deployment:** {wf["deployment"]}
- **OS:** {wf["os"]}
- **LoRAs / Adapters:** {wf["loras"]}

### Model
- **Name:** {m["name"]}
- **Version:** {m["version"]}
- **Link:** {m["link"]}

### Technical generation details
- **Resolution:** {tech["size"]}
- **Steps:** {tech["steps"]}
- **CFG:** {tech["cfg"]}
- **Sampler:** {tech["sampler"]}
- **Scheduler:** {tech["scheduler"]}
- **Seed:** {tech["seed"]}
- **Batch size:** {tech["batch_size"]}
- **VAE:** {tech["vae"]}

### Pipeline screenshot (ComfyUI graph)
![Pipeline]({paths["pipeline"]})

## Prompts used

### Book
**Positive:** {p["book"]}
**Negative:** {n.get("book", "")}

### Audio
**Positive:** {p["audio"]}
**Negative:** {n.get("audio", "")}

### Video
**Positive:** {p["video"]}
**Negative:** {n.get("video", "")}

## Hardware
- **GPU:** {hw["gpu"]} ({hw["vram"]})
- **RAM:** {hw["ram"]}
- **CPU:** {hw["cpu"]}

## Notes (compliance)
- Images were generated using a **self-hosted local setup** (no public image generation APIs).
- Provided **3 AI variations**: book, audio album, and video cover.
"""