import base64

from task.client import OpenAIClient
from task.constants import OPENAI_HOST

# https://platform.openai.com/docs/guides/images-vision?api-mode=chat#analyze-images
# https://platform.openai.com/docs/guides/images-vision?api-mode=chat&format=base64-encoded#analyze-images


def _encode_image(image_path):
    #TODO:
    # Function to encode image to base64 you can find in documentation
    # https://platform.openai.com/docs/guides/images-vision?api-mode=chat&format=base64-encoded#analyze-images
    raise NotImplementedError


def main(model_name: str, img_urls: list[str], request: str = "What's in this image/s?"):
    #TODO:
    # 1. Create OpenAIClient with OPENAI_HOST + /v1/chat/completions as endpoint
    # 2. Prepare img_content:
    #   - iterate through img_urls and generate list of dicts {"type": "image_url", "image_url": {"url": img_url}}
    # 3. Call client with:
    #   - model=model_name
    #   - messages=[{"role": "user","content": [{"type": "text", "text": request}, *img_content]}]
    raise NotImplementedError


main(
    #TODO:
    # - model_name gpt-4o-mini
    # - img_urls:
    #   - https://a-z-animals.com/media/2019/11/Elephant-male-1024x535.jpg
    #   or
    #   - f"data:image/jpeg;base64,{_encode_image('banner.png')}"
)

#TODO:
# In the end load both images (url and base64 encoded 'banner.png'), ask "Generate poem based on images" and se what will happen?