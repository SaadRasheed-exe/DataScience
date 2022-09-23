# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import sqlite3


class PracticePipeline:

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.connection = sqlite3.connect('quotes.db')
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute("""DROP TABLE IF EXISTS quotes_table""")
        self.cursor.execute("""CREATE TABLE quotes_table(
            quote text,
            author text,
            tags text
        )""")

    def insert_values(self, item):
        self.cursor.execute("""INSERT INTO quotes_table VALUES (?,?,?)""",
                            (
                                item['text'][0],
                                item['author'][0],
                                item['tags'][0]
                            ))
        self.connection.commit()

    def process_item(self, item, spider):
        self.insert_values(item)
        return item
