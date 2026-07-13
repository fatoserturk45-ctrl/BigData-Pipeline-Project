import pandas as pd
import matplotlib.pyplot as plt
import os

def main():
    csv_path = "data/olist_orders_dataset.csv"
    
    if not os.path.exists(csv_path):
        print("HATA: olist_orders_dataset.csv dosyası 'data' klasöründe bulunamadı!")
        return

    print("Veriler okunuyor ve grafik hazırlanıyor...")
    df = pd.read_csv(csv_path)
    
    status_counts = df['order_status'].value_counts()
    
    plt.figure(figsize=(10, 6))
    status_counts.plot(kind='bar', color='skyblue', edgecolor='black')
    
    plt.title('Olist Sipariş Durumları Dağılımı (Order Status Counts)', fontsize=14, fontweight='bold')
    plt.xlabel('Sipariş Durumu', fontsize=12)
    plt.ylabel('Sipariş Sayısı', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    plt.tight_layout()
    
    print("Grafik başarıyla oluşturuldu! 'grafik.png' dosyasına kaydedildi.")
    plt.savefig("grafik.png")
    plt.close()
if __name__ == "__main__":
    main()

