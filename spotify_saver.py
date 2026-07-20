import subprocess


def download_spotify_mp3():
    print("Spotify to MP3 Downloader")
    content_type = (
        input("What do you want to download? (Enter 'track', 'playlist', or 'album'): ")
        .strip()
        .lower()
    )

    if content_type not in ["track", "playlist", "album"]:
        print("Invalid choice. Please enter 'track', 'playlist', or 'album'.")
        return

    spotify_url = input(f"Enter the Spotify {content_type} URL: ").strip()

    try:
        print(f"\nDownloading {content_type} as MP3...")

        subprocess.run(
            [
                "python",
                "-m",
                "spotdl",
                spotify_url,
                "--format",
                "mp3",
                "--audio",
                "youtube-music",
                "--output",
                "{title}/{artists} - {title}.{ext}",
            ],
            check=True,
        )

        print(
            f"\nDownload of {content_type} completed! "
            "You'll find it in a new folder.\n"
        )
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    download_spotify_mp3()