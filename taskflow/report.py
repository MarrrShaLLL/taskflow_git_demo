def count_done(tasks):
    return sum(1 for task in tasks if task.get("done") is True)
