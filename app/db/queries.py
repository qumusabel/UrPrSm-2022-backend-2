from ..server import db

def add(object):
    db.session.add(object)
    db.session.commit()

def get_one(model, id):
    return db.session.query(model).get(id)

def get_all(model):
    return db.session.query(model).all()

def update(model, id, values):
    db.session.query(model).filter(model.id == id).update(values)
    db.session.commit()

def delete(model, id):
    db.session.query(model).filter(model.id == id).delete()
    db.session.commit()

