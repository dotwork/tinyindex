

########################################################################
class Index(object):

    ####################################################################
    def __init__(self, table, *keys, **kwargs):
        self.table = table
        self.keys = keys
        self.reverse = bool(kwargs.get('reverse'))
        self.save_unindexed = bool(kwargs.get('save_unindexed'))
        self.unindexed = []

    ####################################################################
    def can_index(self, datum):
        return all(key in datum for key in self.keys)

    ####################################################################
    def all(self):
        for item in self.table.all():
            if self.can_index(item):
                yield item
            elif self.save_unindexed:
                self.unindexed.append(item)

    ####################################################################
    @property
    def keyfunc(self):
        def function(datum):
            return tuple(datum[k] for k in self.keys)
        return function

    ####################################################################
    def ranked(self):
        records = list(self.all())
        records.sort(
            key=self.keyfunc,
            reverse=self.reverse,
        )
        return records

    ####################################################################
    def __iter__(self):
        for item in self.ranked():
            yield item

    ####################################################################
    def __getitem__(self, idx):
        return self.ranked()[idx]
