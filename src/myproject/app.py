from api_server import get_daily_advice
from utils import print_advice


def main():
    try:
        advice = get_daily_advice()
        print_advice(advice)
    except RuntimeError as error:
        print(f"X {error}")


if __name__ == "__main__":
    main()
