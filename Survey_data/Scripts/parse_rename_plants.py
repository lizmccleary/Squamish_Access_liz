import json
import geojson

# Load the GeoJSON data
with open('withID.geojson', 'r', encoding='utf-8') as f:
    data = geojson.load(f)

# Define the traditional Squamish name mapping based on the Latin name
squamish_names = {
    "Achillea_millefolium": {"squamish_name": "si7semáchxw"},
    "Oplopanax_horridus": {"squamish_name": "ch’átyaý"}, 
    "Rosa_Nutkana": {"squamish_name": "k_áĺk_ay"}, 
    "Rosa_gymnocarpa": {"squamish_name": "k_áĺk_ay"}, 
    "Rosa_pisocarpa": {"squamish_name": "k_áĺk_ay"}, 
    "Urtica": {"squamish_name": "ts’ex _ ts’íx _"}, 
    "Rubus_leucodermis": {"squamish_name": "ts’k_w’um ́áý"}, 
    "Vaccinium_ovalifolium": {"squamish_name": "xwíxwikw’ay/iyálk_paý"}, 
    "Vaccinium_uliginosum": {"squamish_name": "xwíxwikw’ay/iyálk_paý"}, 
    "Vaccinium_alaskaense": {"squamish_name": "xwíxwikw’ay/iyálk_paý"}, 
    "Vaccinium_myrtilloides": {"squamish_name": "xwíxwikw’ay/iyálk_paý"}, 
    "Vaccinium_oxycoccus": {"squamish_name": "k_wemchúĺs"}, 
    "Ledum_groenlandicum": {"squamish_name": "mák_wam"}, 
    "Sambucus_racemosa": {"squamish_name": "sts’iwk_’"}, 
    "Vaccinium_parvifolium": {"squamish_name": "sk_w’ek_wchsáý"}, 
    "Rubus_spectabilis": {"squamish_name": "yetwánaý"}, 
    "Amelanchier_alnifolia": {"squamish_name": "nástam ́aý"}, 
    "Amelanchier_semiintegrifolia": {"squamish_name": "nástam ́aý"}, 
    "Shepherdia_canadensis": {"squamish_name": "sx_wúsum"}, 
    "Rubus_parviflorus": {"squamish_name": "t’ákw’emaý"}, 
    "Rubus_ursinus": {"squamish_name": "sk_w’elḿxw"}, 
    "Camassia_quamash": {"squamish_name": "spánanexw"}, 
    "Typha_latifolia": {"squamish_name": "sts’á7ḵin"}, 
    "Epilobium_angustifolium": {"squamish_name": "x_ach’t"}, 
    "Allium_cernuum": {"squamish_name": "k_weláwa"}, 
    "Sagittaria_latifolia": {"squamish_name": "x_wux_wuk_w’últs"}, 
    "Asarum_caudatum": {"squamish_name": "xet’tánay"}, 
    "Fragaria_chiloensis": {"squamish_name": "schi7i7áý"}, 
    "Polypodium_glycyrrhiza": {"squamish_name": "tl’esíp"}, 
    "Pyrus_fusca": {"squamish_name": "k_we7úpaý"}, 
    # Add more mappings here
}

