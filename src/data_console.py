class DataConsole:
    data = []
    _data_sources = "csv", "database", "web"
    _source = None

    def select_source(self, source):
        if source in self._data_sources:
            self._source =