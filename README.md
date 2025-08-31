# AI Content Generation

Practice with image analysis, image generation, text-to-speech (TTS), and speech-to-text (STT) using OpenAI APIs.

## 🎯 Task Overview

Complete 5 practical tasks to master AI content generation APIs including vision, image generation, and audio processing capabilities.

## 🎓 Learning Goals

By completing these tasks, you will learn:
- Analyze images using vision models
- Generate images with DALL-E and GPT models
- Convert speech to text with Whisper and 
- Convert text to speech with TTS models
- Process audio-to-audio conversations
- Work with different content modalities in AI applications

## 📋 Requirements

- Python 3.13
- pip
- OpenAI API key
- Basic understanding of HTTP requests and file handling

## 🔧 Setup

1. **Setup venv:**
   ```bash
   python -m venv .venv
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set your API key:**
    - Set OPENAI_API_KEY as env variable: https://platform.openai.com/settings/organization/api-keys

4. **Project structure:**
   ```
   task/
   ├── client.py                      ✅ Complete
   ├── constants.py                   ✅ Complete
   ├── t1/
   │   └── image_analysis.py          🚧 TODO: Implement image analysis
   ├── t2/
   │   ├── image_generation_dalle.py  🚧 TODO: Implement DALL-E generation
   │   └── image_generation_gpt.py    🚧 TODO: Implement GPT image generation
   ├── t3/
   │   └── speech_to_text.py          🚧 TODO: Implement STT
   ├── t4/
   │   └── text_to_speech.py          🚧 TODO: Implement TTS
   └── t5/
       └── speech_to_speech.py        🚧 TODO: Implement audio conversation
   ```

## 📝 Your Tasks

### 1. Complete [Image Analysis](task/t1/image_analysis.py)
- Analyze images from URL and local base64-encoded files
- Generate poems based on visual content
- Use `/v1/chat/completions` endpoint with vision capabilities

### Optional:
- Try to make image analysis with anthropic: https://docs.anthropic.com/en/docs/build-with-claude/vision

### 2. Complete [DALL-E Image Generation](task/t2/image_generation_dalle.py)
- Generate images using DALL-E 3 model
- Experiment with different sizes, styles, and quality settings
- Use `/v1/images/generations` endpoint

### 3. Complete [GPT Image Generation](task/t2/image_generation_gpt.py)
- Generate images using GPT-Image-1 model
- Handle base64 response format
- Save generated images locally

### 4. Complete [Speech to Text](task/t3/speech_to_text.py)
- Transcribe audio files using Whisper or GPT-4o-transcribe
- Handle multipart/form-data requests
- Use `/v1/audio/transcriptions` endpoint

### 5. Complete [Text to Speech](task/t4/text_to_speech.py)
- Convert text to speech using TTS models
- Save audio output as MP3 files
- Use `/v1/audio/speech` endpoint

### 6. Complete [Speech to Speech](task/t5/speech_to_speech.py)
- Process audio input and generate audio responses
- Handle multimodal conversations
- Use base64 audio encoding/decoding

## 📚 API References

### Vision API
- [Image Analysis Guide](https://platform.openai.com/docs/guides/images-vision?api-mode=chat)
- [Base64 Image Encoding](https://platform.openai.com/docs/guides/images-vision?api-mode=chat&format=base64-encoded)

### Image Generation APIs
- [DALL-E 3 Guide](https://platform.openai.com/docs/guides/image-generation?image-generation-model=dall-e-3)
- [GPT Image Generation](https://platform.openai.com/docs/guides/image-generation?image-generation-model=gpt-image-1)

### Audio APIs
- [Speech to Text Guide](https://platform.openai.com/docs/guides/speech-to-text)
- [Text to Speech Guide](https://platform.openai.com/docs/guides/text-to-speech)
- [Audio Conversations](https://platform.openai.com/docs/guides/audio?example=audio-in)

## ✅ Success Criteria

1. **Image Analysis**: Successfully analyze both URL and local images, generate creative content based on visual input
2. **Image Generation**: Create images using both DALL-E and GPT models with different configurations
3. **Audio Processing**: Convert between text and speech in both directions
4. **Multimodal Integration**: Handle audio-to-audio conversations with AI models

