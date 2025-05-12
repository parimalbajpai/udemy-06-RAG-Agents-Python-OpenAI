
islands = {
    'Wano': ['Road Poneglyph', 'Historical Poneglyph'],
    'Zou': ['Road Poneglyph'],
    'Alabasta': ['Historical Poneglyph']
}

def get_island_poneglyphs(island):
    return islands.get(island, [])

print("Hello dear!")
ponoglyphs_collected = []

for island, ponoglyphs in islands.items():
    print(f"On {island}, the crew collected the following Poneglyphs: {', '.join(ponoglyphs)}.")
    for p in ponoglyphs:
        if p not in ponoglyphs_collected:
            ponoglyphs_collected.append(p)

print("Total unique Poneglyph types collected:", len(ponoglyphs_collected))
print("Their names:", ponoglyphs_collected)



