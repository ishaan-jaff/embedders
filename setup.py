#!/usr/bin/env python
import os

from setuptools import setup, find_packages

this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, "README.md")) as file:
    long_description = file.read()

setup(
    name="embedders",
    version="0.0.8",
    author="Johannes Hötter",
    author_email="johannes.hoetter@kern.ai",
    description="High-level API for creating sentence and token embeddings",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/code-kern-ai/embedders",
    keywords=["kern", "machine learning", "representation learning", "python"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    package_dir={"": "."},
    packages=find_packages("."),
    install_requires=[
        "blis==0.7.7",
        "catalogue==2.0.7",
        "certifi==2021.10.8",
        "charset-normalizer==2.0.12",
        "click==8.0.4",
        "cymem==2.0.6",
        "filelock==3.6.0",
        "gensim==4.1.2",
        "huggingface-hub==0.5.1",
        "idna==3.3",
        "Jinja2==3.1.1",
        "joblib==1.1.0",
        "langcodes==3.3.0",
        "MarkupSafe==2.1.1",
        "murmurhash==1.0.7",
        "nltk==3.7",
        "numpy==1.22.3",
        "packaging==21.3",
        "pathy==0.6.1",
        "Pillow==9.1.0",
        "preshed==3.0.6",
        "pydantic==1.8.2",
        "pyparsing==3.0.8",
        "PyYAML==6.0",
        "regex==2022.4.24",
        "requests==2.27.1",
        "sacremoses==0.0.49",
        "scikit-learn==1.0.2",
        "scipy==1.8.0",
        "sentence-transformers==2.2.0",
        "sentencepiece==0.1.96",
        "six==1.16.0",
        "smart-open==5.2.1",
        "spacy==3.2.4",
        "spacy-legacy==3.0.9",
        "spacy-loggers==1.0.2",
        "srsly==2.4.3",
        "thinc==8.0.15",
        "threadpoolctl==3.1.0",
        "tokenizers==0.12.1",
        "torch==1.11.0",
        "torchvision==0.12.0",
        "tqdm==4.64.0",
        "transformers==4.18.0",
        "typer==0.4.1",
        "typing_extensions==4.2.0",
        "urllib3==1.26.9",
        "wasabi==0.9.1",
    ],
)
