import click
from Commands_Box.urls import Adding_to_database, Enter_your_links, Enter_the_categories


@click.group()
def cli():
    pass

@click.command()
def settup():
    print("Tworzę tabelę w bazie danych")
    db = Databass(getenv("DB_NAME"))
    db.creating_table(
        """CREATE TABLE Isemestr (id integer primary key autoincrement,
         category TEXT, category2 TEXT, url TEXT)""")

@click.command()
@click.argument("category")
@click.argument("category2")
@click.argument("url")
def add(category: str, category2: str, url):
    Adding_to_database(category, category2, url)

@click.command(name='linki')
@click.argument("category")
def index(category: str):
    Enter_your_links(category)

@click.command(name='kategorie')
def category():
    Enter_the_categories()
