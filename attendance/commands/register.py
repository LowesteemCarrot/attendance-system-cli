import click
import cv2
from attendance.db import get_db
from attendance.face import encode_frame, enc_to_bytes

@click.command(name="register")
@click.argument("name")
@click.argument("roll")
def register_face(name, roll):
    cam = cv2.VideoCapture(0)
    print("[INFO] Press 'q' to capture face")

    encoding = None

    while True:
        ret, frame = cam.read()
        cv2.imshow("Register Face", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            encoding = encode_frame(frame)
            if encoding is None:
                print("[ERROR] No face detected, try again.")
                continue
            break

    cam.release()
    cv2.destroyAllWindows()

    db = get_db()
    cur = db.cursor()

    sql = "INSERT INTO students (name, roll, face_encoding) VALUES (%s, %s, %s)"
    cur.execute(sql, (name, roll, enc_to_bytes(encoding)))
    db.commit()

    print(f"[OK] Registered {name}")
