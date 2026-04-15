import random

class KararMerkezi:
    def __init__(self, toplam_secenek=20):
        # 1den 20 ye kadar olan seçenekeleri her seferinde karıştırıp havuz oluşturma.
        self.havuz = list(range(1, toplam_secenek + 1))
        random.shuffle(self.havuz)
        
        # sol_aday ve sag_aday havuzdan çekilen resim ve yazı olarak düşünelim.
        self.sol_aday = self.havuz.pop()
        self.sag_aday = self.havuz.pop()
        
        self.tur_sayisi = 1
        self.oyun_bitti = False
        self.sampiyon = None

    def secim_yap(self, taraf):
        
        """
        sol/sağ seçimini yapıp havuzda elaman varsa devam eden yoksa 
        kalan elemanın kazandığına karar vericez
        """
        
        if self.oyun_bitti:
            return

        if taraf == "SOL":
            # solu seçince sağ elenir sağın yerine havuzdan yeni aday gelir
            print(f"Tur {self.tur_sayisi}: {self.sol_aday} kazandı, {self.sag_aday} elendi.")
            if len(self.havuz) > 0:
                self.sag_aday = self.havuz.pop()
            else:
                self.bitir(self.sol_aday)

        elif taraf == "SAG":
            # sağı seçince sol elerin sağdaki resim sola geçer ve sağın yerine havuzdan yeni eleman gelir 
            print(f"Tur {self.tur_sayisi}: {self.sag_aday} kazandı, {self.sol_aday} elendi.")
            self.sol_aday = self.sag_aday
            if len(self.havuz) > 0:
                self.sag_aday = self.havuz.pop()
            else:
                self.bitir(self.sol_aday)
        
        self.tur_sayisi += 1

    def bitir(self, kazanan):
        self.oyun_bitti = True
        self.sampiyon = kazanan
        print(f"--- OYUN BİTTİ --- Şampiyon: {self.sampiyon}")

    def mevcut_durum(self):
        
        return {
            "sol": self.sol_aday,
            "sag": self.sag_aday,
            "bitti": self.oyun_bitti,
            "sampiyon": self.sampiyon
        }

#bu kısmı test etmek için ekledim benim sol ve sağ olarak seçmem sonucu seçimi yapıyor.
if __name__ == "__main__":
    beyin = KararMerkezi(20)
    
    while not beyin.oyun_bitti:
        durum = beyin.mevcut_durum()
        print(f"\nŞu anki Kapışma: {durum['sol']} vs {durum['sag']}")
        secim = input("Hangi taraf kazansın? (sol/sag): ").upper()
        beyin.secim_yap(secim)