from setuptools import setup

setup(
    name="python-sdk-example",
    version="0.1",
    description="The dispatch model loader - lambda part.",
    url="https://github.com/garethrylance/python-sdk-example",
    author="Gareth Rylance",
    author_email="gareth@rylance.me.uk",
    packages=["example-sdk"],
    install_requires=[
        "pandas",
    ],
    zip_safe=False,
    entry_points={"console_scripts": [""]},
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    extras_require={
        "development": [
            "flake8",
            "black",
            "pytest",
            "snapshottest",
        ]
    },
)