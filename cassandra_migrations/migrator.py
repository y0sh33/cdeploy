import os


class Migrator:
    def __init__(self, migrations_path, session):
        self.migrations_path = migrations_path
        self.session = session
        self.session.execute("""
            CREATE TABLE IF NOT EXISTS schema_migrations (type text, version int, PRIMARY KEY(type, version))
            WITH COMMENT = 'Schema migration history' AND CLUSTERING ORDER BY (version DESC)
        """)

    def run_migrations(self):
        for file_name in os.listdir(self.migrations_path):
            migration_content = self._read_migration(file_name)
            self.session.execute(migration_content)

    def _read_migration(self, file_name):
        migration_file = open(os.path.join(self.migrations_path, file_name))
        return migration_file.read()