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


def get_luminosite(lower_range, upper_range):
    luminosite = random.randint(lower_range, upper_range)
    return luminosite


def get_temperature(lower_range, upper_range):
    temperature = random.randint(lower_range, upper_range)
    return temperature


def get_mouvement(lower_range, upper_range):
    mouvement = random.randint(lower_range, upper_range)
    return mouvement


def record_begin(dataset):
    dataset = dataset + '{"Content": ['
    return dataset


def record_comma(dataset):
    dataset = dataset + ","
    return dataset


def record_ending(dataset):
    dataset = dataset + ']}'
    return dataset


def single_depressif_record(dataset, iteration):
    dataset += '{'
    dataset += record_number_str + str(iteration) + comma_str
    dataset += recorder_ID_str + str(iteration) + comma_str
    dataset += expected_type_str + '"depressif"' + comma_str
    dataset += data_str + '{'
    dataset += luminosite_str + str(get_luminosite(luminosite_depressif_lower,luminosite_depressif_upper)) + comma_str
    dataset += temperature_str + str(get_temperature(temperature_depressif_lower, temperature_depressif_upper)) + comma_str
    dataset += mouvement_str + str(get_mouvement(mouvement_depressif_lower, mouvement_depressif_upper))
    dataset += '}}'
    return dataset


def single_anxieux_record(dataset, iteration):
    dataset += '{'
    dataset += record_number_str + str(iteration) + comma_str
    dataset += recorder_ID_str + str(iteration) + comma_str
    dataset += expected_type_str + '"anxieux"' + comma_str
    dataset += data_str + '{'
    dataset += luminosite_str + str(get_luminosite(luminosite_anxieux_lower,luminosite_anxieux_upper)) + comma_str
    dataset += temperature_str + str(get_temperature(temperature_anxieux_lower,temperature_anxieux_upper)) + comma_str
    dataset += mouvement_str + str(get_mouvement(mouvement_anxieux_lower, mouvement_anxieux_upper))
    dataset += '}}'
    return dataset


def single_normal_record(dataset, iteration):
    dataset += '{'
    dataset += record_number_str + str(iteration) + comma_str
    dataset += recorder_ID_str + str(iteration) + comma_str
    dataset += expected_type_str + '"normal"' + comma_str
    dataset += data_str + '{'
    dataset += luminosite_str + str(get_luminosite(luminosite_normal_lower, luminosite_normal_upper)) + comma_str
    dataset += temperature_str + str(get_temperature(temperature_normal_lower, temperature_normal_upper)) + comma_str
    dataset += mouvement_str + str(get_mouvement(mouvement_normal_lower,mouvement_normal_upper))
    dataset += '}}'
    return dataset


def single_alea_record(dataset, iteration):
    dataset += '{'
    dataset += record_number_str + str(iteration) + comma_str
    dataset += recorder_ID_str + str(iteration) + comma_str
    dataset += expected_type_str + '"alea"' + comma_str
    dataset += data_str + '{'
    dataset += luminosite_str + str(get_luminosite(luminosite_alea_lower, luminosite_alea_upper)) + comma_str
    dataset += temperature_str + str(get_temperature(temperature_alea_lower, temperature_alea_upper)) + comma_str
    dataset += mouvement_str + str(get_mouvement(mouvement_alea_lower,mouvement_alea_upper))
    dataset += '}}'
    return dataset

def mixer(dataset):
    iterations = 1

    for x in range(int(nb_anxieux)):
        dataset = single_anxieux_record(dataset, iterations)
        dataset = record_comma(dataset)
        iterations += 1
    # dataset = single_anxieux_record(dataset, iterations)
    # iterations += 1

    for x in range(int(nb_normaux)):
        dataset = single_normal_record(dataset, iterations)
        dataset = record_comma(dataset)
        iterations += 1
    #dataset = single_normal_record(dataset, iterations)
    #iterations += 1

    for x in range(int(nb_depressifs)):
        dataset = single_depressif_record(dataset, iterations)
        dataset = record_comma(dataset)
        iterations += 1
    #dataset = single_depressif_record(dataset, iterations)
    # iterations += 1

    for x in range(int(nb_alea)-1):
        dataset = single_alea_record(dataset, iterations)
        dataset = record_comma(dataset)
        iterations += 1
    dataset = single_alea_record(dataset, iterations)
    iterations += 1

    return dataset




# MAIN
print("START")

#basics
records = int(input("Nombre de records : "))
print("Veuillez entrer les pourcentage des catégories de personnes, la partie restante des poucentages est aléatoire")
depressifs = int(input("Pourcentage de depressifs : "))
anxieux = int(input("pourcentage d'anxieux : "))
normaux = int(input("pourcentage de normaux  : "))
tirage_alea = 100 - (normaux + anxieux + depressifs)
print("pourcentage aléatoire " + str(tirage_alea))
nb_depressifs = records * (depressifs / 100)
print(str(nb_depressifs) + " depressifs")
nb_anxieux = records * (anxieux / 100)
print(str(nb_anxieux) + " anxieux")
nb_normaux = records * (normaux / 100)
print(str(nb_normaux) + " normaux")
nb_alea = records * (tirage_alea / 100)
print(str(nb_alea) + " tirage aleatoire")

#ranges CHANGER LES VALEURS ICI
luminosite_anxieux_lower = 100
luminosite_depressif_lower = 100
luminosite_normal_lower = 200

luminosite_anxieux_upper = 300
luminosite_depressif_upper = 300
luminosite_normal_upper = 500

temperature_anxieux_lower = 19
temperature_depressif_lower = 16
temperature_normal_lower = 19

temperature_anxieux_upper = 24
temperature_depressif_upper = 20
temperature_normal_upper = 24

mouvement_anxieux_lower = 6500
mouvement_depressif_lower = 0
mouvement_normal_lower = 5000

mouvement_anxieux_upper = 12500
mouvement_depressif_upper = 7500
mouvement_normal_upper = 10000

mouvement_alea_lower = min(mouvement_anxieux_lower, mouvement_depressif_lower, mouvement_normal_lower)
mouvement_alea_upper = max(mouvement_anxieux_upper, mouvement_depressif_upper, mouvement_normal_upper)

luminosite_alea_lower = min(luminosite_anxieux_lower, luminosite_depressif_lower, luminosite_normal_lower)
luminosite_alea_upper = max(luminosite_anxieux_upper, luminosite_depressif_upper, luminosite_normal_upper)

temperature_alea_lower = min(temperature_depressif_lower, temperature_anxieux_lower, temperature_normal_lower)
temperature_alea_upper = max(temperature_normal_upper, temperature_anxieux_upper, temperature_depressif_upper)

#core
dataset = ""
dataset = record_begin(dataset)
dataset = mixer(dataset)
dataset = record_ending(dataset)


#end
#print(dataset)
res = json.loads(dataset)
file.write(json.dumps(res, sort_keys=False, indent=4))
file.close()
print("END")
