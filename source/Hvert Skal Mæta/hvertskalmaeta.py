municipalities = {
    "Reykjavik": {"distance_reykjavik": 0, "distance_akureyri": 388},
    "Kopavogur": {"distance_reykjavik": 6, "distance_akureyri": 387},
    "Hafnarfjordur": {"distance_reykjavik": 12, "distance_akureyri": 391},
    "Reykjanesbaer": {"distance_reykjavik": 48, "distance_akureyri": 427},
    "Akureyri": {"distance_reykjavik": 388, "distance_akureyri": 0},
    "Gardabaer": {"distance_reykjavik": 9, "distance_akureyri": 389},
    "Mosfellsbaer": {"distance_reykjavik": 16, "distance_akureyri": 371},
    "Arborg": {"distance_reykjavik": 64, "distance_akureyri": 428},
    "Akranes": {"distance_reykjavik": 49, "distance_akureyri": 350},
    "Fjardabyggd": {"distance_reykjavik": 659, "distance_akureyri": 290},
    "Mulathing": {"distance_reykjavik": 603, "distance_akureyri": 216},
    "Seltjarnarnes": {"distance_reykjavik": 4, "distance_akureyri": 390}
}

def find_nearest_contest_site(municipality):
    if municipality not in municipalities:
        return "Invalid municipality"
    
    distances = municipalities[municipality]
    if distances["distance_reykjavik"] < distances["distance_akureyri"]:
        return "Reykjavik"
    else:
        return "Akureyri"

# Read input
municipality = input()

# Find and print the nearest contest site
nearest_site = find_nearest_contest_site(municipality)
print(nearest_site)