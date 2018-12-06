from app.main import db
from app.main.model import BaseDocument

class Example(BaseDocument):
    '''
    from app.main.model.example import Example
    example = Example()
    example.name = 'alpine'
    example.save()
    example.to_json()
    # => See more how to use: http://docs.mongoengine.org/tutorial.html#getting-started
    '''
    '''
    Common field options; db_field, required, default, unique, unique_with, choices
    StringField: regex, max_length, min_length
    DateTimeField: NULL
    IntField: min_value, max_value
    ReferenceField: reverse_delete_rule
    '''
    # References
    # Fields
    name                        = db.StringField(min_length=1, max_length=255, required=True)
    # Methods
    # Custom methods
