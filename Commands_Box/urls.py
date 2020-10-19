from database import Databass
from os import getenv

def Adding_to_database(category: str, category2: str, url: str):
    print("Dodaję nowy adres URL")
    db = Databass(getenv("DB_NAME"))
    len_category = len(category)
    len_category2 = len(category2)
    len_url = len(url)
    if len_category != 1 and len_category2 != 1 and len_url != 5:
        if category2 != ".":
            category = category.title()
            category2 = category2.title()
            db.Insert("Isemestr", category, category2, url)
        else:
            category2 = ""
            category = category.title()
            db.Insert("Isemestr", category, category2, url)

def Enter_your_links(category: str):
    print(f"Lista linków z kategori {category}:")
    db = Databass(getenv("DB_NAME"))
    lins = db.fetch_all("Isemestr", category=category)
    urls = []
    for lin in lins:
        urls.append(lin[3])
    return urls


def Enter_the_categories():
    db = Databass(getenv("DB_NAME"))
    categories = db.fetch_category("Isemestr")
    categories2 = db.fetch_category2("Isemestr")
    del categories2[1]
    set_categories = {""}
    set_categories.remove("")
    category = []
    print("Lista kategori w bazie danych:")
    for name in categories:
        set_categories.add(name[0])
    for name in categories2:
        set_categories.add(name[0])
    for index in set_categories:
         category.append(index)
    return category

