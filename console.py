"""The magic begins here."""
from colorama import init, Fore

init()


class Console(object):
    """This is your console object."""

    def log(self, message):
        """Log simple error messages. Pretty standard JavaScripting."""
        print(Fore.WHITE + message)

    def error(self, message):
        """console.error() logging. Great for error reporting."""
        print(Fore.RED + message)

    def warn(self, message):
        """Need a warning? This is the method for you."""
        print(Fore.YELLOW + message)

    def debug(self, message):
        """Looking to debug your code? console.debug('Your message') will solve all of your problems."""
        print(Fore.BLUE + message)


console = Console()

# Example code
# console.log('testing log')
# console.error('testing error')
# console.warn('testing warn')
# console.debug('testing debug')