# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the name of the character.

define s = Character("Saintess") # narasi dengan nama karakter Character("Saintess", color="#ffb200")
define b = Character("") # narasi tanpa nama
define k = Character("Knight")
define m = Character("Mysterious Person 1")

init python:
    def screen_shake():
        renpy.with_statement(None)
        renpy.scene()
        renpy.show("village", at_list=[shake])
        renpy.pause(0.3)
        renpy.show("village")

transform shake:
    linear 0.05 xoffset -15
    linear 0.05 xoffset 15
    linear 0.05 xoffset -10
    linear 0.05 xoffset 10
    linear 0.05 xoffset 0


# Resize transform
transform resize:
    zoom 0.4  # mengatur ukuran


transform scale_background:
    zoom 0.9
    xalign 0.5
    yalign 0.5  
    #zoom 0.75  # ubah ke ukuran proporsional

init:
    $ config.default_text_cps = 20  # kecepatan huruf per detik (cps = characters per second)



# The game starts here.
label start:

    scene village at scale_background
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

    s "Iya, ada yang bisa di bantu ?"

    k "Apakah kalian melihat ada hal - hal yang aneh di sekitar sini ?"
    
    s "Hal - hal aneh seperti apa memangnya?"

    k "Jika tidak tahu tidak apa, monster di sekitar sini terlihat aneh, jadi berhati - hatilah"

    s "Baiklah pak, tolong berhati - hatilah juga"

    scene plain monster at scale_background
    with fade


    b "Setelah itu para kesatria pergi dari desa, sementara itu di tempat lain ..."

    m "Apakah itu sudah bisa digunakan ?"

    Character("Mysterious Person 2") "Haduh... saat ini masih belum bisa boss"

    Character("Boss ?") "Cepat segera kerjakan, kita masih butuh banyak monster untuk menyerang Ibu kota"

    Character("Mysterious Person 2") "Siap Boss"

    Character("Boss ?") "Untuk sekarang, mari kita mempersiapkan diri untuk menyerang desa terdekat dulu"

    scene village at scale_background
    with fade

    show saintess at right, resize
    with moveinright

    s "Huh - Huh...."

    s "Melelahkan..."

    s "\"Hari ini sungguh melelahkan, aku harap tidak ada masalah yang akan datang.\""

    $ screen_shake()

    b "Br......."

    return


