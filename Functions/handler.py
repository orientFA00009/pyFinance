import json
def handle_json(data,deserialize):
    #opens testFile.json and writes output of API call to file
    if deserialize == False:
        with open("testFile.json","w") as write_file:
            json.dump(data,write_file)
    #directly handles JSON and converts to python dictionary with two dictionaries,
    # one contains the time series w a dictionary for each week
    else:
        json_list = json.dumps(data)
        list1 = json.loads(json_list)
        return list1


