from utils.constants import Urls
class Team:
    def __init__(
        self,
        id = None,
        slug = None,
        name = None,
        abbr = None,
        flag_url = None,
        players_db = None
    ):
        self.id = id
        self.name =name
        self.slug= slug
        self.abbr = abbr
        self.flag_url = Team.parse_flag_url(flag_url)
        

    @staticmethod
    def parse_flag_url(flag_url):
        if not flag_url:
            return ''
        return Urls.images_base_url+flag_url
    
    @staticmethod
    def from_json(json):
        if not json:
            return None
        return Team(
            id = json.get('objectId'),
            slug = json.get('slug'),
            name = json.get('longName'),
            abbr= json.get('abbreviation'),
            flag_url = json.get('imageUrl')
        )
    def __repr__(self):
        return f"Team(id={self.id!r}, name={self.name!r}, slug={self.slug!r}, abbr={self.abbr!r}, flag_url={self.flag_url!r})"

    def __str__(self):
        return self.__repr__()