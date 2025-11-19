import click
from attendance.db import get_db

@click.command(name="export")
def export_attendance():
    db = get_db()
    cur = db.cursor()

    cur.execute("""
        SELECT s.name, a.date
        FROM attendance a
        JOIN students s ON s.id = a.student_id
    """)

    rows = cur.fetchall()

    with open("attendance_export.csv", "w") as f:
        f.write("name,date\n")
        for name, date in rows:
            f.write(f"{name},{date}\n")

    print("[OK] Exported to attendance_export.csv")
