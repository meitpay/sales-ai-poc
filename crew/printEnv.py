from dotenv import load_dotenv
import os

load_dotenv()

print("OPENAI_API_KEY=" + os.environ.get('OPENAI_API_KEY'))
print("OPENAI_MODEL_NAME=" + os.environ.get('OPENAI_MODEL_NAME'))
