from googleapiclient.discovery import build

# YouTube API anahtarını ekle
api_key = 'AIAPI anahtarını ekle'

# YouTube hizmetini başlat
youtube = build('youtube', 'v3', developerKey=api_key)

# Teneke Kafalar Studios kanal kimliği
channel_id = 'UCePSqJZ_0yg7aUMSJDIng3g'

# Kanalın yükleme oynatma listesinin kimliğini alalım
channel_request = youtube.channels().list(
    part='contentDetails',
    id=channel_id
)
channel_response = channel_request.execute()

# Yükleme oynatma listesinin kimliğini alalım
playlist_id = channel_response['items'][0]['contentDetails']['relatedPlaylists']['uploads']

print(f"Yükleme oynatma listesi ID'si: {playlist_id}")
