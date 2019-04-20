"""Module for storing information about Abstract class."""

class Abstract:
    """Stores information about title, content, authors and track
    of the abstract.

    """

    def __init__(self, title, content, authors, track):
        """Class constructor."""
        self.title = title
        self.content = content
        self.authors = authors
        self.track = track
        # self.speaker = speaker
        # self.contributionType = contributionType
        # self.tracks = tracks
