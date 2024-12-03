FILE_PATH = "/Users/sindribjarkason/Desktop/HFOV_24_PumpPatrol/MembershipPlan/membershipDB.json"

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

def write_json_file(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
