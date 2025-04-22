from urllib.parse import quote_plus
import os
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, text

from app.global_loader import HasGlobalExpensesLoader
from app.industrial_loader import HasIndustrialExpensesLoader


def main():
    dotenv_path = os.path.join(os.path.dirname(__file__), ".env")

    load_dotenv(
        dotenv_path=dotenv_path
    )
    HAS_DB_CONNECTION_STRING = f'postgresql+psycopg2://{os.getenv("HAS_DB_USERNAME")}:{quote_plus(os.getenv("HAS_DB_PASSWORD"))}@{os.getenv("HAS_DB_SERVER")}/{os.getenv("HAS_DB_NAME")}'

    has_db_engine = create_engine(
        HAS_DB_CONNECTION_STRING
    )

    HasSession = sessionmaker(has_db_engine)
    session_121 = HasSession()

    # has_industrial_loader = HasIndustrialExpensesLoader(
    #     session=session_121,
    #     url=os.getenv('PLANFIX_INDUSTRIAL_URL'),
    #     token=os.getenv('PLANFIX_INDUSTRIAL_BEARER_TOKEN'),
    #     start_date="01-08-2024"
    # )
    # has_industrial_loader.get_task_list()

    has_global_loader = HasGlobalExpensesLoader(
        session=session_121,
        url=os.getenv('PLANFIX_URL'),
        token=os.getenv('PLANFIX_BEARER_TOKEN'),
        start_date="01-08-2024"
    )
    has_global_loader.get_task_list()


if __name__ == '__main__':
    main()
