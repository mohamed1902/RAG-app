from enum import Enum

class LLMEunms(Enum):

    OPENAI = "OPENAI"
    COHERE = "COHERE"

class OpenAiEnums(Enum):

    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"