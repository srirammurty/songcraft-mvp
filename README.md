# Indian Music Starter Kit (Local ↔ RunPod)

This starter kit wires a Local Flask UI to a RunPod GPU server that runs:
- **MusicGen (AudioCraft)** for instrumental generation. :contentReference[oaicite:1]{index=1}
- **Bark (Suno)** for text-to-audio / vocals POC. :contentReference[oaicite:2]{index=2}
- **RVC / Retrieval-based Voice Conversion** for fine-tuning or voice cloning. :contentReference[oaicite:3]{index=3}

**Important:** model weights are not included. Download official weights from the project pages (links below) and place them under the `runpod_server/models/` folder as explained.

Useful links:
- MusicGen (Hugging Face): https://huggingface.co/facebook/musicgen-small. :contentReference[oaicite:4]{index=4}
- AudioCraft (GitHub): https://github.com/facebookresearch/audiocraft. :contentReference[oaicite:5]{index=5}
- Bark (GitHub): https://github.com/suno-ai/bark. :contentReference[oaicite:6]{index=6}
- RVC WebUI / RVC: https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI. :contentReference[oaicite:7]{index=7}
- IndicTTS Telugu dataset (for Telugu text/audio): https://huggingface.co/datasets/SPRINGLab/IndicTTS_Telugu. :contentReference[oaicite:8]{index=8}
- RunPod (GPU hosting): https://runpod.io/. :contentReference[oaicite:9]{index=9}

See `local_app/` and `runpod_server/` for code and instructions.
