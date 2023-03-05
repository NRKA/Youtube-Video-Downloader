from pytube import Stream
from pytube import YouTube
from tqdm import tqdm


def progress_callback(stream: Stream, data_chunk: bytes, bytes_remaining: int) -> None:
    pbar.update(len(data_chunk))

if __name__ == '__main__':
    url = input("Enter URL please! ")
    print("Downloading is started.")

    yt = YouTube(url, on_progress_callback=progress_callback)
    stream = yt.streams.get_highest_resolution()

    print(f"Downloading video '{stream.default_filename}' from Youtube")
    pbar = tqdm(total=stream.filesize, unit="bytes")
    path = stream.download()
    pbar.close()
    print(f"Saved video to {path}")
