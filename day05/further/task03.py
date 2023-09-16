list_in = input("Donne nous ton surnom pour la reunion:")

surnom = [
        {  
            "jour": "jeudi",
            "time": "16h12",
            "nom": "ptit-Lou"
         
         },
        {
              
            "jour": "mardi",
            "time": "13h23",
            "nom": ["bob", "ptit-lou"]
         
         
        },
        {
              
            "jour": "vendredi",
            "time": "12h12",
            "nom": "francky"
         
         
        },

    ]


for x in surnom:
    if list_in in x["nom"]:
        print(f"vous êtes bien invité ici {x['nom']} à la date {x['jour']} et à l heure {x['time']}")