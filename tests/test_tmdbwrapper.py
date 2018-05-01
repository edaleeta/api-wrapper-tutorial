from pytest import fixture
from tmdbwrapper import TV
import vcr


@fixture
def tv_keys():
    #  Responsible only for returning the test data.
    keys = ["id", "origin_country", "poster_path", "name",
            "overview", "popularity", "backdrop_path", "first_air_date",
            "vote_count", "vote_average"]
    return keys


@vcr.use_cassette("tests/vcr_cassettes/tv-info.yml")
def test_tv_info(tv_keys):
    """Tests an API call to get a TV show's info."""

    tv_instance = TV(63247)
    response = tv_instance.info()

    assert isinstance(response, dict)
    assert response["id"] == 63247, "The ID should be in the response."
    assert set(tv_keys).issubset(response.keys()), (
           "All keys should be in the response.")


@vcr.use_cassette("tests/vcr_cassettes/tv-popular.yml")
def test_tv_popular(tv_keys):
    """Tests an API call to get popular TV shows."""

    response = TV.popular()

    assert isinstance(response, dict)
    assert isinstance(response["results"], list)
    assert isinstance(response["results"][0], dict)
    assert set(tv_keys).issubset(response["results"][0].keys())
