from tmdbwrapper import TV

def test_tv_info():
    """Tests an API call to get a TV show's info."""

    tv_instance = TV(63247)
    response = tv_instance.info()

    assert isinstance(response, dict)
    assert response["id"] == 63247, "The ID should be in the response."