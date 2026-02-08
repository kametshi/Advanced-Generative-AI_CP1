# Generative AI — Capstone Project 2 (Art)

**Student:** Karina Abdullaeva

## Original works (iconic media)

### Book — "The Iliad" by Homer
![Book Original](output/images/originals/book/book.jpg)

### Audio — Rammstein — "Mutter" (CD)
![Audio Original](output/images/originals/audio/audio.jpg)

### Video — "Interstellar" (DVD)
![Video Original](output/images/originals/video/video.jpg)

## AI-generated alternative variations (3)

### Book (AI)
**Idea:** Cinematic epic interpretation (SDXL).
![Book AI](output/images/generated/book/book_ai.png)

### Audio (AI)
**Idea:** The industrial abstract version (SDXL).
![Audio AI](output/images/generated/audio/audio_ai.png)

### Video (AI)
**Idea:** Poster style for DVD/VHS (SDXL).
![Video AI](output/images/generated/video/video_ai.png)

## Workflow

### Tools
- **WebUI:** ComfyUI
- **Deployment:** Local self-hosted (Windows)
- **OS:** Windows 10
- **LoRAs / Adapters:** Not used

### Model
- **Name:** Juggernaut XL v10
- **Version:** SDXL-based
- **Link:** https://huggingface.co/RunDiffusion/Juggernaut-XL-v10

### Technical generation details
- **Resolution:** 1024x1024
- **Steps:** 30
- **CFG:** 5.5
- **Sampler:** DPM++ 2M Karras
- **Scheduler:** karras
- **Seed:** random
- **Batch size:** 1
- **VAE:** from checkpoint (default)

### Pipeline screenshot (ComfyUI graph)
![Pipeline](output/images/pipeline/structure.png)

## Prompts used

### Book
**Positive:** Epic ancient Greek battlefield inspired by The Iliad, cinematic composition, dramatic volumetric lighting, bronze armored warrior, mythological atmosphere, classical sculpture aesthetics, high detail, ultra realistic textures, professional book cover design, symmetrical layout, sharp focus, 4k
**Negative:** low quality, blurry, distorted anatomy, extra limbs, bad hands, watermark, text, logo, cropped, jpeg artifacts, oversaturated

### Audio
**Positive:** Dark industrial album cover, metallic textures, cold monochrome palette, dramatic studio lighting, brutalist design, symmetrical composition, high contrast, professional CD cover layout, ultra sharp, 4k
**Negative:** low quality, blurry, oversaturated, watermark, text, logo, jpeg artifacts, messy composition

### Video
**Positive:** Cinematic sci-fi movie poster inspired by Interstellar, lone astronaut in deep space, dramatic lighting, emotional atmosphere, realistic stars and nebula background, centered composition, professional DVD cover design, film grain, ultra detailed, 4k
**Negative:** low quality, blurry, watermark, text, logo, distorted anatomy, extra limbs, cartoonish, jpeg artifacts

## Hardware
- **GPU:** NVIDIA GeForce RTX 4060 Laptop GPU (8GB)
- **RAM:** 64GB
- **CPU:** Intel Core i7

## Notes (compliance)
- Images were generated using a **self-hosted local setup** (no public image generation APIs).
- Provided **3 AI variations**: book, audio album, and video cover.
