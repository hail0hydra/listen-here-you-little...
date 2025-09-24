# My Music Streamer

- This is how I listen to music on my terminal. :)

<br>

1. simple script to glue audio logic and added links together to get a working audio streamer.

2. ✅ options are as follows:
    - arg: `-s` for **singles**,
    - agr: `-p` for **playlists**

3. ⏳disown  [TODO]

4. ⏳add images to fzf links. Get the image from yt-dlp. [TODO]


## Requirements

- `yt-dlp`
- `mpv`
- `fzf`

## Usage

```bash
git clone pyStreamer
cd pyStreamer

python3 load.py -s # for singles
python3 load.py -p  # for playlists
```


## Adding Your Music
- Add you playlist or single links in `playlists.json` or `singles.json` files respectively.


## Head's Up
- I am using a profile in mpv config to save my settings. You can remove `--profile=your_profile_name` from the script if you want to use default settings.

- Here is what my profile looks like. You can customize it as you like.

```ini
# ~/.config/mpv/mpv.conf
[customsize]
geometry=800x600+100+100
fs=no
no-resume-playback
```

<br>
<br>
<br>

## Note
- This is a personal project. Feel free to modify it as you like.
- If you have any suggestions or improvements, please open an issue or a pull request.
- Enjoy your music! 🎵

<br>
<br>

> #### TL;DR - `mpv --profile=customsize --shuffle --really-quiet --no-input-terminal $1 & disown`
