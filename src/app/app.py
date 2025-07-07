

from src.messages import LANGUAGES 
from src.core.core import CoreLogic
import datetime

class OProgram:
    def __init__(self, language: str, time_provider=None):
        self.messages = self._load_messages(language)
        self.core_logic = CoreLogic(time_provider=time_provider) 

    def _load_messages(self, language: str) -> dict:
        if language in LANGUAGES:
            return LANGUAGES[language]
        raise ValueError(f"Langue non supportée : {language}")

    def _get_salutation_message(self) -> str:
        time_of_day_key = self.core_logic.get_time_of_day() 
        if time_of_day_key == "AM":
            return self.messages["salutation_am"]
        elif time_of_day_key == "PM":
            return self.messages["salutation_pm"]
        else:
            return self.messages["salutation_nuit"]

    def get_congratulation(self) -> str:
        return self.messages["felicitation"]

    def get_goodbye(self) -> str:
        return self.messages["adieu"]

    def palindrome(self, text: str) -> str:
        is_palindrome = self.core_logic.is_palindrome(text)
        display_reversed_text = self.core_logic.reverse_text(text)
        
        output = [self._get_salutation_message()]

        if is_palindrome:
            output.append(self.get_congratulation())
        else:
            output.append(display_reversed_text)
        
        output.append(self.get_goodbye())
        
        return "\n".join(output)