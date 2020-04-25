import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ytscm",
    version="1.0.0",
    author="Grant Wilk",
    author_email="grant@remington.pro",
    description="A simplified API for live Super Chat monitoring on YouTube.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/grantwilk/youtube-super-chat-monitor",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)