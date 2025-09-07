from enum import Enum

class LLMEunms(Enum):

    OPENAI = "OPENAI"
    COHERE = "COHERE"

class OpenAiEnums(Enum):

    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"

class CoHereEnums(Enum):

    SYSTEM = "SYSTEM"
    USER = "USER"
    ASSISTANT = "CHATBOT"

    DOCUMENT = "search_document"
    QUERY = "search_query"

class DocumentTypeEnum(Enum):

    DOCUMENT = "document"
    QUERY = "query"