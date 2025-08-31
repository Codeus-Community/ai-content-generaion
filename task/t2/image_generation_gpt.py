import base64
from datetime import datetime

from task.client import OpenAIClient
from task.constants import OPENAI_HOST

# https://platform.openai.com/docs/guides/image-generation?image-generation-model=gpt-image-1&api=image&multi-turn=imageid
# ---
# Request:
# curl -X POST "https://api.openai.com/v1/images/generations" \
#     -H "Authorization: Bearer $OPENAI_API_KEY" \
#     -H "Content-type: application/json" \
#     -d '{
#         "model": "gpt-image-1",
#         "prompt": "smiling catdog."
#     }'
# Response:
# {
#   "created": 1699900000,
#   "data": [
#     {
#       "b64_json": Qt0n6ArYAEABGOhEoYgVAJFdt8jM79uW2DO...,
#     }
#   ]
# }


def main(model_name: str, request: str):
    #TODO:
    # 1. Create OpenAIClient with OPENAI_HOST + /v1/images/generations as endpoint
    # 2. Call client with:
    #   - model=model_name
    #   - prompt=request
    # 3. Get b64_json content from data[0] and assign to `image_base64` variable
    # 4. Decode it with base64.b64decode and assign to `image_bytes` variable
    # 5. Create filename as `f"{datetime.now()}.png"` ({current datetime}.png)
    # 6. open filename (wb) and write `image_bytes`
    raise NotImplementedError


main(
    #TODO:
    # - model_name gpt-image-1
    # - request="Smiling catdog"
)
