import os
import subprocess

def is_5_1_audio(file_path):
    try:
        result = subprocess.run(
            ["ffprobe", "-v", "error", "-select_streams", "a", "-show_entries", "stream=channels", "-of", "csv=p=0", file_path],
            capture_output=True, text=True
        )
        channels = result.stdout.strip()
        return channels == "6"
    except Exception as e:
        print(f"Error al procesar {file_path}: {e}")
        return False

def find_5_1_mp4_files(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(".mp4"):
                file_path = os.path.join(root, file)
                if is_5_1_audio(file_path):
                    print(f"✅ {file_path} tiene audio 5.1")
                else:
                    print(f"❌ {file_path} no tiene audio 5.1")

if __name__ == "__main__":
    network_path = r"\\192.168.1.50\salas\series"
    find_5_1_mp4_files(network_path)
