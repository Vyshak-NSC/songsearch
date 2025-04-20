# yt_song_extractor/extractor.py

from yt_dlp import YoutubeDL

def get_audio_url(query):
    ydl_opts = {
        'format': 'bestaudio/best',
        'noplaylist': True,
        'quiet': True,
        'default_search': 'ytsearch',
        'extract_flat': False,
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(query, download=False)
        if 'entries' in info:
            info = info['entries'][0]

        return {
            'title': info.get('title'),
            'webpage_url': info.get('webpage_url'),
            'stream_url': info.get('url'),
            'thumbnail_url': info.get('thumbnail'),
            'like_count': info.get('like_count'),
            'view_count': info.get('view_count'),
            'tags' : info.get('tags')
        }

result = get_audio_url('despacito')
print(result['title'])
print(result['tags'])
