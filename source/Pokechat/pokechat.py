def decode_message(S, pokemon_ids):
    # Create a dictionary to map each Pokémon ID to its corresponding character
    id_to_char = {int(id): char for char, id in zip(S, range(1, len(S) + 1))}
    
    # Decode the message by mapping Pokémon IDs to characters
    message = ''.join([id_to_char[int(id)] for id in pokemon_ids])
    
    return message

# Read input
S = input()
pokemon_ids = input()

# Decode the message
message = decode_message(S, pokemon_ids)

# Print the decoded message
print(message)