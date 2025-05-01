import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app_instagram.settings')
django.setup()

from app_main.models import Author as PgAuthor, Quote as PgQuote
from mongo_models import Author as MgAuthor, Quote as MgQuote  # mongoengine моделі

def migrate_data():
    for mg_author in MgAuthor.objects:
        pg_author, _ = PgAuthor.objects.get_or_create(
            fullname=mg_author.fullname,
            defaults={
                "born_date": mg_author.born_date,
                "born_location": mg_author.born_location,
                "description": mg_author.description
            }
        )

        for mg_quote in MgQuote.objects(author=mg_author):
            PgQuote.objects.get_or_create(
                quote=mg_quote.quote,
                author=pg_author,
                defaults={"tags": ', '.join(mg_quote.tags)}
            )

    print("Дані перенесено!")

if __name__ == '__main__':
    migrate_data()
