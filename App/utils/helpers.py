from datetime import datetime
def get_format_by_id(format_id):
    formats = {
        1: "Tests",
        2: "ODI",
        3: "T20I",
        4: "First-Class",
        5: "List A",
        6: "T20",
        7: "",
        8: "Women's Tests",
        9: "Women's ODI",
        10: "Women's T20I"
    }
    return formats.get(format_id)

def parse_date(json):
        if not json:
            return None
        year = json.get('year')
        month = json.get('month')
        day = json.get('date')
        if (year == None or month == None) or day == None:
             return None
        return datetime(year = year, month = month, day= day).date()