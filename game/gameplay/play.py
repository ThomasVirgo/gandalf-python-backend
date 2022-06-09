class Turn:
    """command should be a string of the form "55->110" or ""
    where the numbers represent the values of the
    card positions - see CardPosition enum"""

    def __init__(self, command: str) -> None:
        self.command = command
