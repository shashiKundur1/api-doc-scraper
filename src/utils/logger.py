import logging
from rich.logging import RichHandler
from rich.console import Console
from rich.theme import Theme

# Define a custom theme for our console
custom_theme = Theme({
    "info": "cyan",
    "warning": "yellow",
    "error": "bold red",
    "success": "bold green"
})

# Initialize Rich Console
console = Console(theme=custom_theme)

def setup_logger(name: str = "ApiScraper"):
    """
    Configures a professional logger using Rich.
    """
    logging.basicConfig(
        level=logging.INFO,
        format="%(message)s",
        datefmt="[%X]",
        handlers=[RichHandler(console=console, rich_tracebacks=True)]
    )
    
    logger = logging.getLogger(name)
    return logger, console

# Create global instances
logger, console = setup_logger()