import setuptools

with open("README.md", "r") as f:
    long_description = f.read()



__version__ = "0.0.0"

REPO_NAME = "Chicken_Disease_Classification_EndToEnd"
AUTHOR_USER_NAME = "AkashDhude"
SRC_REPO = "Chicken_Disease_Classification"
AUTHOT_EMAIL = "akashdhude02@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOT_EMAIL,
    description="A small python package for CNN app.",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}"

)