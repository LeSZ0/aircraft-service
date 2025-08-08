class AircraftNotFoundException(Exception):
    def __init__(self) -> None:
        self.message = 'Aircraft was not found.'
        self.status_code = 404
        super().__init__(self.message)

    def __str__(self) -> str:
        return self.message


class AircraftUnknownError(Exception):
    def __init__(self) -> None:
        self.message = 'An unknown error occurred while fetching aircraft data'
        self.status_code = 500
        super().__init__(self.message)

    def __str__(self) -> str:
        return self.message
