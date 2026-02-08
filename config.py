CONFIG = {
    "student": {
        "first_name": "Karina",
        "last_name": "Abdullaeva",
    },
    "originals": {
        "book": {
            "title": "The Iliad",
            "author": "Homer",
            "image_path": r"output\images\originals\book\book.jpg",
        },
        "audio": {
            "artist": "Rammstein",
            "album": "Mutter",
            "format": "CD",
            "image_path": r"output\images\originals\audio\audio.jpg",
        },
        "video": {
            "title": "Interstellar",
            "format": "DVD",
            "image_path": r"output\images\originals\video\video.jpg",
        },
    },

    "generated": {
        "book": {
            "idea": "Cinematic epic interpretation (SDXL).",
            "image_path": r"output\images\generated\book\book_ai.png",
        },
        "audio": {
            "idea": "The industrial abstract version (SDXL).",
            "image_path": r"output\images\generated\audio\audio_ai.png",
        },
        "video": {
            "idea": "Poster style for DVD/VHS (SDXL).",
            "image_path": r"output\images\generated\video\video_ai.png",
        },
    },

    "pipeline_screenshot_path": r"structure.png",

    "workflow": {
        "webui": "ComfyUI",
        "deployment": "Local self-hosted (Windows)",
        "os": "Windows 10",
        "hardware": {
            "gpu": "NVIDIA GeForce RTX 4060 Laptop GPU",
            "vram": "8GB",
            "ram": "64GB",
            "cpu": "Intel Core i7",
        },
        "model": {
            "name": "Juggernaut XL v10",
            "version": "SDXL-based",
            "link": "https://huggingface.co/RunDiffusion/Juggernaut-XL-v10",
        },
        "loras": "Not used",
        "technical": {
            "steps": 30,
            "cfg": 5.5,
            "sampler": "DPM++ 2M Karras",
            "scheduler": "karras",
            "seed": "random",
            "size": "1024x1024",
            "batch_size": 1,
            "vae": "from checkpoint (default)",
        },
    },

    "prompts": {
        "book": "Epic ancient Greek battlefield inspired by The Iliad, cinematic composition, dramatic volumetric lighting, bronze armored warrior, mythological atmosphere, classical sculpture aesthetics, high detail, ultra realistic textures, professional book cover design, symmetrical layout, sharp focus, 4k",
        "audio": "Dark industrial album cover, metallic textures, cold monochrome palette, dramatic studio lighting, brutalist design, symmetrical composition, high contrast, professional CD cover layout, ultra sharp, 4k",
        "video": "Cinematic sci-fi movie poster inspired by Interstellar, lone astronaut in deep space, dramatic lighting, emotional atmosphere, realistic stars and nebula background, centered composition, professional DVD cover design, film grain, ultra detailed, 4k",
    },

    "negative_prompts": {
        "book": "low quality, blurry, distorted anatomy, extra limbs, bad hands, watermark, text, logo, cropped, jpeg artifacts, oversaturated",
        "audio": "low quality, blurry, oversaturated, watermark, text, logo, jpeg artifacts, messy composition",
        "video": "low quality, blurry, watermark, text, logo, distorted anatomy, extra limbs, cartoonish, jpeg artifacts",
    },
    "output_dir": "output",
}
