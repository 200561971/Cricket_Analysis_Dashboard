from datetime import datetime
def get_format_by_id(format_id):
    formats = {
        1: "Tests",
        2: "ODI",
        4: "First-Class",
        5: "List A",
        6: "T20"
    }
    return formats.get(format_id)

def parse_date(json):
        if not json:
            return None
        year = json.get('year')
        month = json.get('month')
        day = json.get('date')
        return datetime(year = year, month = month, day= day)