common_names = {
    "Achillea_millefolium": {"Common_Name": "Yarrow"},
    "Oplopanax_horridus": {"Common_Name": "Devil's Club"}, 
    "Rosa_Nutkana": {"Common_Name": "Wild Rose"}, 
    "Rosa_gymnocarpa": {"Common_Name": "Wild Rose"}, 
    "Rosa_pisocarpa": {"Common_Name": "Wild Rose"}, 
    "Urtica": {"Common_Name": "Stinging Nettle"}, 
    "Rubus_leucodermis": {"Common_Name": "Black Cap"}, 
    "Vaccinium_ovalifolium": {"Common_Name": "Blueberry"}, 
    "Vaccinium_uliginosum": {"Common_Name": "Blueberry"}, 
    "Vaccinium_alaskaense": {"Common_Name": "Blueberry"}, 
    "Vaccinium_myrtilloides": {"Common_Name": "Blueberry"}, 
    "Vaccinium_oxycoccus": {"Common_Name": "Bog Cranberry"}, 
    "Ledum_groenlandicum": {"Common_Name": "Labrador Tea"}, 
    "Sambucus_racemosa": {"Common_Name": "Red Elderberry"}, 
    "Vaccinium_parvifolium": {"Common_Name": "Red Huckleberry"}, 
    "Rubus_spectabilis": {"Common_Name": "Salmonberry"}, 
    "Amelanchier_alnifolia": {"Common_Name": "Saskatoon Berry"}, 
    "Amelanchier_semiintegrifolia": {"Common_Name": "Saskatoon Berry"}, 
    "Shepherdia_canadensis": {"Common_Name": "Soapberry"}, 
    "Rubus_parviflorus": {"Common_Name": "Thimbleberry"}, 
    "Rubus_ursinus": {"Common_Name": "Trailing Blackberry"}, 
    "Camassia_quamash": {"Common_Name": "Camas"}, 
    "Typha_latifolia": {"Common_Name": "Cat-tail"}, 
    "Epilobium_angustifolium": {"Common_Name": "Fireweed"}, 
    "Allium_cernuum": {"Common_Name": "Nodding Onion"}, 
    "Sagittaria_latifolia": {"Common_Name": "Wapato"}, 
    "Asarum_caudatum": {"Common_Name": "Western Wild Ginger"}, 
    "Fragaria_chiloensis": {"Common_Name": "Coastal Wild Strawberry"}, 
    "Polypodium_glycyrrhiza": {"Common_Name": "Licorice Fern"}, 
    "Pyrus_fusca": {"Common_Name": "Wild Crabapple"}, 
    "Tricholoma_murrillianum": {"Common_Name": "Pine Mushroom"}, 
    "Prunus_emarginata": {"Common_Name": "Bitter Cherry"}, 
    "Osmaronia_cerasiformis": {"Common_Name": "Indian Plum"}, 
    "Perideria_gairgeri": {"Common_Name": "Wild Carrot"}, 
    "Lomatium_nudicaule": {"Common_Name": "Indian Consumption Plant"}, 
    "Triglochin_maritimum": {"Common_Name": "Arrow-Grass"}, 
    "Pinus_monticola": {"Common_Name": "White Pine"}, 
    "Echinodontium_tinctorium": {"Common_Name": "Indian Paint Fungus"}, 
    "Solidago_Canadensi": {"Common_Name": "Golden Rod"}, 
    "Fragaria_vesca": {"Common_Name": "Woodland Strawberry"}, 
    "Sambucus_canadensis": {"Common_Name": "Common Elderberry"}, 
    "Arbutus_menziesii": {"Common_Name": "Arbutus"}, 
    "Vaccinium_membranaceum": {"Common_Name": "Mountain Bilberry"},
    "Rubus_idaeus": {"Common_Name": "Red Raspberry"}, 
    # Add more mappings here
}
# Update each feature with the traditional Squamish name and common name 
for feature in data['features']:
    latin_name = feature['properties']['feature_collection_name']
    
    # Check if the Latin name exists in squamish_names
    if latin_name in squamish_names:
        feature['properties']['squamish_name'] = squamish_names[latin_name]['squamish_name']
        
        # Check if the Latin name also exists in common_names
        if latin_name in common_names:
            feature['properties']['Common_Name'] = common_names[latin_name]['Common_Name']
        else:
            feature['properties']['Common_Name'] = None  # Set to None if no common name exists
    
    # If the Latin name doesn't exist in squamish_names, check if it exists in common_names
    elif latin_name in common_names:
        feature['properties']['Common_Name'] = common_names[latin_name]['Common_Name']
        feature['properties']['squamish_name'] = None  # Set to None if no Squamish name exists

    # If neither Squamish nor common name exists, set both to None
    else:
        feature['properties']['Common_Name'] = None
        feature['properties']['squamish_name'] = None


# Save the updated GeoJSON data to a separate new file
output_file = 'updated_plants.geojson'
with open(output_file, 'w', encoding='utf-8') as f:
    geojson.dump(data, f, ensure_ascii=False)

print("Traditional Squamish names added successfully.")
