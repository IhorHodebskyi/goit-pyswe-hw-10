from mongoengine import connect, Document, StringField, ListField, ReferenceField

connect(db="dbname", host="mongodb+srv://test:test@cluster0.1yso3.mongodb.net/")

class Author(Document):
    fullname = StringField(required=True)
    born_date = StringField()
    born_location = StringField()
    description = StringField()

class Quote(Document):
    tags = ListField(StringField())
    author = ReferenceField(Author)
    quote = StringField(required=True)
