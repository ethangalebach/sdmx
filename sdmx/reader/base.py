from abc import ABC, abstractmethod


class BaseReader(ABC):
    #: List of HTTP content types handled by the reader.
    content_types = []

    #: List of file name suffixes handled by the reader.
    suffixes = []

    @classmethod
    def detect(cls, content: bytes):
        """Detect whether the reader can handle `content`.

        Returns
        -------
        bool
            :obj:`True` if the reader can handle the content.
        """
        return False

    @abstractmethod
    def read_message(self, source, dsd=None):
        """Read message from *source*.

        Parameters
        ----------
        source : file-like
            Message content.
        dsd : DataStructureDefinition, optional
            DSD for aid in reading `source`.

        Returns
        -------
        :class:`.Message`
            An instance of a Message subclass.
        """
        pass  # pragma: no cover
