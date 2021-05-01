import pymongo

client = pymongo.MongoClient('127.0.0.1:27017')

db = client.ncovi


def check_collection_exist(collection):
    if collection in db.list_collection_names():
        return True
    else:
        return False

# find all documents

def count_record(collection, dict):
    res = db[collection].find(dict).count()
    return res

def find_all(collection, dict,
             order=None,
             distinct=None,
             page=None,
             limit=None,
             incre=-1, disable_field = None):
    if page:
        if not limit:
            limit = 20
        page = int(page)
        limit = int(limit)
        if order:
            res = db[collection].find(dict, disable_field)\
                .sort(order, incre)\
                .skip((page - 1) * limit)\
                .limit(limit)
        else:
            res = db[collection].find(dict, disable_field)\
                .skip((page - 1) * limit)\
                .limit(limit)
    else:
        if order:
            res = db[collection].find(dict, disable_field).sort(order, incre)
        else:
            res = db[collection].find(dict, disable_field)
    if distinct:
        res = res.distinct(distinct)
        res = filter(lambda r: r != "", res)
    return res


# find one document


def find_one(collection, dict=None, field_not = None):
    if check_collection_exist(collection):
        return db[collection].find_one(dict, field_not)
    else:
        return None

# save document into database


def add_document(collection, dict, field_unique=None):
    
    try:
        if field_unique:
          db[collection].create_index(
            field_unique, unique=True, sparse=True)

        db[collection].insert(dict)
        message = {"status": True, "message": "Insert success"}
        if "id" in dict:
            message.update({"id": dict["id"]})
    except BaseException:
        message = {
            "status": False,
            "message": "{} is exists.".format(field_unique)}
    return message

# update document


def update_document(collection, query_dict, dict):
    return db[collection].update(query_dict, {"$set": dict})


# delete document


def delete_document(collection, dict):
    return db[collection].delete_one(dict)