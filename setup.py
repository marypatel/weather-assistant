from setuptools import setup, find_packages

setup(
    name="weather-assistant",
    version="0.1.0",
    description="A Python CLI for fetching weather by city and getting attire/activity suggestions",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    install_requires=[
        "requests"
    ],
    entry_points={
        "console_scripts": [
            "weather-assistant = weather_assistant.cli:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires=">=3.6",
)