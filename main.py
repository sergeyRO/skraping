import requests
import bs4

if __name__ == '__main__':
    KEYWORDS = ['дизайн', 'фото', 'web', 'python']
    responce = requests.get('https://habr.com/ru/all/')
    soup = bs4.BeautifulSoup(responce.text, 'html.parser')

    for article in soup.find_all('article'):
        responce_article = requests.get(f"https://habr.com{article.find('h2').find('a').get('href')}")
        soup1 = bs4.BeautifulSoup(responce_article.text, 'html.parser')
        text_article = soup1.find('div', id='post-content-body').get_text()

        if set(KEYWORDS) & set(text_article.split()):
            # < дата > - < заголовок > - < ссылка >
            print(f"{article.find('time').get('title')} - "
                  f"{article.find('h2').find('span').get_text()} - "
                  f"{article.find('h2').find('a').get('href')}")
