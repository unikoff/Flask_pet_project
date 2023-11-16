from sqlalchemy import create_engine, text, insert
import config
from models import metadata_obj, users_table

engine = create_engine(
    url=config.postgresql(),
    echo=False
)


def create_tables():
    metadata_obj.create_all(engine)


def insert_data():
    with engine.connect() as conn:
        stmt = insert(users_table).values(
            [
                {"username": "rere", "password": "rwrw"}
            ]
        )
        conn.execute(stmt)
        conn.commit()


if __name__=="__main__":
    insert_data()