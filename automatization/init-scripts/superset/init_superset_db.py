#!/usr/bin/env python3
import os
from superset import create_app, db


def main():
    app = create_app()

    with app.app_context():
        from superset.models.core import Database
        from superset.connectors.sqla.models import SqlaTable
        from superset.models.slice import Slice
        from superset.models.dashboard import Dashboard

        session = db.session

        # --- Añadir ClickHouse como BD ---
        uri = (
            f"clickhouse+http://"
            f"{os.environ['CH_USER']}:{os.environ['CH_PASSWORD']}@"
            f"{os.environ['CH_HOST']}:{os.environ['DATABASE_PORT']}/"
            f"{os.environ['CH_DATABASE']}"
        )

        db_name = "clickhouse"
        database = session.query(Database).filter_by(database_name=db_name).first()
        if not database:
            database = Database(database_name=db_name, sqlalchemy_uri=uri)
            session.add(database)
            session.commit()
            print("[OK] ClickHouse database added to Superset metadata")
        else:
            print("[INFO] ClickHouse database already registered")

        # --- Configuración de roles y usuarios ---
        sm = app.appbuilder.sm
        ROLE_PERMISSIONS = {
            'EmbedDashboard': [
                ('can_read', 'Dashboard'),
                ('can_read', 'Chart'),
                ('can_read', 'DashboardModelView'),
                ('can_read', 'DashboardModelView'),
            ],
            'DashboardAdmin': [
                ('all_dashboard_access', 'all_dashboard_access'),
                ('all_datasource_access', 'all_datasource_access'),
                ('all_database_access', 'all_database_access'),
                ('can_read', 'Database'),
                ('can_read', 'Dataset'),
                ('can_csv_upload', 'Database'),
                ('can_sql_json', 'SQLLab'),
            ],
            'SQL_User': [
                ('can_execute_sql_query', 'SQLLab'),
                ('can_get_results', 'SQLLab'),
                ('can_export_csv', 'SQLLab'),
                ('all_query_access', 'all_query_access'),
                ('all_database_access', 'all_database_access'),
            ],
        }

        for role_name, perms in ROLE_PERMISSIONS.items():
            role = sm.find_role(role_name) or sm.add_role(role_name)
            for perm_name, view_name in perms:
                pv = sm.find_permission_view_menu(permission_name=perm_name, view_menu_name=view_name)
                if pv:
                    sm.add_permission_role(role, pv)
            print(f"[OK] Role '{role_name}' configured")

        def ensure_user(username, first, last, email, role_name, password):
            user = sm.find_user(username=username)
            role = sm.find_role(role_name)
            if not user and role:
                sm.add_user(
                    username=username,
                    first_name=first,
                    last_name=last,
                    email=email,
                    role=role,
                    password=password
                )
                print(f"[OK] User '{username}' created with role '{role_name}'")
            else:
                print(f"[INFO] User '{username}' already exists or role not found")

        ensure_user('dashboard_admin', 'Dash', 'Admin', 'dash_admin@example.com', 'DashboardAdmin', 'dashadmin_pass')
        ensure_user('embed', 'Dash', 'Embed', 'embed@example.com', 'EmbedDashboard', 'embed')
        ensure_user('sql_user', 'SQL', 'User', 'sql_user@example.com', 'SQL_User', 'sqluser_pass')


if __name__ == "__main__":
    main()
