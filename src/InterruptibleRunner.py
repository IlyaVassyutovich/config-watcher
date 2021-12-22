import signal
import logging
from typing import Callable
from time import sleep


class InterruptibleRunner:
    __cancellation_requested = False

    def __init__(self) -> None:
        self.__logger = logging.getLogger("config-watcher.signalled-runner")
        signal.signal(signal.SIGTERM, self.__mark_as_cancelled)
        self.__logger.debug(f"subscribed to \"{signal.strsignal(signal.SIGTERM)}\"")
        signal.signal(signal.SIGINT, self.__mark_as_cancelled)
        self.__logger.debug(f"subscribed to \"{signal.strsignal(signal.SIGINT)}\"")

    def __mark_as_cancelled(self, signal_number, stack_frame) -> None:
        self.__logger.info(f"got signal \"{signal.strsignal(signal_number)}\"")
        self.__cancellation_requested = True
    
    def should_continue(self) -> bool:
        return not self.__cancellation_requested
    
    def run(self, callable: Callable) -> None:
        if self.__cancellation_requested:
            self.__logger.debug("already signalled to stop, not running")
            return
        
        while not self.__cancellation_requested:
            callable()
            sleep(3)