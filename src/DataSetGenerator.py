import json
import random

record_number_str = '"Record#": '
recorder_ID_str = '"RecorderID": '
expected_type_str = '"ExpectedType": '
data_str = '"data": '
luminosite_str = '"luminosite": '
temperature_str = '"temperature": '
mouvement_str = '"mouvement": '
comma_str = ',\n'

file = open('output.json', 'w')

#aide pour construire le json.
def record_begin(dataset):
    dataset = dataset + '{"Content": ['
    return dataset

#aide pour construire le json.
def record_comma(dataset):
    dataset = dataset + ","
    return dataset

#aide pour construire le json.
def record_ending(dataset):
    dataset = dataset + ']}'
    return dataset

#partie qui génère les valeurs aléatoires du programme.
def get_value(lower_range, upper_range):
    value = random.randint(lower_range, upper_range)
    return value

#construction json d'un record unique
def single_record(dataset, iteration, record_type_name, record_type_index, nb_units, json_object):
    dataset += '{'
    dataset += record_number_str + str(iteration) + comma_str
    dataset += recorder_ID_str + str(iteration) + comma_str
    dataset += expected_type_str + '"' + record_type_name + '"' + comma_str
    dataset += data_str + '{'
    for i in range(nb_units - 1):
        dataset += '"' + json_object["dataTypes"][record_type_index]["dataUnits"][i]["unitType"] + '" : ' + str(
            get_value(json_object["dataTypes"][record_type_index]["dataUnits"][i]["lowerLimit"],
                      json_object["dataTypes"][record_type_index]["dataUnits"][i]["upperLimit"])) + comma_str
    # sans comma pour le dernier
    dataset += '"' + json_object["dataTypes"][record_type_index]["dataUnits"][nb_units - 1]["unitType"] + '" : ' + str(
        get_value(json_object["dataTypes"][record_type_index]["dataUnits"][nb_units - 1]["lowerLimit"],
                  json_object["dataTypes"][record_type_index]["dataUnits"][nb_units - 1]["upperLimit"]))
    dataset += '}}'
    return dataset

#détermine la valeur minimum de tout le fichier de configuration pour une mesure donnée, sert pour les personnes aléatoires.
def min_value(unit_type_index: int, json_object):
    minimum = json_object["dataTypes"][0]["dataUnits"][unit_type_index]["lowerLimit"]
    for j in range(json_object["numberOfTypes"]):
        if json_object["dataTypes"][j]["dataUnits"][unit_type_index]["lowerLimit"] < minimum:
            minimum = json_object["dataTypes"][j]["dataUnits"][unit_type_index]["lowerLimit"]
    return minimum

#détermine la valeur maximum de tout le fichier de configuration pour une mesure donnée, sert pour les personnes aléatoires.
def max_value(unit_type_index: int, json_object):
    maximum = json_object["dataTypes"][0]["dataUnits"][unit_type_index]["upperLimit"]
    for j in range(json_object["numberOfTypes"]):
        if json_object["dataTypes"][j]["dataUnits"][unit_type_index]["upperLimit"] > maximum:
            maximum = json_object["dataTypes"][j]["dataUnits"][unit_type_index]["upperLimit"]
    return maximum

#construction aléatoire d'un unique record de type aléatoire
def alea_single_record(dataset, iteration, record_type_name, nb_units, json_object):
    dataset += '{'
    dataset += record_number_str + str(iteration) + comma_str
    dataset += recorder_ID_str + str(iteration) + comma_str
    dataset += expected_type_str + '"' + record_type_name + '"' + comma_str
    dataset += data_str + '{'
    for i in range(nb_units - 1):
        dataset += '"' + json_object["dataTypes"][0]["dataUnits"][i]["unitType"] + '" : ' + str(
            get_value(min_value(i, json_object), max_value(i, json_object))) + comma_str
    # sans comma pour le dernier
    dataset += '"' + json_object["dataTypes"][0]["dataUnits"][nb_units - 1]["unitType"] + '" : ' + str(
        get_value(min_value(nb_units-1, json_object),
                  max_value(nb_units-1, json_object)))
    dataset += '}}'
    return dataset

#charge le fichier de configuration
def get_input_from_file(filepath):
    fileInput = open(filepath, 'r')
    fileContent = fileInput.read()
    json_object = json.loads(fileContent)
    fileInput.close()
    return json_object

#détermine le pourcentage des records a faire en aléatoire
def calculate_nb_alea(records, json_object):
    other_records = 0
    for i in range(json_object["numberOfTypes"]):
        other_records += records * (json_object["dataTypes"][i]["percent"] / 100)
    return (records - other_records)

#genere tous les records aléatoires
def alea_records(dataset, json_object, iterations):
    for a in range(int(tirages_alea)):
        dataset = alea_single_record(dataset, iterations, "alea", json_object["numberOfUnits"], json_object)
        dataset = record_comma(dataset)
        iterations += 1
    return dataset

#construction json de tous les records
def non_mixed(dataset, json_object):
    iterations = 1
    for i in range(json_object["numberOfTypes"] - 1):
        for j in range(int(records * (json_object["dataTypes"][i]["percent"] / 100))):
            dataset = single_record(dataset, iterations, json_object["dataTypes"][i]["TypeName"], i,
                                    json_object["numberOfUnits"], json_object)
            dataset = record_comma(dataset)
            iterations += 1
    for j in range(int(records * (json_object["dataTypes"][json_object["numberOfTypes"] - 1]["percent"] / 100))):
        dataset = single_record(dataset, iterations,
                                json_object["dataTypes"][json_object["numberOfTypes"] - 1]["TypeName"],
                                json_object["numberOfTypes"] - 1, json_object["numberOfUnits"], json_object)
        dataset = record_comma(dataset)
        iterations += 1
    dataset = alea_records(dataset, json_object, iterations)
    dataset = dataset[:-1]
    return dataset

#idée abandonnée pour mélanger les records, perspective d'amélioration
def mixed(dataset):
    print("not yet supported")
    return dataset

#séparateur si il faut mélanger, abandonné
def processing(dataset, json_object):
    if json_object["scramble"] == False:
        dataset = non_mixed(dataset, json_object)
    else:
        dataset = mixed(dataset)
    return dataset


# MAIN
print("START")

inputData = get_input_from_file("settings.json")

# basics
records = int(input("Nombre de records : "))
tirages_alea: int = calculate_nb_alea(records, inputData)
print(str(tirages_alea) + " tirage aleatoire")

# core
dataset = ""
dataset = record_begin(dataset)
dataset = processing(dataset, inputData)
dataset = record_ending(dataset)

# end
# print(dataset)
res = json.loads(dataset)
file.write(json.dumps(res, sort_keys=False, indent=4))
file.close()

print("END")
