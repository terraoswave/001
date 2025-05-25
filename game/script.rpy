# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the name of the character.

define s = Character("Saintess") # narasi dengan nama karakter Character("Saintess", color="#ffb200")
define b = Character("") # narasi tanpa nama
define k = Character("Knight")
# Resize transform
transform resize:
    zoom 0.4  # mengatur ukuran

init:
    $ config.default_text_cps = 20  # kecepatan huruf per detik (cps = characters per second)


# The game starts here.
label start:

    scene village
    with fade

    # Show character using corrected transform syntax
    # Show itu cuman mengganti gackground images, scene menghapus semua sprite dan gambar

    b "Ini adalah cerita mengenai seorang wanita yang kelak dipanggil seorang Saintess"

    b "Dia yatim piatu yang dibesarkan di sebuah desa terpencil."

    b "Dia sangat di sayangi oleh penduduk sekitar karena ke sopanan dan keramahan dia, dan diapun menyukai bermain dengan anak kecil"
    
    show saintess at right, resize
    with moveinright # fade itu semuanya satu layar cuk

    s "Ibadah hari ini sudah selesai, saatnya melakukan pekerjaan lainnya lagi."

    Character("Saintess", color="#ffb200") "Aku harus mencuci baju, menjemurnya dan memasak untuk siang nanti" #name beda warna

    b "Siang itu, terdapat hal yang aneh terjadi di luar desa."

    Character("Kid 1") "Kakak - kakak."

    s "Ada apa ?"

    Character("Kid 2") "Itu disana"
    Character("Kid 3") "Itu - itu"
    Character("Kid 1") "Itu ada orang - orang aneh diluar desa"

    s "Hmmm dia seorang kesatria, mungkin dia sedang membasmi monster di sekitar sini"

    show knight at left, resize 
    with moveinleft

    k "Halo selamat siang, Saya adalah kapten dari kesatria Singa putih"

    return


