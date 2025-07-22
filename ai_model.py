"""
This module defines the AiModel class, which serves as a base class for AI models.
It includes attributes for model type, name, API key, and configuration, along with methods for
preparing the model and providing string representations.
"""

from typing import Dict, Any

class AiModel:
    OLLAMA: str = "ollama"
    OPEN_AI: str = "open_ai"

    def __init__(
        self,
        type: str = "ollama",
        model_name: str = "llama3.1:8b",
        api_key: str = "http://localhost:11434/api/chat",
        config: Dict[str, Any] = dict(),
    ):
        self.type = type
        self.model_name = model_name
        self.api_key = api_key
        self.config = config
        self._prepare_model()

    def _prepare_model(self) -> None:
        """
        Prepares the model for use.
        This method can be overridden by subclasses to implement specific model preparation logic.
        """
        match self.type:
            case AiModel.OLLAMA:
                pass
            case _:
                pass

    def _prepare_ollama(self) -> None:
        pass
        
    def __repr__(self):
        """
        Returns a string representation of the AiModel instance.
        This is useful for debugging and logging purposes.
        :return: A string representation of the AiModel instance.
        """
        return f"Model(type={self.type}, model_name={self.model_name}, api_key={self.api_key}, config={self.config})"
    
    def __str__(self):
        """
        Returns a concise string representation of the AiModel instance.
        This is useful for displaying the model information in a user-friendly format.
        :return: A concise string representation of the AiModel instance.
        """
        return f"Model(type={self.type}, model_name={self.model_name}"