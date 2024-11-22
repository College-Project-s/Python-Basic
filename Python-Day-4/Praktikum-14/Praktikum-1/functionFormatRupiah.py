def format_rupiah(angka):
    """
    Fungsi untuk memformat angka menjadi format Rupiah sederhana (tanpa "Rp" dan desimal).
    Contoh: 1500000 -> 1.500.000
    """
    try:
        return f"{angka:,.0f}".replace(',', '.')
    except ValueError:
        return "Input bukan angka yang valid"
