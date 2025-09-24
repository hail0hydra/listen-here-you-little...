import json
from pathlib import Path
import argparse
import subprocess


def play(link:str | None):
    """Play the given link using mpv. The command being `mpv --profile=customsize --shuffle --really-quiet --no-input-terminal link`"""
    if link:
        try:
            subprocess.run(['mpv', '--profile=customsize', '--shuffle', '--really-quiet', '--no-input-terminal', link], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Failed to play the link: {e}")
        except FileNotFoundError:
            print("mpv is not installed or not found in PATH.")
    else:
        print("No link provided to play.")


def load_json(file_path) -> dict[str, dict[str, str]]:
    """Load JSON data from a file."""
    path = Path(file_path)
    if not path.is_file():
        raise FileNotFoundError(f"No such file: '{file_path}'")
    
    with path.open('r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def get_url() -> dict[str, str] | None:
    """Get URLs from singles or playlists based on command-line arguments."""
    if args.s:
        singles = load_json('singles.json')
        return singles.get('singles', {})
    
    elif args.p:
        playlists = load_json('playlists.json')
        return playlists.get('playlists', {})

    else :
        print("No valid argument provided. Use -s for singles or -p for playlists.")
        return None


def fzf_select(links, prompt="select a playlist: ") -> str | None:
    """Presents a list of links to the user using fzf and returns the selected item."""
    input_str = "\n".join(links)
    try:
        process = subprocess.run(
            ['fzf', '--prompt', prompt],
            input=input_str,
            capture_output=True,
            text=True,
            check=True
        )
        selected_link = process.stdout.strip()
        return selected_link
    except subprocess.CalledProcessError as e:
        print(f"fzf selection failed: {e}")
        return None
    except FileNotFoundError:
        print("fzf is not installed or not found in PATH.")
        return None


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="music player")
    parser.add_argument('-s', action='store_true', help='singles')
    parser.add_argument('-p', action='store_true', help='playlists')

    args = parser.parse_args()

    if not (args.s or args.p):
        parser.print_help()
        exit(1)

    data_link = get_url()
    my_links = [i.get('url') for i in data_link]


    try:
        selected = fzf_select(my_links, prompt="select a link: ")
    except AttributeError:
        selected = None

    if selected:
        print(f"Selected link: {selected}")
    else:
        print("No link selected.")

    play(selected)
