from datetime import datetime
from utils.helpers import parse_date
from utils.constants import Urls
from models.csv_writer import CsvWriter
class PlayerProfile:
    def __init__(
        self,
        slug = None,
        id = None,
        long_name = None,
        gender = None,
        image_url = None,
        headshot_image_url=None,
        dob=None,
        dod=None,
        country_team_id=None) -> None:
        self.slug = slug
        self.id = id
        self.long_name = long_name
        self.gender = gender
        self.image_url =  image_url
        self.headshot_image_url = headshot_image_url
        self.dob = dob
        self.dod = dod
        self.country_team_id = country_team_id
    
    
    @staticmethod
    def from_json(json):
        headshot_image = json.get('headshotImage',None)
        image_url = json.get('imageUrl',None)
        if image_url:
            image_url = Urls.images_base_url +image_url
        if headshot_image:
            headshot_image_url = Urls.images_base_url+ headshot_image.get('url')
        else:
            headshot_image_url = None
        return PlayerProfile(
            slug= json.get('slug'),
            id=json.get('objectId'),
            long_name=json.get('longName'),
            gender = json.get('gender'),
            image_url= image_url,
            headshot_image_url=headshot_image_url,
            dob= parse_date(json.get('dateOfBirth',None)),
            dod = parse_date(json.get('dateOfDeath',None)),
            country_team_id=json.get('countryTeamId',None)
            
        )
    def get_player_url(self):
        if self.slug and self.id:
            return f"{self.slug}-{self.id}"
        return None
    
