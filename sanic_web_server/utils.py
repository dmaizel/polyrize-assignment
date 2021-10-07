def normalize_json(json_list):
    return {
        json_obj["name"]: json_obj[
            [k for k in json_obj.keys() if "Val" in k][0]]
        for json_obj in json_list
    }
