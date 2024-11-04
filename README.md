# TenekeKafalarTwitch-YoutubeChannel-Analysis

Bu proje, **'Teneke Kafalar Twitch' YouTube Kanalı** için veri çekme, düzenleme ve analiz süreçlerini içerir. Projede kanalın izlenme, beğeni ve yorum verileri analiz edilerek çeşitli içgörüler elde edilmiştir.

## Proje Süreci
1. **Veri Çekme**: `to get playlist id.py` ile kanalın video oynatma listesi (playlist) ID'si bulunur ve `'Teneke Kafalar Twitch' data retrieval.py` ile YouTube API kullanarak videolara ait veriler çekilerek **Teneke_Kafalar_Twitch.csv** dosyasına kaydedilir.
2. **Veri Düzenleme**: Çekilen veriler Excel'de temizlenir ve analiz için hazırlanır.
3. **Analiz ve Görselleştirme**: Veriler Power BI'da analiz edilir ve görselleştirilir (**'Teneke Kafalar Twitch' Youtube Channel analysis.pbix** dosyasında).

## Kullanılan Teknolojiler
- **Python**: Veri çekme işlemi ve veri düzenleme için.
- **YouTube API**: Kanal verilerini almak için.
- **Power BI**: Verileri analiz etmek ve görselleştirmek için.
- **Excel**: Verileri düzenlemek için.
- **GitHub**: Proje dosyalarının ve kodlarının yönetimi için.

## Elde Edilen Sonuçlar
- **Ay ve Yıla Göre İzlenme Eğilimleri**: Kanalın yıllık ve aylık izlenme değişimleri analiz edilerek izleyici ilgisinin zaman içindeki değişimleri incelenmiştir.
- **Oyunlara Göre İzlenme**: Yayınlanan oyunlara göre izlenme sayıları karşılaştırılmış, izleyicinin hangi oyunlara daha fazla ilgi gösterdiği belirlenmiştir.
- **Haftanın Günlerine Göre İzlenme**: İzlenme sayılarının haftanın günlerine göre dağılımı analiz edilerek izleyici alışkanlıkları hakkında fikir edinilmiştir.
- **Video Türü Dağılımı**: Shorts ve standart videoların izlenme performansları karşılaştırılmıştır.

Bu analiz, kanalın içerik stratejisi ve izleyici etkileşimini geliştirmeye yönelik faydalı içgörüler sağlamaktadır.

---

# TenekeKafalarTwitch-YoutubeChannel-Analysis

This project provides a data collection, processing, and analysis process for the **'Teneke Kafalar Twitch' YouTube Channel**. The project analyzes the channel's views, likes, and comments data to obtain various insights.

## Project Workflow
1. **Data Collection**: The `to get playlist id.py` script is used to find the channel's playlist ID. Then, `'Teneke Kafalar Twitch' data retrieval.py` retrieves video data using YouTube API and saves it into the **Teneke_Kafalar_Twitch.csv** file.
2. **Data Cleaning**: The collected data is cleaned and organized in Excel to prepare it for analysis.
3. **Analysis and Visualization**: The data is analyzed and visualized in Power BI (**'Teneke Kafalar Twitch' Youtube Channel analysis.pbix** file).

## Technologies Used
- **Python**: For data collection and initial data handling.
- **YouTube API**: For retrieving data from the channel.
- **Power BI**: For data analysis and visualization.
- **Excel**: For data cleaning and organization.
- **GitHub**: For managing project files and code.

## Key Insights
- **Monthly and Yearly View Trends**: Analyzes the changes in viewer interest over time based on monthly and yearly view counts.
- **View Counts by Game**: Compares view counts based on games published to identify which games attract more interest.
- **View Counts by Day of the Week**: Analyzes view patterns by the day of the week to understand viewer habits.
- **Distribution by Video Type**: Compares the performance of Shorts and standard videos in terms of views.

This analysis provides valuable insights into optimizing content strategy and enhancing audience engagement for the channel.

![Teneke Kafalar Analizi Görseli](https://github.com/bugrahansimsek/TenekeKafalarTwitch-YoutubeChannel-Analysis/blob/main/TenekeKafalarTwitch.gif)
