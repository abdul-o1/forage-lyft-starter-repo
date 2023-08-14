from abc import ABC , abstractmethod
from datetime import date

class Battery (ABC): 
    def needs_service(self) -> bool:
        return True