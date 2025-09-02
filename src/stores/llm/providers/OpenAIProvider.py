from ..LLMInterFace import LLMInterFace
from ..LLMEnums import OpenAiEnums
from openai import OpenAI
import logging

class OpenAIProvider(LLMInterFace):

    def __init__(self, api_key: str, api_url: str = None,
                        defualt_input_max_characters: int=1000,
                        defualt_generation_max_output_tokens: int=1000,
                        defualt_generation_temperature: float=0.1):
        
        self.api_key = api_key
        self.api_url = api_url

        self.defualt_input_max_characters = defualt_input_max_characters
        self.defualt_generation_max_output_tokens = defualt_generation_max_output_tokens
        self.defualt_generation_temperature = defualt_generation_temperature

        self.generation_model_id = None

        self.embedding_model_id = None
        self.embedding_size = None

        self.client = OpenAI(
            api_key = self.api_key,
            base_url = self.api_url if self.api_url and len(self.api_url) else None
        )

        self.logger = logging.getLogger(__name__)

        self.enums = OpenAiEnums

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

        chat_history.append(
            self.construct_prompt(prompt=prompt , role=OpenAiEnums.USER.value)
        )

        response = self.client.chat.completions.create(
            model = self.generation_model_id,
            messages = chat_history,
            max_tokens = max_output_tokens,
            temperature = temperature
        )

        if not response or not response.choices or not len(response.choices) == 0 or not response.choices[0].message:
            self.logger.error("Error while generating text with OpenAI")
            return None
        
        return response.choices[0].message.content
    
    def embed_text(self, text: str, document_type: str = None):

        if not self.client:
            self.logger.error("OpenAI Client was not set")
            return None
        
        if not self.embedding_model_id:
            self.logger.error("Embedding model for OpenAI was not set")
            return None
        
        response = self.client.embeddings.create(
            model= self.embedding_model_id,
            input= text
        )

        if not response or not response.data or not len(response.data) == 0 or not response.data[0].embedding:
            self.logger.error("Error while embedding text with OpenAI")
            return None
        
        return response.data[0].embedding
    

    def construct_prompt(self, prompt: str, role: str):

        return{
            "role": role,
            "content": self.process_text(prompt)
        }