import os
from dotenv import load_dotenv
from long_polling import get_reviews


def main():
    load_dotenv()
    dvmn_token = os.getenv('dvmn_token')
    tg_token = os.getenv('tg_token')
    url = 'https://dvmn.org/api/long_polling/'
    response = get_reviews(url, dvmn_token)


if __name__ == "__main__":
    main()


