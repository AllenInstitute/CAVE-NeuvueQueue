from itertools import chain


def status_table_name(base_table, suffix="status"):
    return f"{base_table}_{suffix}"


def flatten_list(list_of_lists):
    return list(chain.from_iterable(list_of_lists))


class TaskValidationError(Exception):
    "Raised when tasks do not have all needed data"

    pass