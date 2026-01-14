from api_client import get_advice


def get_daily_advice() -> str:
    return get_advice()
