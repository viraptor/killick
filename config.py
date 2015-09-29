server = {
    'port': '5000',
    'host': '0.0.0.0'
}

# Pecan Application Configurations
app = {
    'root': 'killick.controllers.root_controller.RootController',
    'modules': ['killick'],
    # 'static_root': '%(confdir)s/public',
    # 'template_path': '%(confdir)s/${package}/templates',
    'debug': True,
    'errors': {
        '404': '/error/404',
        '__force_dict__': True
    },
}

logging = {
    "formatters": {
        "simple": {
            "format": ("%(asctime)s %(levelname)-5.5s [%(name)s][%(process)d/"
                       "%(threadName)s] %(message)s")
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
            "level": "DEBUG"
        },
    },
    "loggers": {
        "anchor": {
            "level": "DEBUG"
        },
        "wsgi": {
            "level": "INFO"
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO"
    },
}
