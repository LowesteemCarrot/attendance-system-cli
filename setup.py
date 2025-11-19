from setuptools import setup, find_packages

setup(
    name="attendance-cli",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "click",
        "opencv-python",
        "face_recognition",
        "mysql-connector-python",
        "rich"
    ],
    entry_points={
        "console_scripts": [
            "attendance=attendance.main:cli"
        ]
    }
)
