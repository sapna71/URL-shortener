from fastapi.responses import RedirectResponse

async def get_original_url(db, short_code: str):
    return RedirectResponse(
        url="https://google.com",
        status_code=307
    )