from setuptools import setup

setup(
    name="bert4rec",
    version="0.1.0",
    description="0.1.0 Initial release",
    packages=[
        "bert4rec",
        "bert4rec.dataloaders",
        "bert4rec.datasets",
        "bert4rec.models",
        "bert4rec.models.bert_modules",
        "bert4rec.models.bert_modules.attention",
        "bert4rec.models.bert_modules.embedding",
        "bert4rec.models.bert_modules.utils",
        "bert4rec.trainers"
    ],
)
