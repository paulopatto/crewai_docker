from langchain_google_genai import ChatGoogleGenerativeAI
#from langchain_groq import ChatGroq
import app.settings

GeminiModel = ChatGoogleGenerativeAI(
  model = app.settings.GEMINI_MODEL_NAME,
  temperature = 0.2,
  convert_system_message_to_human=True,
  google_api_key = app.settings.GEMINI_API_KEY,
  verbose = False
)


