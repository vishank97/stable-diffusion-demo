from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import StreamingResponse
from predict.predict import generate_image

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to caption to Image Generator!"}

class ImageGenerator(BaseModel):
    caption: str

@app.post("/predict")
async def predict(ic: ImageGenerator):
    # im_png = generate_image(ic.caption)
    # return StreamingResponse(io.BytesIO(im_png.tobytes()), media_type="image/png")
    image_stream = io.BytesIO(generate_image(ic.caption))
    return StreamingResponse(content=image_stream, media_type="image/png")