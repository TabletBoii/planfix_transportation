

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
