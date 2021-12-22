import logging
from pathlib import Path
import logging

class ConfigWatcher:
    def __init__(self, running_config_path: str, controlled_config_path) -> None:
        self.__logger = logging.getLogger("config-watcher.config-watcher")
        self.__running_config_path = running_config_path
        self.__controlled_config_path = controlled_config_path

        self.__logger.debug(f"intialized watcher with running config path: {self.__running_config_path}")
        self.__logger.debug(f"intialized watcher with controlled config path: {self.__controlled_config_path}")
        self.__initialize_core()
    
    def __initialize_core(self):
        Path(self.__controlled_config_path).touch(exist_ok=True)
        self.__logger.debug("touched controlled config")
    
    def try_sync_configs(self):
        running_config = Path(self.__running_config_path).read_text()
        controlled_config = Path(self.__controlled_config_path).read_text()

        if controlled_config != running_config:
            Path(self.__controlled_config_path).write_text(running_config)
            self.__logger.info(f"updated controlled config ({len(running_config)} >> {len(controlled_config)})")

