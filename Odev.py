class Calisan:
    tcKimlikNo = ""
    ad = ""
    soyAd = ""
    yas = 0
    calismaSaatleri = 0
    maas = 0

    def __init__(self, tcKimlikNo, ad, soyAd, yas, calismaSaatleri, maas):
        if len(tcKimlikNo) != 11:
            raise AttributeError("tc kimlik no 11 haneli olmalıdır")
        self.tcKimlikNo = tcKimlikNo
        self.ad = ad
        self.soyAd = soyAd
        self.calismaSaatleri = calismaSaatleri
        self.maas = maas

        if 18 <= yas <= 100:
            self.yas = yas
        else:
            raise AttributeError("yaş aralığı 18 ile 100 arası olmalıdır.")

    def vergiHesapla(self):
        if self.maas < 8000:
            return self.maas * 0.12
        else:
            return self.maas * 0.18

    def sonDurumMaas(self):
        return self.maas - self.vergiHesapla()

    def goster(self):
        print("\ntc no: " + str(self.tcKimlikNo) + "\nisim: " + self.ad + \
              "\nsoy isim: " + self.soyAd + "\nyaş: " + str(self.yas) + \
              "\nmaas: " + str(self.maas) + "\ncalışma saatleri:" + str(self.calismaSaatleri) + \
              "\n------------------------------")

class PartTimeCalisan(Calisan):
    saatlikUcret = 0
    def __init__(self, tcKimlikNo, ad, soyAd, yas, calismaSaatleri, saatlikUcret):
        super().__init__(tcKimlikNo, ad, soyAd, yas, calismaSaatleri, saatlikUcret)
        self.saatlikUcret = saatlikUcret

    def sonDurumMaas(self):
        return self.saatlikUcret * self.calismaSaatleri * 5 #buradaki 5 haftalik calisma saatini belirtmektedir

    def goster(self):
        print("\ntc no: " + str(self.tcKimlikNo) + "\nisim: " + self.ad + \
              "\nsoy isim: " + self.soyAd + "\nyaş: " + str(self.yas) + \
              "\ncalışma saatleri:" + str(self.calismaSaatleri) + \
              "\nsaatlik ücret " + str(self.saatlikUcret) + "\n------------------------------")

class FullTimeCalisan(Calisan):
    def __init__(self, tcKimlikNo, ad, soyAd, yas, maas):
        super().__init__(tcKimlikNo, ad, soyAd, yas, "full time calısan", maas)

    def sonDurumMaas(self):
        return super().sonDurumMaas() - self.maas * 0.08

    def goster(self):
        print("\ntc no: " + str(self.tcKimlikNo) + "\nisim: " + self.ad + \
              "\nsoy isim: " + self.soyAd + "\nyaş: " + str(self.yas) + \
              "\ncalışma saatleri:" + str(self.calismaSaatleri) + \
              "\n------------------------------")

calisan = Calisan("15592189460", "faruk", "kornaz", 22, 8, 20_000)
partTimer = PartTimeCalisan("15610188864", "sevde", "yıldız", 20, 8, 200)
fulTimer = FullTimeCalisan("12345678910", "mehmet", "çelebi", 30, 20_000)

calisan.goster()
partTimer.goster()
fulTimer.goster()

print("\n")
print("Çalışa maaş: " + str(calisan.sonDurumMaas()))
print("part time çalışan maaş: " + str(partTimer.sonDurumMaas()))
print("full time calısan son durum maaş: " + str(fulTimer.sonDurumMaas()))
