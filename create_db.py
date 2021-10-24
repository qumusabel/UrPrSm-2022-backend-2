#!/usr/bin/env python3
import os
db_file = os.getenv("SQLITE_FILE", "")
os.system(f"mkdir -p {os.path.dirname(db_file)}")
open(db_file, "a").close()

from app.server import db
db.create_all()

