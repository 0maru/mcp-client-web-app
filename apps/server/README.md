# LLM API Gateway Server

FastAPI server with LiteLLM integration for accessing various LLM APIs through a unified interface.

## Setup

1. Install dependencies:
```bash
cd apps/server
uv sync
```

2. Configure environment variables:
```bash
cp .env.example .env
# Edit .env with your API keys
```

3. Run the server:
```bash
uv run uvicorn main:app --reload
```

## Available Endpoints

- `GET /` - Health check
- `GET /health` - Health status
- `POST /chat/completions` - Main chat endpoint (OpenAI-compatible)
- `GET /models` - List available models

## Supported Providers

LiteLLM supports multiple LLM providers:
- OpenAI (GPT-3.5, GPT-4)
- Anthropic (Claude)
- Google AI (Gemini)
- Azure OpenAI
- AWS Bedrock
- Cohere
- Replicate
- HuggingFace

## Usage Example

```bash
curl -X POST http://localhost:8000/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-3.5-turbo",
    "messages": [
      {"role": "user", "content": "Hello!"}
    ]
  }'
```

## Streaming Support

The API supports streaming responses by setting `stream: true` in the request:

```bash
curl -X POST http://localhost:8000/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": "Hello!"}],
    "stream": true
  }'
```