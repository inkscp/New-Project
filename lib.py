import requests

def count_word_at_url(url):
    """
    это ф-ция для примера как вызывается async

    """
    response = requests.get(url)
    print(len(response.text.split()))
    return len(response.text.split())

