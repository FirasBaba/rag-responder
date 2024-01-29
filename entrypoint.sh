ollama serve &
sleep 1
ollama pull $OLLAMA_MODEL_NAME
tail -f /dev/null
