import json

import requests

from task.constants import OPENAI_HOST, OPENAI_API_KEY

# https://platform.openai.com/docs/guides/speech-to-text?lang=curl


class OpenAIClient:
    def __init__(self):
        #TODO:
        # 1. Set up `_api_key` (use OPENAI_API_KEY env var), don't forget to check that it is present and add 'Bearer ' prefix
        # 2. Set up `_endpoint` (OPENAI_HOST + "/v1/audio/transcriptions")
        raise NotImplementedError

    def call(self, audio_file_path: str,  print_response=True, **kwargs):
        #TODO:
        # 1. Set up `headers` dict, provide Authorization header with self._api_key
        # 2. Create dict `{'file': open(audio_file_path, 'rb')}` and assign to `files` variable
        # 3. Make POST request (use `requests` lib) with such params:
        #   - url=self._endpoint
        #   - headers=headers
        #   - files=files
        #   -  data=kwargs
        # 4. Close files read `files['file'].close()`
        # 5. If response is 200 then:
        #   - get json from response
        #   - print(json.dumps(data, indent=2))
        # 5.1. Otherwise, raise Exception(f"HTTP {response.status_code}: {response.text}")
        raise NotImplementedError


client = OpenAIClient()
client.call(
    #TODO:
    # - model_name gpt-4o-transcribe or whisper-1
    # - audio_file_path="codeus_audio.mp3"
    # - Optional, try to do that with audio on different languages
)
