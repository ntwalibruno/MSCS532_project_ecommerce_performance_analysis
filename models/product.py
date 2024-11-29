import datetime

class Product:
    def __init__(self, id, product_type, product_name, comments_id, insert_date, creation_date, creator_id):
        self.id = id
        self.product_type = product_type
        self.product_name = product_name
        self.comments_id = comments_id
        self.insert_date = self.parse_date(insert_date)
        self.creation_date = self.parse_date(creation_date)
        self.creator_id = creator_id

    @staticmethod
    def parse_date(date_str):
        return datetime.datetime.fromisoformat(date_str)

    def to_dict(self):
        return {
            "id": self.id,
            "product_type": self.product_type,
            "product_name": self.product_name,
            "comments_id": self.comments_id,
            "insert_date": self.insert_date.isoformat(),
            "creation_date": self.creation_date.isoformat(),
            "creator_id": self.creator_id
        }

    #Object print
    def __repr__(self):
        return f"Product(id={self.id}, product_type='{self.product_type}', product_name='{self.product_name}', comments_id={self.comments_id}, insert_date='{self.insert_date}', creation_date='{self.creation_date}', creator_id={self.creator_id})"

