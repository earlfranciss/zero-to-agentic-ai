# Custom exception classes for API errors
class AuthenticationError(Exception):
    pass

class RateLimitError(Exception):
    pass

class APIConnectionError(Exception):
    pass

class APITimeoutError(Exception):
    pass

class APIStatusError(Exception):
    pass

# API error handler
def handle_api_error(error):
    if isinstance(error, AuthenticationError):
        print("Error: Invalid API key.")

    elif isinstance(error, RateLimitError):
        print("Error: API rate limit or quota exceeded.")

    elif isinstance(error, APIConnectionError):
        print("Error: Unable to connect to the API.")

    elif isinstance(error, APITimeoutError):
        print("Error: API request timed out.")

    elif isinstance(error, APIStatusError):
        print(f"Error: API returned status code {error.status_code}.")

    else:
        print(f"Unexpected error: {error}")


# Simulate a rate limit error
try:
    raise RateLimitError("Rate limit exceeded")

except Exception as error:
    handle_api_error(error)
