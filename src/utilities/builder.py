from src.app.app import OProgram



class OProgramBuilder:
    def __init__(self):
        self._language = ""
        self._time_provider = None

    def with_language(self, language: str):
        self._language = language
        return self

    def with_time_provider(self, time_provider):
        self._time_provider = time_provider
        return self

    def build(self):
        return OProgram(self._language, time_provider=self._time_provider)