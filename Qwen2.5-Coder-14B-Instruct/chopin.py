def find_alternate_name(note, tonality):
    # Dictionary to map notes with their alternates
    note_alternates = {
        'A': None,
        'A#': 'Bb',
        'B': None,
        'C': None,
        'C#': 'Db',
        'D': None,
        'D#': 'Eb',
        'E': None,
        'F': None,
        'F#': 'Gb',
        'G': None,
        'G#': 'Ab'
    }
    
    # Check if the note has an alternate
    alternate = note_alternates[note]
    
    # If there's no alternate, return UNIQUE
    if alternate is None:
        return "UNIQUE"
    
    # Construct the alternate key name with tonality
    alternate_key = f"{alternate} {tonality}"
    
    # List of keys that are unique despite having an alternate note
    unique_keys = [
        'A# major', 'A# minor', 'C# major', 'D# major', 'D# minor',
        'G# major', 'G# minor'
    ]
    
    # Check if the alternate key is one of the unique keys
    if alternate_key in unique_keys:
        return "UNIQUE"
    
    # Otherwise, return the alternate key name
    return f"{alternate} {tonality}"

# Read input until EOF
case_number = 1
while True:
    try:
        line = input().strip()
        if not line:
            continue
        note, tonality = line.split()
        result = find_alternate_name(note, tonality)
        print(f"Case {case_number}: {result}")
        case_number += 1
    except EOFError:
        break
# Generator time: 49.0019 seconds