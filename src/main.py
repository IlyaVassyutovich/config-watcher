from Arguments import create_parser
from Logger import create_root_logger
from InterruptibleRunner import InterruptibleRunner
from ConfigWatcher import ConfigWatcher
from time import sleep


def main():
    args = create_parser().parse_args()
    logger = create_root_logger(args.verbose)


    logger.debug("application starting")
    runner = InterruptibleRunner()
    config_watcher = ConfigWatcher(args.running_config, args.controlled_config)

    logger.info("application started")

    runner.run(
        lambda: config_watcher.try_sync_configs())

    logger.info("application stopped")


if __name__ == "__main__":
    main()