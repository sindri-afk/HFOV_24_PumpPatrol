class Workout:
    def __init__(self, program_id, program_name, program_description):
        self.program_id = program_id
        self.program_name = program_name
        self.program_description = program_description
    
    def to_dict(self):
        return {
            "program id": self.program_id,
            "program name": self.program_name,
            "program description": self.program_description
        }
    
    @staticmethod
    def from_dict(data):
        return Workout(data["program id"], data["program name"], data["program description"])
        