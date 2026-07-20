import argparse
from pathlib import Path
from audio_separator.separator import Separator

MODELS = {
    "bs-roformer": "model_bs_roformer_ep_317_sdr_12.9755.ckpt",
    "mel-roformer": "vocals_mel_band_roformer.ckpt",
    "mdx23c": "MDX23C-8KFFT-InstVoc_HQ.ckpt",
    "mdx-net": "UVR-MDX-NET-Inst_HQ_4.onnx",
    "demucs": "htdemucs_ft.yaml",
}


def main():
    p = argparse.ArgumentParser(description="Vocal/instrumental separation")

    p.add_argument("input", nargs="?", help="Audio file (mp3/wav/flac...)")
    p.add_argument("-m", "--model", choices=MODELS, default="bs-roformer")
    p.add_argument("-o", "--output", default="output")

    # Here you choose what to keep
    p.add_argument(
        "-e",
        "--extract",
        choices=["both", "vocals", "instrumental"],
        default="both",
        help="Choose what to extract (default: both)",
    )
    p.add_argument(
        "--list_models",
        action="store_true",
        help="Show the list of available models",
    )

    args = p.parse_args()

    if args.list_models:
        print("Available models (-m):")
        for key, filename in MODELS.items():
            print(f" - {key} (file: {filename})")
        return

    if not args.input:
        p.error(
            "You must provide an input file. Usage: python separator_app.py song.mp3"
        )

    Path(args.output).mkdir(exist_ok=True)

    single_stem = None
    if args.extract == "vocals":
        single_stem = "vocals"
    elif args.extract == "instrumental":
        single_stem = "instrumental"

    # Pass output_single_stem to limit the output files
    separator = Separator(
        output_dir=args.output,
        output_format="wav",
        output_single_stem=single_stem,
    )
    separator.load_model(model_filename=MODELS[args.model])

    files = separator.separate(args.input)
    print(f"\nDone! Extracted ({args.extract}):")

    # Warning in case that files are empty
    if files:
        for f in files:
            print(" -", f)
    else:
        print(
            " Something went wrong... the folder may be empty. "
            "(Check whether the model supports this naming convention)"
        )


if __name__ == "__main__":
    main()