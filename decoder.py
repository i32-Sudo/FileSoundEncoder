import wave
import sys
import os

def decode_from_wav(input_wav_path, output_file_path):
    # Check if the input WAV file exists
    if not os.path.isfile(input_wav_path):
        print(f"Error: The file '{input_wav_path}' does not exist.")
        return

    # Read the WAV file
    with wave.open(input_wav_path, 'rb') as wav_file:
        params = wav_file.getparams()
        sample_rate = params.framerate
        sampwidth = params.sampwidth
        nframes = params.nframes
        audio_data = wav_file.readframes(nframes)

    # Extract the file type and file data
    separator_index = audio_data.find(b'\x00')
    if separator_index == -1:
        print("Error: Separator byte not found in the WAV file.")
        return

    file_extension = audio_data[:separator_index].decode('utf-8')
    file_data = audio_data[separator_index + 1:]

    # Save the extracted data to the output file
    with open(output_file_path + '.' + file_extension, 'wb') as file:
        file.write(file_data)

    print(f'File decoded and saved as {output_file_path}.{file_extension}')
    print(f'Decoded file size: {len(file_data)} bytes')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python decoder.py <input_wav>")
        sys.exit(1)

    input_wav = sys.argv[1]
    output_file = 'decoded_file'
    decode_from_wav(input_wav, output_file)
