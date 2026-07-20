import argparse
from pathlib import Path
from pydub import AudioSegment


def convert_wav_to_mp3(input_path: Path, output_dir: Path, bitrate: str):
    output_dir.mkdir(exist_ok=True)
    output_file = output_dir / f"{input_path.stem}.mp3"

    audio = AudioSegment.from_wav(input_path)
    audio.export(output_file, format="mp3", bitrate=bitrate)

    print(f"Converted: {input_path.name} -> {output_file}")


def main():
    p = argparse.ArgumentParser(description="WAV to MP3 converter")
    p.add_argument("input", help="WAV file or folder with WAV files")
    p.add_argument("-o", "--output", default="converted", help="Output folder")
    p.add_argument(
        "-b",
        "--bitrate",
        default="320k",
        choices=["128k", "192k", "256k", "320k"],
        help="MP3 bitrate (default: 320k)",
    )

    args = p.parse_args()
    input_path = Path(args.input)
    output_dir = Path(args.output)

    if input_path.is_file():
        if input_path.suffix.lower() != ".wav":
            p.error("Input file must be a .wav file")
        convert_wav_to_mp3(input_path, output_dir, args.bitrate)
    elif input_path.is_dir():
        wav_files = list(input_path.glob("*.wav"))
        if not wav_files:
            print("No WAV files found in the folder.")
            return
        for wav in wav_files:
            convert_wav_to_mp3(wav, output_dir, args.bitrate)
        print(f"\nDone! Converted {len(wav_files)} file(s).")
    else:
        p.error(f"Path not found: {args.input}")


if __name__ == "__main__":
    main()