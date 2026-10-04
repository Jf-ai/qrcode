"""Buat QR code SVG untuk satu atau beberapa tautan media sosial dan website.

Pasang dependensi terlebih dahulu:
    py -m pip install segno

Lalu jalankan:
    py qrcode.py

Masukkan nama platform dan URL untuk setiap QR. Tekan Enter pada nama
platform untuk selesai. File QR disimpan di folder yang sama dengan script.
"""

from pathlib import Path
import re
from urllib.parse import urlparse

import segno


def buat_qr(link: str, nama_file: str = "qr_link") -> Path:
    """Buat QR code untuk URL dan simpan sebagai file SVG di folder script."""
    link = link.strip()
    if not link:
        raise ValueError("Link tidak boleh kosong.")

    if not link.lower().startswith(("http://", "https://")):
        if "://" in link:
            raise ValueError("Gunakan link web yang diawali http:// atau https://.")
        link = f"https://{link.lstrip('/')}"

    alamat = urlparse(link)
    if (
        alamat.scheme not in {"http", "https"}
        or not alamat.hostname
        or any(character.isspace() for character in alamat.netloc)
    ):
        raise ValueError("Link tidak terbaca. Coba format wa.me/628... atau bit.ly/namalink.")

    nama_file = re.sub(r"[^A-Za-z0-9_-]+", "_", nama_file.strip()).strip("_-")
    nama_file = nama_file or "qr_link"
    output = Path(__file__).resolve().parent / f"{nama_file}.svg"

    kode = segno.make(link, error="h")
    kode.save(output, kind="svg", scale=10, border=4, dark="#111111", light="#ffffff")
    return output


def main() -> None:
    print("Buat QR untuk semua tautan yang kamu inginkan.")
    print("Contoh link: wa.me/6281234567890 atau bit.ly/namalink.")
    print("Bisa juga masukkan link lengkap dengan https://.")
    print("Tekan Enter saat diminta nama platform untuk selesai.\n")

    jumlah_berhasil = 0
    while True:
        platform = input("Nama platform (contoh: Instagram): ").strip()
        if not platform:
            break

        link = input(f"Link {platform}: ").strip()
        try:
            output = buat_qr(link, platform)
        except ValueError as error:
            print(f"Link {platform} tidak valid: {error}\n")
            continue

        print(f"QR {platform} berhasil dibuat: {output}\n")
        jumlah_berhasil += 1

    if jumlah_berhasil:
        print(f"Selesai. {jumlah_berhasil} file QR tersimpan di folder script.")
    else:
        print("Belum ada QR yang dibuat.")


if __name__ == "__main__":
    main()