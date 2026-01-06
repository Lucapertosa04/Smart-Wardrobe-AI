class UserInput:

    USAGE_TIME_OPTIONS = ["Indossato di frequente", "Indossato occasionalmente", "Indossato raramente", "Mai indossato"]
    WEAR_LEVEL_OPTIONS = ["Usurato", "Mediocre", "Buono", "Ottimo", "Nuovo"]

    def __init__(self, usage_time: str, wear_level: str, notes: str = ""):
        self.usage_time = usage_time
        self.wear_level = wear_level
        self.notes = notes

    def is_valid(self):
        if self.usage_time not in self.USAGE_TIME_OPTIONS:
            return False, f"Valore non valido per usage_time: {self.usage_time}"

        if self.wear_level not in self.WEAR_LEVEL_OPTIONS:
            return False, f"Valore non valido per wear_level: {self.wear_level}"

        return True, None

    def to_dict(self):
        return {
            "usage_time": self.usage_time,
            "wear_level": self.wear_level,
            "notes": self.notes
        }
