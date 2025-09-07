from .LLMEnums import LLMEunms
from .providers import OpenAIProvider , CoHereProvider

class LLMProviderFactory:
    def __init__(self, config: dict):
        self.config = config


    def create(self, provider: str):

        if provider == LLMEunms.OPENAI.value:
            return OpenAIProvider(
                api_key= self.config.OPENAI_API_KEY,
                api_url= self.config.OPENAI_API_URL,
                defualt_input_max_characters= self.config.INPUT_DEFUALT_MAX_CHARACTERS,
                defualt_generation_max_output_tokens= self.config.GENERATION_DEFUALT_MAX_TOKENS,
                defualt_generation_temperature= self.config.GENERATION_DEFUALT_TEMPERATURE
            )

        if provider == LLMEunms.COHERE.value:
            return CoHereProvider(  
                api_key= self.config.COHERE_API_KEY,
                defualt_input_max_characters= self.config.INPUT_DEFUALT_MAX_CHARACTERS,
                defualt_generation_max_output_tokens= self.config.GENERATION_DEFUALT_MAX_TOKENS,
                defualt_generation_temperature= self.config.GENERATION_DEFUALT_TEMPERATURE
            )
        
        return None