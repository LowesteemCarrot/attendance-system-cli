import click
import cv2
import datetime
from attendance.db import get_db
from attendance.face import encode_frame, bytes_to_enc, compare

@click.command(name="scan")
def scan_faces():
    db = get_db()
    cur = db.cursor()

    cur.execute("SELECT id, name, face_encoding FROM students")
    data = cur.fetchall()

    known_ids = [row[0] for row in data]
    known_names = [row[1] for row in data]
    known_encodings = [bytes_to_enc(row[2]) for row in data]

    cam = cv2.VideoCapture(0)
    print("[INFO] Press 'q' to stop scanning")

    while True:
        ret, frame = cam.read()
        cv2.imshow("Scanning...", frame)

        enc = encode_frame(frame)
        if enc is not None:
            for i, stored_enc in enumerate(known_encodings):
                if compare(stored_enc, enc):
                    sid = known_ids[i]
                    nm = known_names[i]

                    sql = "INSERT INTO attendance (student_id, date) VALUES (%s, %s)"
                    cur.execute(sql, (sid, datetime.date.today()))
                    db.commit()

                    print(f"[PRESENT] {nm}")

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()
