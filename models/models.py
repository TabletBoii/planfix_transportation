

from sqlalchemy import String, Column, Unicode, Date, Boolean, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class GlobalTransportation(Base):
    __tablename__ = "planfix_transportation"

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    claim_id = Column('claim_id', String)
    claim_name = Column('claim_name', String)
    claim_status = Column('claim_status', String)
    fact_date_begin = Column('fact_date_begin', Date)
    fact_date_end = Column('fact_date_end', Date)
    plan_date_begin = Column('plan_date_begin', Date)
    plan_date_end = Column('plan_date_end', Date)
    pay_date = Column('pay_date', Date)
    invoicing_date = Column('invoicing_date', Date)
    customer = Column('customer', String)
    customer_iin = Column('customer_iin', String)
    customer_route = Column('customer_route', String)
    selling_price = Column('selling_price', String)
    selling_currency = Column('selling_currency', String)
    buying_price = Column('buying_price', String)
    buying_currency = Column('buying_currency', String)
    driver = Column('driver', String)
    vehicle = Column('vehicle', String)
    carrier = Column('carrier', String)
    debt_customer = Column('debt_customer', String)
    debt_currency_customer = Column('debt_currency_customer', String)
    debt_carrier = Column('debt_carrier', String)
    debt_currency_carrier = Column('debt_currency_carrier', String)
    customer_vat_type = Column('customer_vat_type', String)
    carrier_vat_type = Column('carrier_vat_type', String)
    shipping_type = Column('shipping_type', String)
    rolling_stock_type = Column('rolling_stock_type', String)
    cargo_consolidation = Column('cargo_consolidation', String)
    distance_km = Column('distance_km', String)
    avr_number = Column('avr_number', String)
    avr_date = Column('avr_date', Date)
    electronic_invoice_number = Column('electronic_invoice_number', String)
    electronic_invoice_date = Column('electronic_invoice_date', Date)
    shipping_datetime = Column('shipping_datetime', Date)
    vehicle_number = Column('vehicle_number', String)
    logistics_assistant = Column('logistics_assistant', String)
    clearance_date = Column('clearance_date', Date)
    convertion_date = Column('convertion_date', Date)
    customer_vat = Column('customer_vat', String)
    carrier_vat = Column('carrier_vat', String)
    assigner = Column('assigner', String)
    point_one = Column('point_one', String)
    point_two = Column('point_two', String)
    point_three = Column('point_three', String)
    point_four = Column('point_four', String)
    point_five = Column('point_five', String)
    point_one_id = Column('point_one_id', Integer)
    point_two_id = Column('point_two_id', Integer)
    point_three_id = Column('point_three_id', Integer)
    point_four_id = Column('point_four_id', Integer)
    point_five_id = Column('point_five_id', Integer)
    parent_claim = Column('parent_claim', String)


class Expenses(Base):
    __tablename__ = "planfix_expenses_data"

    id = Column('id', String, primary_key=True, autoincrement=True)
    claim_name = Column('claim_name', String)
    claim_id = Column('claim_id', String)
    pay_date = Column('pay_date', Date)
    subitem = Column('subitem', String)
    turnover_date = Column('turnover_date', Date)
    currency = Column('currency', String)
    subitem_id = Column('subitem_id', String)
    amount_to_pay = Column('amount_to_pay', String)
    paid = Column('paid', String)
    acquisition_cost = Column('acquisition_cost', String)
    payment_type = Column('payment_type', String)
    project = Column('project', String)
    project_id = Column('project_id', String)
    organization = Column('organization', String)
    has_photo_confirmation = Column('has_photo_confirmation', Boolean)
    initiator = Column("initiator", String)
    # template_name = Column("template_name", String)


class IndustrialTransportation(Base):
    __tablename__ = "industrial_transportation"

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    work_name = Column('work_name', String)
    date_period = Column('date_period', String)
    debt_customer_accepted = Column('debt_customer_accepted', Integer)
    data_type = Column('data_type', String)
    sell_price_accepted = Column('sell_price_accepted', Integer)
    buy_price = Column('buy_price', Integer)
    details = Column('details', String)
    buy_price_accepted = Column('buy_price_accepted', Integer)
    customer = Column('customer', String)
    sell_price = Column('sell_price', Integer)
    currency = Column('currency', String)
    debt_customer = Column('debt_customer', Integer)
    claim_name = Column('claim_name', String)
    claim_id = Column('claim_id', Integer)
