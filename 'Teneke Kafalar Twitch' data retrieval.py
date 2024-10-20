from googleapiclient.discovery import build
import pandas as pd
import isodate  # ISO 8601 formatındaki süreyi çözümlemek için gerekli

# YouTube API anahtarını ekle
api_key = 'AIzAPI anahtarını ekle'

# YouTube hizmetini başlat
youtube = build('youtube', 'v3', developerKey=api_key)

# Teneke Kafalar Studios kanalının yükleme oynatma listesinin ID'si
playlist_id = 'UUePSqJZ_0yg7aUMSJDIng3g'  # Kanalın yükleme oynatma listesi ID'si

# Tüm videoları toplamak için liste
video_data = []

# İlk isteği yapalım ve ilk sayfayı çekelim
request = youtube.playlistItems().list(
    part='snippet,contentDetails',
    playlistId=playlist_id,
    maxResults=50  # API'nin izin verdiği maksimum sonuç sayısı
)
response = request.execute()

# Tüm sayfaları çekmek için döngü
while True:
    for item in response['items']:
        video_id = item['contentDetails']['videoId']
        video_title = item['snippet']['title']
        published_at = item['snippet']['publishedAt']

        # Her videonun beğeni, yorum, izlenme sayılarını ve süreyi almak için API çağrısı
        video_request = youtube.videos().list(
            part='statistics,contentDetails',  # 'statistics' ve 'contentDetails' ekleniyor
            id=video_id
        )
        video_response = video_request.execute()

        for video in video_response['items']:
            view_count = video['statistics'].get('viewCount', '0')  # İzlenme sayısı
            like_count = video['statistics'].get('likeCount', '0')  # Beğeni sayısı
            comment_count = video['statistics'].get('commentCount', '0')  # Yorum sayısı
            duration = video['contentDetails']['duration']  # ISO 8601 formatında süre

            # Süreyi saniye cinsine dönüştürelim
            duration_seconds = isodate.parse_duration(duration).total_seconds()

            # Videoya ait bilgileri listeye ekle
            video_data.append({
                'Video Title': video_title,
                'Published At': published_at,
                'View Count': view_count,
                'Like Count': like_count,
                'Comment Count': comment_count,
                'Duration (seconds)': duration_seconds  # Saniye cinsinden süre
            })

    # Bir sonraki sayfa için nextPageToken'ı al ve devam et
    next_page_token = response.get('nextPageToken')
    if next_page_token:
        request = youtube.playlistItems().list(
            part='snippet,contentDetails',
            playlistId=playlist_id,
            maxResults=50,
            pageToken=next_page_token  # Sonraki sayfanın token'ı
        )
        response = request.execute()
    else:
        break  # Daha fazla sayfa yoksa döngüyü bitir

# Verileri DataFrame'e dönüştür
df = pd.DataFrame(video_data)

# CSV dosyasına kaydet
df.to_csv('youtube_video_data.csv', index=False)

print(f"Toplam {len(video_data)} video çekildi ve CSV dosyasına kaydedildi.")
