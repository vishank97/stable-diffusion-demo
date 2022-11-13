from torch import autocast
from diffusers import StableDiffusionPipeline

model_id = "CompVis/stable-diffusion-v1-4"
device = "cuda"


pipe = StableDiffusionPipeline.from_pretrained(model_id, use_auth_token=True)
pipe = pipe.to(device)


def generate_image(prompt):
    with autocast("cuda"):
        image = pipe(prompt, guidance_scale=7.5).images[0]

    image.save("astronaut_rides_horse.png")
    return image
