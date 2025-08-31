import json
from datetime import datetime
from typing import Any

import requests

from task.constants import OPENAI_HOST, OPENAI_API_KEY

# https://platform.openai.com/docs/guides/text-to-speech
# Request:
# curl https://api.openai.com/v1/audio/speech \
#   -H "Authorization: Bearer $OPENAI_API_KEY" \
#   -H "Content-Type: application/json" \
#   -d '{
#     "model": "gpt-4o-mini-tts",
#     "input": "Why can't we say that black is white?",
#     "voice": "coral",
#     "instructions": "Speak in a cheerful and positive tone."
#   }' \
# Response:
#   bytes with audio


class OpenAIClient:

    def __init__(self):
        #TODO:
        # 1. Set up `_api_key` (use OPENAI_API_KEY env var), don't forget to check that it is present and add 'Bearer ' prefix
        # 2. Set up `_endpoint` (OPENAI_HOST + "/v1/audio/speech")
        raise NotImplementedError

    def call(self, print_request=True, **kwargs):
        #TODO:
        # 1. Set up `headers` dict, provide Authorization header with self._api_key and Content-Type as application/json
        # 2. Create output file name `f"{datetime.now()}.mp3"` and assign to `output_file` variable
        # 3. Print request: print(json.dumps(kwargs, indent=2))
        # 4. Make POST request (use `requests` lib) with such params:
        #   - url=self._endpoint
        #   - headers=headers
        #   - json=kwargs
        # 5. If response is 200 then:
        #   - Save it (open output_file (wb) and write byte `response.content`)
        #   - print(f"Audio saved to {output_file}")
        # 5.1. Otherwise, raise Exception(f"HTTP {response.status_code}: {response.text}")
        raise NotImplementedError


class Voice:
    alloy: str = 'alloy'
    ash: str = 'ash'
    ballad: str = 'ballad'
    coral: str = 'coral'
    echo: str = 'echo'
    fable: str = 'fable'
    nova: str = 'nova'
    onyx: str = 'onyx'
    sage: str = 'sage'
    shimmer: str = 'shimmer'


client = OpenAIClient()
client.call(
    #TODO:
    # - model_name gpt-4o-mini-tts
    # - input="Why can't we say that black is white?"
    # instructions="Speak in a cheerful and positive tone."
    # - voice - play with different types
)

