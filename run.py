import sys
from pathlib import Path

# Menambahkan direktori utama ke PYTHONPATH
sys.path.append(str(Path(__file__).resolve().parent))

from app import create_app, db

app = create_app()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Membuat tabel jika belum ada
    app.run(debug=True)
