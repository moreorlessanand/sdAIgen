## MODEL

model_list = {
    "1. realismByStableYogi_v5XLFP16": [
        {"url": "https://civitai.com/api/download/models/1075446?type=Model&format=SafeTensor&size=pruned&fp=fp16"}
    ]
}

## VAE

vae_list = {
    "1. Anime.vae": [
        {"url": "https://huggingface.co/fp16-guy/anything_kl-f8-anime2_vae-ft-mse-840000-ema-pruned_blessed_clearvae_fp16_cleaned/resolve/main/kl-f8-anime2_fp16.safetensors", "name": "Anime-kl-f8.vae.safetensors"},
        {"url": "https://huggingface.co/fp16-guy/anything_kl-f8-anime2_vae-ft-mse-840000-ema-pruned_blessed_clearvae_fp16_cleaned/resolve/main/vae-ft-mse-840000-ema-pruned_fp16.safetensors", "name": "Anime-mse.vae.safetensors"}
    ],
    "2. Anything.vae": [{"url": "https://huggingface.co/fp16-guy/anything_kl-f8-anime2_vae-ft-mse-840000-ema-pruned_blessed_clearvae_fp16_cleaned/resolve/main/anything_fp16.safetensors", "name": "Anything.vae.safetensors"}],
    "3. Blessed2.vae": [{"url": "https://huggingface.co/fp16-guy/anything_kl-f8-anime2_vae-ft-mse-840000-ema-pruned_blessed_clearvae_fp16_cleaned/resolve/main/blessed2_fp16.safetensors", "name": "Blessed2.vae.safetensors"}],
    "4. ClearVae.vae": [{"url": "https://huggingface.co/fp16-guy/anything_kl-f8-anime2_vae-ft-mse-840000-ema-pruned_blessed_clearvae_fp16_cleaned/resolve/main/ClearVAE_V2.3_fp16.safetensors", "name": "ClearVae_23.vae.safetensors"}],
    "5. WD.vae": [{"url": "https://huggingface.co/NoCrypt/resources/resolve/main/VAE/wd.vae.safetensors", "name": "WD.vae.safetensors"}]
}

## CONTROLNET

controlnet_list = {
    "1. Openpose": [
        {"url": "https://huggingface.co/xinsir/controlnet-depth-sdxl-1.0/resolve/main/diffusion_pytorch_model.safetensors"}
    ]
}
