from setuptools import setup

setup(
    name="url-shortener",
    version="0.1",
    py_modules=["main"],
    install_requires=["flask"],
    entry_points={
        "console_scripts": [
        "url-shortener=main:run"
        ]
    }
)

