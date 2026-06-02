async def create_short_url(db, long_url):

    print("Function called")

    short_code = generate_short_code()

    print("Generated:", short_code)

    url = URL(
        long_url=long_url,
        short_code=short_code
    )

    print("Object created")

    db.add(url)

    print("Added to session")

    db.commit()

    print("Committed")

    db.refresh(url)

    print("Saved ID:", url.id)

    return {
        "short_code": short_code,
        "short_url": f"http://localhost:8000/{short_code}"
    }