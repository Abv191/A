from django.core.management.base import BaseCommand
from quotes.models import Author, Quote
from pymongo import MongoClient


class Command(BaseCommand):
    help = 'Migrate data from MongoDB to PostgreSQL'

    def handle(self, *args, **kwargs):
        mongo_client = MongoClient('mongodb://your_mongo_user:your_mongo_password@localhost:27017/')
        mongo_db = mongo_client['quotes_mongo_db']

        authors_collection = mongo_db['quotes_author']
        quotes_collection = mongo_db['quotes_quote']

        authors = list(authors_collection.find())
        quotes = list(quotes_collection.find())

        for author in authors:
            new_author = Author(name=author['name'], bio=author['bio'])
            new_author.save()

        for quote in quotes:
            author = Author.objects.get(name=quote['author']['name'])
            new_quote = Quote(text=quote['text'], author=author)
            new_quote.save()

        self.stdout.write(self.style.SUCCESS('Successfully migrated data'))
