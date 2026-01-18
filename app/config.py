import os
from dotenv import load_dotenv

load_dotenv()

USE_MOCK_GENAI = os.getenv("USE_MOCK_GENAI", "true").lower() == "true"
