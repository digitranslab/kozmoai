FROM kozmoai/kozmoai:1.0-alpha

CMD ["python", "-m", "kozmoai", "run", "--host", "0.0.0.0", "--port", "7860"]
