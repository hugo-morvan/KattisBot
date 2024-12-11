def decrypt_drm_message(drm_message):
    def rotate_string(s, n):
        return ''.join(chr((ord(c) - ord('A') + n) % 26 + ord('A')) for c in s)

    def get_rotation_value(s):
        return sum(ord(c) - ord('A') for c in s)

    # Step 1: Divide the message in half
    half_length = len(drm_message) // 2
    half1 = drm_message[:half_length]
    half2 = drm_message[half_length:]

    # Step 2: Rotate each half
    rotated_half1 = rotate_string(half1, get_rotation_value(half1))
    rotated_half2 = rotate_string(half2, get_rotation_value(half2))

    # Step 3: Merge the rotated halves
    merged_message = ''.join(
        rotate_char(rotated_half1[i], rotated_half2[i]) for i in range(len(rotated_half1))
    )

    return merged_message

def rotate_char(char1, char2):
    return chr((ord(char1) - ord('A') + ord(char2) - ord('A')) % 26 + ord('A'))

# Read input
drm_message = input()

# Decrypt the DRM message
decrypted_message = decrypt_drm_message(drm_message)

# Print the output
print(decrypted_message)