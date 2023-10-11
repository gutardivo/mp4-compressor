import subprocess
import os

def compress_mp4(input_file, output_file, crf=23):
    """
    Compress an MP4 video using FFmpeg.

    Args:
        input_file (str): The input MP4 file to be compressed.
        output_file (str): The output compressed MP4 file.
        crf (int): Constant Rate Factor (CRF) for video quality (default: 23).
    """
    try:
        # Check if input file exists
        if not os.path.exists(input_file):
            print(f"Error: Input file '{input_file}' not found.")
            return

        # FFmpeg command for video compression
        cmd = [
            'ffmpeg',
            '-i', input_file,
            '-c:v', 'libx264',
            '-crf', str(crf),
            '-preset', 'medium',
            '-c:a', 'aac',
            '-strict', 'experimental',
            output_file
        ]

        # Execute FFmpeg command
        subprocess.run(cmd, check=True)

        print(f"Compression complete. Output saved as '{output_file}'.")

    except subprocess.CalledProcessError as e:
        print(f"Error: FFmpeg command failed with error code {e.returncode}.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    input_file = "/Users/mac/Desktop/input.mp4"  # Replace with your input MP4 file
    output_file = "/Users/mac/Desktop/output_compressed.mp4"  # Replace with the desired output file name
    crf_value = 23  # Adjust the CRF value as needed (lower values result in higher quality)

    compress_mp4(input_file, output_file, crf_value)
