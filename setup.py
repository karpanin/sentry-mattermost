from setuptools import setup, find_packages

setup(
    name="sentry-loop",
    version='0.0.1',
    author="Roman Karpanin",
    author_email="karpanin@litres.ru",
    description=("A Sentry plugin to send alerts to Loop channel."),
    keywords="sentry loop",
    url="https://github.com/karpanin/sentry-mattermost",
    packages=find_packages(exclude=['tests']),
    entry_points={
       'sentry.plugins': [
            'loop = sentry_loop.plugin:Loop'
        ],
    },
)
