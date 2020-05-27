# DataSetGenerator
DataSetGenerator sert à générer des données distribuées, c'est-à-dire que, l'utilisateur peut définir des paramètres de distribution du type de données qu'il souhaite obtenir. Par exemple, un utilisateur souhaite générer un jeu de données pour entraîner un algorithme sur des types de personnes. Les différents types sont : des personnes dépressives, des personnes anxieuses et des personnes "normales". L'utilisateur va alors définir les paramètres qui différencient ces types de personnes. 

Avec notre exemple, l'utilisateur choisi les trois paramètres suivants :
    
   -  la luminosité : faible pour les dépressifs et les anxieux.
    
   - le mouvement : faible pour les dépressifs et haut pour les anxieux.
   
   - la température : faible pour les dépressifs.

Ensuite, l'utilisateur va définir les proportions de personnes qu'il veut générer pour chaque catégorie. Dans notre exemple, l'utilisateur choisit 30 % pour les dépressifs, 30 % pour les anxieux et 30 % pour les normaux. Les 10 % restants sont qualifiés d'aléatoires, nous y reviendrons dans un instant.

Enfin, l'utilisateur choisit le nombre de personnes qu'il souhaite générer. Il obtient un fichier json avec des "records" pour chaque personne.

Les valeurs de ces records sont un nombre aléatoire entre une borne maximale et minimale en fonction du type de personne, les bornes sont données par l'utilisateur.

Les valeurs des 10 % aléatoires sont calculées en faisant l'écart maximum entre les différents types de personnes, cette partie des records est donc celle qui a la plus grande variation entre ces membres.

C'est avec cet exemple que le premier programme à été créé, mais avec le temps nous avons poussé la possibilité de paramétrer les données à l'extrême. 

L'utilisateur peut, par le biais d'un fichier de configuration, définir les données suivantes :
    
   - Le type de personnes à générer (anxieux, normales, dépressives, …), il n'y a pas de limites sur le nombre de types.
   
   - Le pourcentage des données que représente chaque type de personnes.
   
   - Les différentes sources (luminosité, température, mouvement, …), il n'y a pas de limites sur le nombre de sources à prendre en compte.
   
   - Les limites hautes et basse pour chaque source et pour chaque catégorie.
   
   - Le nombre de personnes à générer. (pas par le biais du fichier, mais par la ligne de commande)

## Manuel
### Informations générales
Le programme prend en entrée un fichier de configuration, le programme demande à l'utilisateur le nombre de records qu'il souhaite générer, ces records sont écris dans le fichier : output.json.

### Fichier de configuration
Le programme possède un fichier de configuration : settings.json.

```json
{
    "scramble" : false,
    "numberOfTypes": 4,
    "numberOfUnits" : 4,
    "dataTypes" : [
        {
            "TypeName": "normal",
            "percent": 25,
            "dataUnits" : [
                {
                    "unitType": "luminosite",
                    "lowerLimit" : 200,
                    "upperLimit": 500
                },
                {
                    "unitType": "temperature",
                    "lowerLimit" : 19,
                    "upperLimit": 24
                },
               ...
            ]
        },
    ...
    ]
}
```

Dans le fichier de configuration l'utilisateur va paramétrer toutes les données du programme.

Le premier bloc de données contient :
        
   - scramble : ce feature n'est pas implémenté et est donc inutile, laisser sur false.
   
   - numberOfTypes : correspond au nombre de différents types de personnes que l'on souhaite générer (anxieux, normaux, spéciaux, dépressifs), le type aléatoire n'est pas compté.

   - numberOfUnits : correspond au nombre de différents types de mesures que l'on veut générer (luminosité, mouvement, température)
   
   - dataTypes : tableau json des différents types de personnes, si numberOfType = 4 il faut 4 éléments dans ce tableau.
   
   - TypeName : nom du type de personne
   
   - percent : pourcentage du type de personnes. Si la somme des pourcentages définis dans le fichier de configuration est inférieure à 100, un type de personne spécial baptisé aléatoire est créé complétant les pourcentages manquants. Les limites des personnes aléatoires sont le maximum et le minimum possible pour une mesure donnée dans les fichier de configuration.
   
   - dataUnits : tableau json des différentes mesures pour un type de personne, toutes les unitées existantes dans le fichier de configuration doivent être présentent. Si numberOfUnits =  4 il faut 4 éléments dans ce tableau.
   
   - unitType : nom du type de mesure.
   
   - lowerLimit : limite basse pour l'unité de mesure. Sert à délimiter les bornes de la valeur aléatoire.
   
   - upperLimit : limite haute pour l'unité de mesure. Sert à délimiter les bornes de la valeur aléatoire.

Quelques informations sur le json :
Un tableau est délimité par des "[]" , les éléments d'un tableau sont délimités par des "{}" et séparés par des ",", il n'y a pas de ","  après le dernier élément d'un tableau ni le dernier champs d'un élément.

### Sortie
```json


{
    "Content": [
        {
            "Record#": 1,
            "RecorderID": 1,
            "ExpectedType": "normal",
            "data": {
                "luminosite": 350,
                "temperature": 23,
                "mouvement": 6640,
                "test": 3758
            }
        },
        {
            "Record#": 2,
            "RecorderID": 2,
            "ExpectedType": "normal",
            "data": {
                "luminosite": 297,
                "temperature": 23,
                "mouvement": 9705,
                "test": 3350
            }
        },...
    ]
}
```

En sortie on a :

- Content : le tableau json des records.

- Record# & RecorderID : ces deux valeurs sont identiques et représentent des informations qu'on trouve couramment dans les fichiers json issus de nos recherches. Ici elles servent simplement à numéroter les records.

- ExpectedType : le type de personne du record, util pour tester un algorithme d'entrainement.

- data : le champs des mesures.

- luminosité, temperature, mouvement, test : les valeurs des mesures du record.