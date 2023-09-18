from utils.constants import Urls
class PlayerShort:
    def __init__(self,slug,id):
        self.slug = slug
        self.id = id

    def get_url(self):
        return f"{Urls.player_url_by_id}?playerId={self.id}"
    
    @staticmethod
    def from_json(json):
        if not json:
            return None
        player = PlayerShort(slug=json.get('slug'),id= json.get('objectId'))
        #print(f"Created player {player.slug} with id: {player.id} from json")
        return player