This is a side project to learn more about LLMs by building an LLM that RAGs your notes.

1. Request access to [Llama-2-70b-chat-hf](https://huggingface.co/meta-llama/Llama-2-70b-chat-hf)
2. Create new full write access Hugging Face token [here](https://huggingface.co/settings/tokens). Save your token for the next step.
3. Input your token after running the commands below

```bash
pip install -U "huggingface_hub[cli]"
huggingface-cli login
```

4. Next start up a virtual environment in `llm-service/`

```bash
cd llm-service
python3 -m venv env
source env/bin/activate
pip install langchain_huggingface langchain accelerate fastapi uvicorn
```

3. Run the app in app.py where your FastAPI server lives

```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

4. Test out prompting your Llama 2 node

```bash
curl -X POST "http://localhost:8000/prompt/" -H "Content-Type: application/json" -d '{"query": "What's the first rule of fight club?"}'
```
