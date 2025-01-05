def find_alternate_key(note, tonality):
    # List of all possible notes with their alternate names
    notes_with_alt_names = {
        "A": ["A", "Bb"],
        "A#": ["B", "Cb"],
        "B": ["C", "Db"],
        "C": ["C#", "Dbb"],
        "C#": ["D", "Ebb"],
        "D": ["D#", "Ebf"],
        "D#": ["E", "Fb"],
        "E": ["F", "Gb"],
        "F": ["F#", "Gbb"],
        "F#": ["G", "Abb"],
        "G": ["G#", "Ab"],
        "G#": ["A", "Bb"]
    }
    
    # Check if the note has an alternate name
    if note in notes_with_alt_names:
        # Find the alternate name corresponding to the given tonality
        alt_name = next((alt for alt in notes_with_alt_names[note] if alt != note), None)
        if alt_name:
            return alt_name
    else:
        return "UNIQUE"

# Read input
cases = []
while True:
    try:
        line = input().strip()
        if not line:
            break
        note, tonality = line.split()
        cases.append((note, tonality))
    except EOFError:
        break

# Process each case
case_number = 1
for note, tonality in cases:
    result = find_alternate_key(note, tonality)
    print(f"Case {case_number}: {result}")
    case_number += 1
# Generator time: 15.0224 seconds