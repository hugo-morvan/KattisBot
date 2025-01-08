def find_alternate_key():
    # Define the mapping of keys to their alternate names
    key_mapping = {
        "A#": "Bb", "Bb": "A#", "C#": "Db", "Db": "C#", "D#": "Eb",
        "Eb": "D#", "F#": "Gb", "Gb": "F#", "G#": "Ab", "Ab": "G#"
    }

    # Define the set of keys with unique names
    unique_keys = {
        ("A", "major"), ("A#", "minor"), ("Bb", "major"),
        ("C", "major"), ("C#", "minor"), ("D", "major"),
        ("D#", "minor"), ("E", "major"), ("F", "major"),
        ("F#", "minor"), ("G", "major"), ("G#", "minor")
    }

    case_number = 1
    while True:
        try:
            line = input().strip()
            if not line:
                break

            note, tonality = line.split()

            # Check if the key is unique
            if (note, tonality) in unique_keys:
                print(f"Case {case_number}: UNIQUE")
            else:
                alternate_note = key_mapping.get(note)
                if alternate_note:
                    print(f"Case {case_number}: {alternate_note}{tonality}")
                else:
                    print(f"Case {case_number}: {note}{tonality}")

            case_number += 1
        except EOFError:
            break

find_alternate_key()
# Generator time: 10.6808 seconds