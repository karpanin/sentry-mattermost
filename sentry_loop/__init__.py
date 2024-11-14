try:
    VERSION = __import__('pkg_resources') \
        .get_distribution('sentry-loop').version
except Exception as e:
    VERSION = 'unknown'