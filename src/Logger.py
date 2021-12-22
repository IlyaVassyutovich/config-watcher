import logging

def create_root_logger(verbose):
    logger = logging.getLogger("config-watcher")
    logger.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG if verbose else logging.INFO)

    formatter = logging.Formatter("%(asctime)s\t%(levelname)s\t%(name)s\t%(message)s")
    ch.setFormatter(formatter)

    logger.addHandler(ch)

    return logger
