async def get_url_analytics(db, short_code: str):
    return {
        "short_code": short_code,
        "clicks": 0
    }