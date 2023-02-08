def secToHMS(sec: int):
    """Convert second into hh:mm:ss"""
    remain = sec % 3600
    hours = (sec - remain) // 3600
    sec -= hours * 3600  # Remove the hours from the secondes

    remain = sec % 60
    minutes = (sec - remain) // 60
    sec -= minutes * 60  # Remove the minutes from the secondes

    return f"{hours}:{minutes}:{sec[0:1]}"
