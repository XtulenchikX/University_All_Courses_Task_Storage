def StoreUserController(first_name = "Not Defiend", second_name = "Not Defiend", fathers_name = "Not Defiend", birth_date = "Not Defiend", language = "Not Defiend"):
  import json
  data = {
    "first_name": first_name,
    "second_name": second_name, 
    "fathers_name": fathers_name,
    "birth_date": birth_date,
    "language": language
  }

  json_data = json.dumps(data, ensure_ascii=False)
  return json_data