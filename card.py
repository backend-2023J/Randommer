import requests
from randommer import Randommer


class Card(Randommer):
    def get_card(self, api_key: str, type=None) -> dict:
        '''get card from randommer
        
        Args:
            api_key (str): api key
            type (str): card type

        Returns:
            dict: card data
        '''
        url = f"{self.get_url()}Card"

        
        headers = {
            "X-Api-Key": api_key
        }

        response = requests.get(url, headers=headers)
        
        return response.json()

    def get_card_types(self, api_key: str) -> list:
        '''get cars types from randommer

        Args:
            api_key (str): api key
            
        Returns:
            list: list of types
        '''
        pass


card = Card()
api_key = "f1ab06cd2da14928a4f4299e85162d76"
print(card.get_card(api_key=api_key))