import requests
from sqlalchemy import text, insert
from sqlalchemy.orm import Session

from models.models import IndustrialTransportation
from utils import Utils
from enums.planfix_task_fields_enum import HasIndustrialSalesRevenueObjectsEnum
from abstraction.abstract_loader import HasExpensesLoader


class HasIndustrialExpensesLoader:

    def __init__(self, session, url, token, start_date):
        self.has_db_session: Session = session
        self.PLANFIX_URL = url
        self.PLANFIX_BEARER_TOKEN = token
        self.headers = {"Authorization": f"Bearer {self.PLANFIX_BEARER_TOKEN}"}
        self.task_list = []
        self.get_task_list_endpoint = 'task/list'
        self.get_task_list_url = self.PLANFIX_URL + self.get_task_list_endpoint
        self.start_date = start_date

    def get_planfix_expenses_query(self):
        return

    def fetch_planfix_tasks(self, current_date: str, current_offset: int, get_task_list_url: str) -> None:
        object_list = [object_enum.value for object_enum in HasIndustrialSalesRevenueObjectsEnum]
        while True:
            preprocessed_task_list = []
            print("Выгружаюся данные с оффсетом: ", current_offset)
            post_body = Utils.industrial_from_request_body(
                current_date=current_date,
                offset=current_offset
            )

            response = requests.post(get_task_list_url, headers=self.headers, json=post_body).json()
            if len(response["tasks"]) == 0:
                break
            for task in response["tasks"]:
                try:
                    if task["object"]["id"] in object_list:
                        preprocessed_task_list.append(task)
                except KeyError as e:
                    continue

            for task_item in preprocessed_task_list:
                task_dict = Utils.industrial_generate_task_dict(
                    task_item=task_item,
                    organization='ТОО "HAS Industrial"'
                )
                self.task_list.append(task_dict)

            current_offset += 100

    def get_task_list(self):
        current_date = self.start_date
        # current_date = f"01-06-2024"
        current_offset = 0
        print(current_date)
        # for template in TaskTemplateEnum:
        #     print(f"Template name: {template.name}")
        self.fetch_planfix_tasks(
            current_date=current_date,
            current_offset=current_offset,
            get_task_list_url=self.get_task_list_url
        )
        self.has_db_session.execute(text("TRUNCATE industrial_transportation;"))
        self.has_db_session.commit()
        print("Database insertion started")
        self.has_db_session.execute(
            insert(IndustrialTransportation),
            self.task_list
        )
        self.has_db_session.commit()
        print("Script finished successfully")
