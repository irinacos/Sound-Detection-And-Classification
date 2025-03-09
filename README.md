# Tema: Clasificare si detectie de sunete

Am rezolvat toate cele 5 cerinte si am obtinut acuratetea de 64% pe setul de test.


## Functiile implementate:

### 1. gabor_filter(size, sigma, freq)

    Mai intai am implementat un filtru Gaussian, acesta avand efectul unui filtru 
    trece-jos atunci cand este inmultit cu un semnal de intrare. Filtrul reprezinta 
    de fapt o fereastra care parcurge intervale de valori discrete ale intrarii. 
    Acesta ofera o pondere mai mare valorilor apropiate de centru (media ferestrei)
    si o pondere mai mica celor care se indeparteaza.
    
    Comportamentul se datoreaza exponentialei: atunci cand n se apropie de medie,
    exponentiala tinde la 1. Atunci cand n se departeaza de valoarea mediei, exp 
    incepe sa scada, tinzand la 0.
    
    Filtrul Gabor muta acest raspunsul filtrului in jurul unei frecvente dorite, f0,
    prin aplicarea unei functii sinusoidale (cos, sin). Asadar, valorile apropiate 
    de f0 vor avea o "importanta" mai mare, acesta fiind un filtru trece-banda.


### 2. gabor_filters(size, fs, M) din fisierul filters_set.py

    Functia genereaza un set de M filtre Gabor, dar fiecare avand un alt f0, adica
    concentrate pe frecvente centrale diferite. 

    Am facut mai intai conversia la scala Mel a frecventelor minime si maxime (Hz) 
    care ne intereseaza. 
    Dupa aceea am impartit acest interval in M segmente si am trecut inapoi in 
    scala normala. Pentru a calcula frecventele centrale si deviatiile standard 
    necesare aplicarii filtrului Gabor, am calculat centrele si lungimile fiecarui 
    segment. In final am construit un array de filtre Gabor, fiecare concentrandu-se
    asupra unei frecvente diferite.

    In imaginile id_gabor_cos.png si id_gabor_sin.png sunt afisate componentele cos 
    si sin ale primului filtru din acest array.


### 3. gabor_spectrum(filters, fs, size) din fisierul filters_spectrum.py

    Functie primeste un set de filtre si aplica FFT asupra componentei cos a acestora. 
    Graficul rezultat, salvat in fisierul id_spectru_filtre.png, reprezinta 
    magnitudinea frecventelor pozitive.


### 4. get_features(audios, fs)
    
    Mai intai am creat un array de ferestre, acestea avand aceeasi dimeniune ca si 
    filtrele Gabor obtinute mai devreme. Am impartit semnalul in F intervale de cate K 
    esantioane, astfel incat o fereastra sa aiba capatele la o distanta de 12 ms fata 
    de ferestrele vecine.
    
    Pentru fiecare fereastra am aplicat toate cele M filtre Gabor, folosing operatia de 
    filtrare liniara, considerand ferestrele din semnalul audio ca fiind semnale de 
    intrare.

    Dupa aplicarea filtrelor asupra tuturor ferestrelor am salvat rezultatele intr-o 
    matrice "o" de dimensiune F x M. Am aplicat modulul peste aceasta si am folosit 
    functiile numpy mean si std pentru a calcula mediile si deviatiile standard absolute 
    pentru fiecare semnal audio (in total sunt D semnale audio). Am obtinut matricea 
    feat_train de dimensiuni D x 2M (2M deoarece, pentru un singur semnal audio, am 
    concatenat mediile si deviatiile, obtinand un vector de dim. 1 x 2M).

    Am rulat codul din scheletul dat, care analizeaza cele 2M caracteristici (features) 
    ale fiecarui semnal audio si antreneaza un model de predictii.