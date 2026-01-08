import logging
from rich.logging import RichHandler
from rich.console import Console
from rich.theme import Theme

# Define custom "SUCCESS" level (between INFO and WARNING)
SUCCESS_LEVEL_NUM = 25
logging.addLevelName(SUCCESS_LEVEL_NUM, "SUCCESS")

def success(self, message, *args, **kws):
    """
    Custom log level for success messages (Green).
    """
    if self.isEnabledFor(SUCCESS_LEVEL_NUM):
        self._log(SUCCESS_LEVEL_NUM, message, args, **kws)

# Monkey-patch the logging.Logger class to add the 'success' method
logging.Logger.success = success

# Define a custom theme for our console
custom_theme = Theme({
    "info": "cyan",
    "warning": "yellow",
    "error": "bold red",
    "success": "bold green",  # Rich will map the level name "SUCCESS" to this style
    "critical": "bold red reverse"
})

# Initialize Rich Console
console = Console(theme=custom_theme)

def setup_logger(name: str = "ApiScraper"):
    """
    Configures a professional logger using Rich.
    """
    # Configure the root logger to handle the custom level
    logging.basicConfig(
        level=logging.INFO,
        format="%(message)s",
        datefmt="[%X]",
        handlers=[RichHandler(console=console, rich_tracebacks=True, markup=True)]
    )
    
    logger = logging.getLogger(name)
    return logger, console

# Create global instances
logger, console = setup_logger()