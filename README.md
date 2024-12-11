## Migrations

-   To setup migrations run `alembic init migrations`. We ony this command once
-   Modify alembic.ini `sqlalchemy.url` to the required db i.e test.db
-   Modify env.py inside migrations folder and import base model from models file

-   To create a migration `alembic revision --autogenerate -m "message"`

-   To apply the generate the generate migration, run `alembic upgrade head`
