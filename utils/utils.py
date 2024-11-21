import re

from enums.planfix_task_fields_enum import HasGlobalTransportationFieldsEnum, HasGlobalTransportationTemplateEnum


class Utils:

    @staticmethod
    def extract_first_6_digits(text: str) -> int | str:
        all_digits = re.findall(r'\d', text)

        digits_str = ''.join(all_digits)

        if len(digits_str) == 0:
            return 0

        claim_id = digits_str[:6]

        return claim_id

    @staticmethod
    def global_form_request_body(current_date: str, offset: int, page_offset: int = 100) -> dict:
        fields = ""
        templates = []

        for enum_index, field_enum in enumerate(HasGlobalTransportationFieldsEnum):
            if enum_index == len(HasGlobalTransportationFieldsEnum):
                fields += str(field_enum.value)
            else:
                fields += str(field_enum.value) + ","

        for field_enum in HasGlobalTransportationTemplateEnum:
            templates.append(field_enum.value)

        request_body = {
            "offset": offset,
            "pageSize": page_offset,
            "filters": [
                {
                    "type": 103,
                    "operator": "gt",
                    "value": {
                        "dateType": "otherDate",
                        "dateValue": f"{current_date}"
                    },
                    "field": 86186
                },
                # Шаблоны
                {
                    "type": 51,
                    "operator": "equal",
                    "value": templates
                },
            ],
            "fields": f"id,name,status,assigner,parent," + fields
        }

        return request_body

    @staticmethod
    def generate_task_dict(task_item: dict, organization: str) -> dict:
        splited_task_name = task_item["name"].split(" ")
        if "object" in task_item.keys():
            claim_id = splited_task_name[0]
        else:
            claim_result = Utils.extract_first_6_digits(task_item["name"])
            claim_id = claim_result if claim_result != 0 else task_item["id"]
        try:
            task_dict = {
                "claim_name": task_item["name"],
                "claim_id": claim_id,
                "claim_status": task_item["status"]["name"],
                "assigner": task_item["assigner"]["name"]
            }

        except Exception as e:
            print(e)
            print(splited_task_name)
            return

        if "parent" in task_item.keys():
            task_dict["parent_claim"] = str(task_item["parent"]["id"])
        else:
            task_dict["parent_claim"] = ""

        for field in task_item["customFieldData"]:
            try:
                match field["field"]["name"]:
                    case "ФАКТ.дата начальной погрузки (ЗАФИКСИРОВАННАЯ)":
                        task_dict["fact_date_begin"] = field["stringValue"]
                    case "Фактическая дата последней выгрузки":
                        task_dict["fact_date_end"] = field["stringValue"]
                    case "Планируемая дата начальной погрузки":
                        task_dict["plan_date_begin"] = field["stringValue"]
                    case "Планируемая дата последней выгрузки":
                        task_dict["plan_date_end"] = field["stringValue"]
                    case "Дата оплаты":
                        task_dict["pay_date"] = field["stringValue"]
                    case "Дата выставления счета на оплату":
                        task_dict["invoicing_date"] = field["stringValue"]
                    case "Заказчик":
                        task_dict["customer"] = field["stringValue"]
                    # case "БИН / ИНН":
                    #     task_dict["customer"] = field["stringValue"]
                    case "Маршрут":
                        task_dict["customer_route"] = field["stringValue"]
                    case "Стоимость продажи (утвержденная)":
                        try:
                            task_dict["selling_price"] = int(field["value"]) if "value" in field else 0
                        except Exception as e:
                            task_dict["selling_price"] = 0
                    case "Валюта продажи":
                        task_dict["selling_currency"] = field["stringValue"]
                    case "Стоимость покупки (утвержденная)":
                        try:
                            task_dict["buying_price"] = int(field["value"]) if "value" in field else 0
                        except Exception as e:
                            task_dict["buying_price"] = 0
                    case "Валюта покупки":
                        task_dict["buying_currency"] = field["stringValue"]
                    case "Водитель":
                        task_dict["driver"] = field["value"]["name"]
                    case "Автотранспорт":
                        task_dict["vehicle"] = field["stringValue"]
                    case "Перевозчик (ЮЛ/ЧЛ)":
                        task_dict["carrier"] = field["stringValue"]
                    case "ДЗ заказчику (УТВЕРЖДЕННОЕ)":
                        task_dict["debt_customer"] = field["stringValue"]
                    case "Валюта ДЗ (ЗАКАЗЧИКА)":
                        task_dict["debt_currency_customer"] = field["stringValue"]
                    case "ДЗ перевозчику (УТВЕРЖДЕННОЕ)":
                        task_dict["debt_carrier"] = field["stringValue"]
                    case "Валюта ДЗ (ПЕРЕВОЗЧИК)":
                        task_dict["debt_currency_carrier"] = field["stringValue"]
                    case "Вид НДС (ЗАКАЗЧИКА)":
                        task_dict["customer_vat_type"] = field["stringValue"]
                    case "Вид НДС (ПЕРЕВОЗЧИКА)":
                        task_dict["carrier_vat_type"] = field["stringValue"]
                    case "Тип перевозки":
                        task_dict["shipping_type"] = field["stringValue"]
                    case "Вид подвижного состава":
                        try:
                            task_dict["rolling_stock_type"] = field["value"]["value"]
                        except Exception as e:
                            task_dict["rolling_stock_type"] = ""
                    case "Консолидация груза":
                        task_dict["cargo_consolidation"] = field["stringValue"]
                    case "Расстояние (в километрах)":
                        task_dict["distance_km"] = field["stringValue"]
                    case "Номер АВР":
                        task_dict["avr_number"] = field["stringValue"]
                    case "Дата АВР":
                        task_dict["avr_date"] = field["stringValue"]
                    case "Номер ЭСФ":
                        task_dict["electronic_invoice_number"] = field["stringValue"]
                    case "Дата ЭСФ":
                        task_dict["electronic_invoice_date"] = field["stringValue"]
                    case "Дата и время доставки":
                        task_dict["shipping_datetime"] = field["stringValue"]
                    case "Собственное ТС (номер)":
                        task_dict["vehicle_number"] = field["stringValue"]
                    case "Ассистент логиста":
                        try:
                            task_dict["logistics_assistant"] = field["value"]["value"]
                        except Exception as e:
                            task_dict["logistics_assistant"] = ""
                    case "Дата растаможки (ЗАФИКСИРОВАННАЯ)":
                        task_dict["clearance_date"] = field["stringValue"]
                    case "Дата конвертации (для перевозчиков, в случае валютных перевозок)":
                        task_dict["convertion_date"] = field["stringValue"]
                    case "НДС заказчика (по договору)":
                        task_dict["customer_vat"] = field["stringValue"]
                    case "НДС перевозчика (по договору)":
                        task_dict["carrier_vat"] = field["stringValue"]
                    case "Точка 3":
                        task_dict["point_three"] = field["value"]["value"]
                        task_dict["point_three_id"] = field["value"]["id"]
                    case "Точка 2":
                        task_dict["point_two"] = field["value"]["value"]
                        task_dict["point_two_id"] = field["value"]["id"]
                    case "Точка 1":
                        task_dict["point_one"] = field["value"]["value"]
                        task_dict["point_one_id"] = field["value"]["id"]
                    case "Точка 4":
                        task_dict["point_four"] = field["value"]["value"]
                        task_dict["point_four_id"] = field["value"]["id"]
                    case "Точка 5":
                        task_dict["point_five"] = field["value"]["value"]
                        task_dict["point_five_id"] = field["value"]["id"]
            except Exception as e:
                print(e)
                print(field)
                pass

        return task_dict

    @staticmethod
    def exclude_incorrect_claims_by_name(task_name: str) -> bool:
        excluded_claim_names = [
            "{{Задача.Номер}}",
            "тест"
        ]

        for excluded_name in excluded_claim_names:
            if excluded_name in task_name:
                return False
        return True
