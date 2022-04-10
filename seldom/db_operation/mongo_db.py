try:
    from pymongo import MongoClient
except ModuleNotFoundError:
    raise ModuleNotFoundError("Please install the library. https://github.com/mongodb/mongo-python-driver")


class MongoDB:

    def __new__(cls, host, port, db):
        """
        Connect the mongodb database
        """
        client = MongoClient(host, port)
        db_obj = client[db]
        return db_obj


if __name__ == '__main__':
    mongo_db = MongoDB("localhost", 27017, "yapi")
    col = mongo_db.list_collection_names()
    print("collection list: ", col)
    data = mongo_db.project.find_one()
    print("table one data:", data)


