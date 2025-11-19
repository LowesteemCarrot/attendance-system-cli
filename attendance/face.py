import numpy as np
import face_recognition

def encode_frame(frame):
    rgb = frame[:, :, ::-1]
    encs = face_recognition.face_encodings(rgb)
    return encs[0] if encs else None

def compare(enc1, enc2):
    return face_recognition.compare_faces([enc1], enc2)[0]

def bytes_to_enc(b):
    return np.frombuffer(b, dtype=np.float64)

def enc_to_bytes(enc):
    return enc.tobytes()
