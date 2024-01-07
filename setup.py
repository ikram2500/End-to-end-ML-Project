import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__= "0.0.0"

REPO_NAME="End-to-end-ML-Project-Implementation"
AUTHOR_USER_NAME = 'entbappy'
SRC_REPO = "mlProject"
AUTHOR_EMAIL = "ikram2500@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python pakage for ml app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issue",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)