from ..LLMInterFace import LLMInterFace
from ..LLMEnums import CoHereEnums , DocumentTypeEnum
import cohere
import logging

class CoHereProvider(LLMInterFace):

    def __init__(self, api_key: str, defualt_input_max_characters: int=1000,
                        defualt_generation_max_output_tokens: int=1000,
                        defualt_generation_temperature: float=0.1):
        
        self.api_key = api_key

        self.defualt_input_max_characters = defualt_input_max_characters
        self.defualt_generation_max_output_tokens = defualt_generation_max_output_tokens
        self.defualt_generation_temperature = defualt_generation_temperature

        self.generation_model_id = None

        self.embedding_model_id = None
        self.embedding_size = None

        self.client = cohere.Client(api_key = self.api_key)

        self.logger = logging.getLogger(__name__)

        self.enums = CoHereEnums

    
    def set_generation_model(self, model_id: str):

        self.generation_model_id = model_id


    def set_embedding_model(self, model_id: str, embedding_size: int):
        
        self.embedding_model_id = model_id
        self.embedding_size = embedding_size


    def process_text(self, text: str):

        return text[:self.defualt_input_max_characters].strip()
    

    def generate_text(self, prompt: str, chat_history: list=[], max_output_tokens: int=None,
                        temperature: float = None):

        if not self.client:
            self.logger.error("OpenAI Client was not set")
            return None 
        
        if not self.generation_model_id:
            self.logger.error("Generation model for OpenAI was not set")
            return None
        
        max_output_tokens = max_output_tokens if max_output_tokens else self.defualt_generation_max_output_tokens
        temperature = temperature if temperature else self.defualt_generation_temperature
        
        response = self.client.chat(
            model = self.generation_model_id,
            chat_history = chat_history,
            message = self.process_text(prompt),
            temperature = temperature,
            max_tokens = max_output_tokens
        )

        if not response or not response.text:
            self.logger.error("Error while generation text with CoHere")
            return None
        
        return response.text
    

    def embed_text(self, text: str, document_type: str = None):

        if not self.client:
            self.logger.error("CoHere Client was not set")
            return None
        
        if not self.embedding_model_id:
            self.logger.error("Embedding model for CoHere was not set")
            return None
        
        input_type = CoHereEnums.DOCUMENT
        if document_type == DocumentTypeEnum.QUERY:
            input_type = CoHereEnums.QUERY

        response = self.client.embed(
            model = self.embedding_model_id,
            texts = [self.process_text(text)],
            input_type = input_type,
            embedding_types = ['float']
        )

        if not response or not response.embeddings or not response.embeddings.float:
            self.logger.error("Error while embedding text with CoHere")
            return None
        
        return response.embeddings.float[0]


    def construct_prompt(self, prompt: str, role: str):

        return{
            "role": role,
            "text": self.process_text(prompt)
        }