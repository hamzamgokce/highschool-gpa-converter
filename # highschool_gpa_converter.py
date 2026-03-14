# highschool_gpa_converter.py

SCALES = {
    "wes": {
        "name": "WES / NACES (Önerilen)",
        "rows": [
            (97, 100, 4.0,  "A+",  "Pekiyi (Üstün)", "Olağanüstü"),
            (93,  96, 4.0,  "A",   "Pekiyi",          "Mükemmel"),
            (90,  92, 3.7,  "A−",  "Pekiyi",          "Çok İyi"),
            (87,  89, 3.3,  "B+",  "İyi+",            "İyi+"),
            (83,  86, 3.0,  "B",   "İyi",             "İyi"),
            (80,  82, 2.7,  "B−",  "İyi",             "İyi−"),
            (77,  79, 2.3,  "C+",  "Orta+",           "Orta+"),
            (73,  76, 2.0,  "C",   "Orta",            "Orta"),
            (70,  72, 1.7,  "C−",  "Orta",            "Orta−"),
            (67,  69, 1.3,  "D+",  "Geçer+",          "Zayıf+"),
            (63,  66, 1.0,  "D",   "Geçer",           "Zayıf"),
            (60,  62, 0.7,  "D−",  "Geçer",           "Zayıf−"),
            ( 0,  59, 0.0,  "F",   "Başarısız",       "Başarısız"),
        ]
    },
    "meb": {
        "name": "MEB Standart",
        "rows": [
            (93, 100, 4.0,  "A+",  "Pekiyi (Üstün)", "Olağanüstü"),
            (85,  92, 4.0,  "A",   "Pekiyi",          "Mükemmel"),
            (80,  84, 3.7,  "A−",  "Pekiyi−",         "Çok İyi"),
            (75,  79, 3.3,  "B+",  "İyi+",            "İyi+"),
            (70,  74, 3.0,  "B",   "İyi",             "İyi"),
            (65,  69, 2.7,  "B−",  "İyi−",            "İyi−"),
            (60,  64, 2.3,  "C+",  "Orta+",           "Orta+"),
            (55,  59, 2.0,  "C",   "Orta",            "Orta"),
            (50,  54, 1.7,  "C−",  "Orta−",           "Orta−"),
            (45,  49, 1.3,  "D+",  "Geçer+",          "Zayıf+"),
            (40,  44, 1.0,  "D",   "Geçer",           "Zayıf"),
            ( 0,  39, 0.0,  "F",   "Başarısız",       "Başarısız"),
        ]
    },
    "us": {
        "name": "ABD Lise Ölçeği (Katı)",
        "rows": [
            (97, 100, 4.0,  "A+",  "Pekiyi (Üstün)", "Olağanüstü"),
            (93,  96, 4.0,  "A",   "Pekiyi",          "Mükemmel"),
            (90,  92, 3.7,  "A−",  "Pekiyi",          "Çok İyi"),
            (87,  89, 3.3,  "B+",  "İyi+",            "İyi+"),
            (83,  86, 3.0,  "B",   "İyi",             "İyi"),
            (80,  82, 2.7,  "B−",  "İyi",             "İyi−"),
            (77,  79, 2.3,  "C+",  "Orta+",           "Orta+"),
            (73,  76, 2.0,  "C",   "Orta",            "Orta"),
            (70,  72, 1.7,  "C−",  "Orta",            "Orta−"),
            (67,  69, 1.3,  "D+",  "Geçer+",          "Zayıf+"),
            (65,  66, 1.0,  "D",   "Geçer",           "Zayıf"),
            ( 0,  64, 0.0,  "F",   "Başarısız",       "Başarısız"),
        ]
    },
}

def convert(score: float, scale: str = "wes") -> dict:
    if not 0 <= score <= 100:
        return {"error": "Not 0–100 arasında olmalı."}
    if scale == "linear":
        gpa = round((score / 100) * 4.0, 2)
        return {"gpa": gpa, "us_letter": "—", "tr_letter": "—", "label": "Doğrusal hesaplama"}
    for (low, high, gpa, us_letter, tr_letter, label) in SCALES[scale]["rows"]:
        if low <= score <= high:
            return {"gpa": gpa, "us_letter": us_letter,
                    "tr_letter": tr_letter, "label": label}
    return {"error": "Eşleşme bulunamadı."}

def print_table(scale: str):
    print(f"\n{'─'*58}")
    print(f"  {SCALES[scale]['name']} — Tam Dönüşüm Tablosu")
    print(f"{'─'*58}")
    print(f"  {'Aralık':<10} {'TR Harf':<18} {'ABD':<5} {'GPA':<6} Açıklama")
    print(f"{'─'*58}")
    for (low, high, gpa, us_letter, tr_letter, label) in SCALES[scale]["rows"]:
        aralık = f"{low}–{high}" if low != high else str(low)
        print(f"  {aralık:<10} {tr_letter:<18} {us_letter:<5} {gpa:<6.1f} {label}")
    print(f"{'─'*58}\n")

def main():
    print("\n=== Türkiye Lise Notu → ABD GPA Dönüştürücü ===\n")
    print("Dönüşüm yöntemi:")
    print("  1 → WES / NACES       (üniversite başvurusu için önerilen)")
    print("  2 → MEB Standart      (Türk harf sistemine dayalı)")
    print("  3 → ABD Lise Ölçeği   (katı, doğrudan uygulama)")
    print("  4 → Doğrusal          (orantısal hesaplama)\n")

    choice = input("Seçim (1/2/3/4, varsayılan 1): ").strip()
    scale = {"2": "meb", "3": "us", "4": "linear"}.get(choice, "wes")

    if scale != "linear":
        print_table(scale)

    try:
        score = float(input("Lise diploma/transkript notunuz: "))
    except ValueError:
        print("Geçersiz giriş!")
        return

    result = convert(score, scale)
    if "error" in result:
        print(result["error"])
        return

    print(f"\n── Sonuç ──────────────────────────")
    print(f"  GPA (4.0 ölçeği) : {result['gpa']:.2f}")
    print(f"  ABD Harf Notu    : {result['us_letter']}")
    print(f"  Türk Karşılığı   : {result['tr_letter']}")
    print(f"  Açıklama         : {result['label']}")
    print(f"───────────────────────────────────\n")

if __name__ == "__main__":
    main()