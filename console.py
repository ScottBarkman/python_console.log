"""The magic begins here."""

class Console(object):
	"""This is your console object."""

    def log(self, message):
    	"""Log simple error messages. Pretty standard JavaScripting."""
        print(message)

    def error(self, message):
    	"""console.error() logging. Great for error reporting."""
        print(message)

    def warn(self, message):
    	"""Need a warning? This is the method for you."""
        print(message)

    def debug(self, message):
    	"""Looking to debug your code? console.debug('Your message') will solve all of your problems."""
        print(message)


console = Console()
