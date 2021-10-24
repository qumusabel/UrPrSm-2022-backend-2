from ariadne import convert_kwargs_to_snake_case, MutationType

from .. import db
from .utils import fail, ok, filter_none


def _make_adder(model):
    field_name = model.__name__.lower()

    def func(_, info, **params):
        obj = model(**params)
        db.queries.add(obj)
        return ok(field_name, obj)
    
    func.__name__ = f"add{model.__name__}" 
    return func


def _make_updater(model):
    field_name = model.__name__.lower()
    id_key = f"{field_name}Id"

    def func(_, info, **params):
        id = params.pop(id_key)

        if db.queries.get_one(model, id) is None:
            return fail([f"{field_name} id={id} not found"])

        db.queries.update(model, id, filter_none(params))

        obj = db.queries.get_one(model, id)
        return ok(field_name, obj)

    func.__name__ = f"update{model.__name__}"
    return func


def _make_remover(model):
    field_name = model.__name__.lower()

    def func(_, info, **params):
        id = params.get(f"{field_name}Id")
        if db.queries.get_one(model, id) is None:
            return fail([f"{field_name} id={id} not found"])

        db.queries.delete(model, id)
        return {"success": True}
    
    func.__name__ = f"remove{model.__name__}"
    return func


mutation = MutationType()

mutation.set_field("addBouquet",  _make_adder(db.models.Bouquet))
mutation.set_field("updateBouquet",  _make_updater(db.models.Bouquet))
mutation.set_field("removeBouquet",  _make_remover(db.models.Bouquet))

mutation.set_field("addCustomer", _make_adder(db.models.Customer))
mutation.set_field("updateCustomer", _make_updater(db.models.Customer))
mutation.set_field("removeCustomer", _make_remover(db.models.Customer))

mutation.set_field("addSeller",   _make_adder(db.models.Seller))
mutation.set_field("updateSeller",   _make_updater(db.models.Seller))
mutation.set_field("removeSeller",   _make_remover(db.models.Seller))


@mutation.field("purchaseBouquet")
@convert_kwargs_to_snake_case
def purchase_bouquet(_, info, bouquet_id, customer_id):
    errors = []

    bouquet = db.queries.get_one(db.models.Bouquet, bouquet_id)
    if bouquet is None:
        errors.append(f"bouquet id={bouquet_id} not found")

    customer = db.queries.get_one(db.models.Customer, customer_id)
    if customer is None:
        errors.append(f"customer id={customer_id} not found")

    if errors:
        return fail(errors)

    purchase = db.models.Purchase(
            bouquetId=bouquet_id, 
            customerId=customer_id,
            price=bouquet.price, 
            commission=bouquet.price * 0.3)
    
    db.queries.add(purchase)
    db.queries.update(db.models.Seller, bouquet.sellerId,
            {"bouquetsSold": db.models.Seller.bouquetsSold + 1})
    
    result = db.queries.get_one(db.models.Purchase, purchase.id)

    return ok("purchase", result)

