from ariadne import QueryType, convert_kwargs_to_snake_case

from .. import db
from .utils import fail, ok


def _make_getter(model):
    field_name = model.__name__.lower()

    def func(_, info, **kwargs):
        id = kwargs.get(f"{field_name}Id")

        obj = db.queries.get_one(model, id)

        if obj is None:
            return fail([f"{field_name} id={id} not found"])

        return ok(field_name, obj)

    func.__name__ = field_name
    return func


def _make_all_getter(model):
    field_name = model.__name__.lower() + "s"

    def func(_, info):
        objs = db.queries.get_all(model)
        return ok(field_name, objs)

    func.__name__ = field_name
    return func


query = QueryType()

query.set_field("bouquet",  _make_getter(db.models.Bouquet))
query.set_field("customer", _make_getter(db.models.Customer))
query.set_field("seller",   _make_getter(db.models.Seller))

query.set_field("bouquets", _make_all_getter(db.models.Bouquet))
query.set_field("sellers",  _make_all_getter(db.models.Seller))


@query.field("purchases")
@convert_kwargs_to_snake_case
def purchases(_, info, customer_id):
    customer = db.queries.get_one(db.models.Customer, customer_id)
    if customer is None:
        return fail([f"customer id={customer_id} not found"])

    return ok("purchases", customer.purchases)

