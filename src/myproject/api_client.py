import requests


advoce_url = "https://api.adviceslip.com/advice"


def get_advice(timeout: int = 5) -> str:
    try:
        response = requests.get(advoce_url, timeout=timeout)
        response.raise_for_status()
    except requests.exceptions.RequestException as exc:
        raise RuntimeError(f"Ошибка при запросе {exc}")

    data = response.json()
    return data["slip"]["advice"]
