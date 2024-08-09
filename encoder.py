import wave
import numpy as np
import sys
import os

def encode_to_wav(input_file_path, output_wav_path):
    # Check if the input file exists
    if not os.path.isfile(input_file_path):
        print(f"Error: The file '{input_file_path}' does not exist.")
        return

    # Read the input file
    with open(input_file_path, 'rb') as file:
        file_data = file.read()

    # Determine the file extension
    file_extension = os.path.splitext(input_file_path)[1].lstrip('.')

    # Parameters for the sine wave
    sample_rate = 44100  # Standard CD-quality sample rate
    duration = 1  # Duration of the audible part in seconds (keep it short for testing)
    freq = 1000  # Frequency of the sine wave

    # Generate the sine wave
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    audio_data = 0.5 * np.sin(2 * np.pi * freq * t)
    audio_data = (audio_data * 32767).astype(np.int16)  # Convert to 16-bit PCM

    # Combine the file type and file data
    encoded_data = bytearray(file_extension.encode('utf-8'))
    encoded_data.append(0)  # Null byte as a separator
    encoded_data.extend(file_data)
    encoded_data.extend(audio_data.tobytes())

    # Write the WAV file
    with wave.open(output_wav_path, 'wb') as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)  # 2 bytes for 16-bit samples
        wav_file.setframerate(sample_rate)
        wav_file.writeframes(encoded_data)

    print(f'File encoded and saved as {output_wav_path}')
    print(f'Original file size: {len(file_data)} bytes')
    print(f'Encoded WAV file size: {len(encoded_data)} bytes')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python encoder.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = 'encoded_file.wav'
    encode_to_wav(input_file, output_file)
