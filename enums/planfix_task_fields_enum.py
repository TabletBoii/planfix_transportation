from enum import Enum


class HasGlobalTransportationFieldsEnum(Enum):
    FACT_DATE_BEGIN = "86186"  # ФАКТ.дата начальной погрузки (ЗАФИКСИРОВАННАЯ)
    FACT_DATE_END = "71486"  # Фактическая дата последней выгрузки
    PLAN_DATE_BEGIN = "85686"  # Планируемая дата начальной погрузки
    PLAN_DATE_END = "85688"  # Планируемая дата последней выгрузки
    PAY_DATE = "85856"  # Дата оплаты
    INVOICING_DATE = "87396"  # Дата выставления счета на оплату
    CUSTOMER = "67174"  # Заказчик
    CUSTOMER_IIN = "86914"  # Заказчик (БИН/ИИН)
    CUSTOMER_ROUTE = "67108"  # Маршрут
    # ТОЧКИ ПОСМОТРЕТЬ И ПРОПИСАТЬ ОТДЕЛЬНО
    SELLING_PRICE = "86182"  # Стоимость продажи
    SELLING_CURRENCY = "67116"  # Валюта продажи
    BUYING_PRICE = "86184"  # Стоимость покупки
    BUYING_CURRENCY = "67156"  # Валюта покупки
    DRIVER = "67148"  # Водитель
    VEHICLE = "67292"  # Автотранспорт
    CARRIER = "67176"  # Перевозчик (ЮЛ/ЧЛ)
    DEBT_CUSTOMER = "86690"  # ДЗ заказчику (сумма)
    DEBT_CURRENCY_CUSTOMER = "85834"  # Валюта ДЗ (ЗАКАЗЧИКА)
    DEBT_CARRIER = "86692"  # ДЗ перевозчику (сумма)
    DEBT_CURRENCY_CARRIER = "85836"  # Валюта ДЗ (ПЕРЕВОЗЧИК)
    CUSTOMER_VAT_TYPE = "85830"  # Вид НДС заказчика
    CARRIER_VAT_TYPE = "85832"  # Вид НДС (ПЕРЕВОЗЧИКА)
    # посмотреть, как называется системное поле Постановщик
    SHIPPING_TYPE = "85736"  # Тип перевозки
    ROLLING_STOCK_TYPE = "67134"  # Вид подвижного состава
    CARGO_CONSOLIDATION = "67140"  # Консолидация груза
    DISTANCE_KM = "86174"  # Расстояние (в километрах)
    AVR_NUMBER = "71316"  # Номер АВР
    AVR_DATE = "71318"  # Дата АВР
    ELECTRONIC_INVOICE_NUMBER = "71320"  # Номер ЭСФ
    ELECTRONIC_INVOICE_DATE = "71322"  # Дата ЭСФ
    SHIPPING_DATETIME = "67260"  # Дата и время доставки
    VEHICLE_NUMBER = "85684"  # Собственное ТС (номер)
    LOGISTICS_ASSISTANT = "87312"  # Ассистент логиста
    CLEARANCE_DATE = "87338"  # Дата растаможки (ЗАФИКСИРОВАННАЯ)
    CONVERTION_DATE = "87356"  # Дата конвертации (для перевозчиков, в случае валютных перевозок)
    CUSTOMER_VAT = "87358"  # НДС заказчика (по договору)
    CARRIER_VAT = "87360"  # НДС перевозчика (по договору)


class HasGlobalTransportationTemplateEnum(Enum):
    ECOVICE_CITY_TRANSPORTATION = 92659  # Перевозка ЭКОВИС по городу
    MULTIMODAL_TRANSPORTATION = 161749  # Мультимодальная Перевозка
    MAREVEN_CITY_TRANSPORTATION = 1762  # Перевозка Маревен по городу
    LG_ELECTRONICS_TRANSPORTATION = 95357  # Перевозка LG Electronics
    OP_TRANSPORTATION = 203641  # Перевозка ОП
    TRANSPORTATION = 17  # Перевозка
    CHINA_TRANSITION_TRANSPORTATION = 323059  # Перевозка через Китай
    CHINA_TRANSPORTATION_EXPENSES = 336921  # Расходы по перевозке через Китай
    ADDITIONAL_TRANSPORTATION_EXPENSES = 357366  # Доп. расходы по перевозке
    METAL_PROFILE_TRANSPORTATION = 317127  # Перевозка Завод Металл Профиль
    MAGNUM_TRANSPORTATION = 1197  # Перевозка Магнум
    EURASIAN_MACHINERY_TRANSPORTATION = 2361  # Перевозка Евразиан Машинери
