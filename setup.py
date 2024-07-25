import setuptools 

with open("README.md", "r", encoding= "utf-8") as f:
    long_description = f.read()


__version__ ="0.0.0"

REPO_NAME = "Text-Summarization_NLP"
AUTHOR_USER_NAME = "santosh589"
SRC_REPO = "TextSummarizer"
AUTHOR_EMAIL= "santosh159@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description= "A app for text-summarization in NLP ",
    long_description=long_description,
    long_description_content = "text/markdown",
    url="https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker" : "https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir= {"":"src"},
    packages= setuptools.find_packages(where= "src")
)
