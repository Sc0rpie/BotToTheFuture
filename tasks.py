import discord
import json
import functions


class Task:
    lead: object

    def __init__(self, id, name, diff, person, task, reward):
        self.id = id
        self.name = name
        self.diff = diff
        self.person = person
        self.task = task
        self.reward = reward


task_dict = {
    Task(1, "Mission objective: Vytenis", "1", 0, "Komandos atstovas turi paglostyti Vytenio galvą", 1),
    Task(2, "Mission objective: Vytenis", "1", 0, "Mystery box", 1),
    Task(3,"Mission objective: Gabrielė D.","1", 0, "Dviejų lyčių atstovai apsikeičia rūbais",1),
    Task(4,"Mission objective: Gabrielė D.","1",0,"Išvardinti 10 programavimo kalbų", 1),
    Task(5,"Mission objective: Gabrielė D.","1",0, "Laimėti kryžiukus nuliukus prieš Gabrielę",1),
    Task(6,"Mission objective: Gabrielė D.","1",0, "Konvertuoti dvejetaine arba šešioliktaine sistema parašytą skaičių į dešimtainę sistemą",1),
    Task(7,"Mission objective: Gabrielė D.","1",0, "Visa komanda turi apkabinti Gabrielę",1),
    Task(8,"Mission objective: Eglė","1",0, "Įrodykit, kad FIDI > MIDI",1),
    Task(9,"Mission objective: Eglė","1",0, "Pateikit 10 faktų kodėl MIDI > KD",1),
    Task(10,"Mission objective: Eglė","1",0, "Išvardinti tris matematikos teoremas ir jas paaiškinti",1),
    Task(11,"Mission objective: Eglė","1",0, "Visi komandos nariai 1 minutę daro grupinį apsikabinimą",1),
    Task(12,"Mission objective: Eglė","1",0, "Eglei pristatyti 3 žmones, kurie augina katinus",1),
    Task(13,"Mission objective: Vaiva","1",0, "Kiekvienam iš komandos pasibučiuoti su savo lyties žmogumi",1),
    Task(14,"Mission objective: Vaiva","1",0, "Atpasakokit visą “Back to the future” siužetą",1),
    Task(15,"Mission objective: Vaiva","1",0,"Apsukti delną nejudinant riešo",1),
    Task(16,"Mission objective: Barbora","1",0,"Nufotografuokit penkias tatuiruotes ir parodykit Barborai",1),
    Task(17,"Mission objective: Rokas","1",0,"Pataikyti popieriaus gabaliuką į šiukšlių dėžę kitam patalpos gale",1),
    Task(18,"Mission objective: Rokas","1",0,"Sudainuokit Kunigundą Rokui",1),
    Task(19,"Mission objective: Rokas","1",0,"Pasakykit juokingiausią “your mom” juokelį kurį žinai",1),
    Task(20,"Mission objective: Rokas","1",0,"Komanda turi išvardinti visus 10 Elono Musko vaikų vardus",1),
    Task(21,"Mission objective: Rokas","1",0,"Vienas komandos narys turi Rokui parodyti savo geriausią Joker impression",1),
    Task(22,"Mission objective: Rokas","1",0,"Išspręsti Rubiko kubą",1),
    Task(23,"Mission objective: Rokas","1",0,"Per nustatytą laiką, iš ant juosmens pritvirtintos dėžutės su skyle, iškratyti joje esančius kamuoliukus",1),
    Task(24,"Mission objective: Ugnė B.","1",0,"Išvardinkit 5 vardus iš nurodytos raidės per 5 sekundes",1),
    Task(25,"Mission objective: Ugnė B.","1",0,"Išvardinkit 7 katinų veisles per 15 sekundžių",1),
    Task(26,"Mission objective: Ugnė B.","1",0,"Komandai sušokti vieną just dance šokį",1),
    Task(27,"Mission objective: Ugnė M.","1",0,"Paklausti Ugnės kodėl ji atrodo tokia pikta ir bauginanti",1),
    Task(28,"Mission objective: Simona U.","1",0,"Išsiaiškinkit kiek exit ženklų yra fakultete",1),
    Task(29,"Mission objective: Aistė","1",0,"Išvardinkit šešis veikėjus iš duoto filmo",1),
    Task(30,"Mission objective: Aistė","1",0,"Bent pusė komandos turi atsistoti ant rankų (kiti gali prilaikyti)",1),
    Task(31,"Mission objective: Aistė","1",0,"Išvardinkit 15 Marvel filmų iš atminties",1),
    Task(32,"Mission objective: Aistė","1",0,"Komandos nariams susikibus už parankių į išorę, kiekvienas narys paeiliui turi ant buteliuko, kuris yra atsuktas, uždėti kamuoliuką",1),
    Task(33,"Mission objective: Akvilė","1",0,"Pasakykit ketureilį su duotu žodžiu",1),
    Task(34,"Mission objective: Danielius","1",0,"Įkalbinkit Danielių kartu pašokti Macaren'ą",1),
    Task(35,"Mission objective: Danielius","1",0,"Visa komanda iš vieno aukšto į kitą aukštą užlipti žąsele",1),
    Task(36,"Mission objective: Danielius","1",0,"Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",1),
    Task(37,"Mission objective: Danielius","1",0,"Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",1),
    Task(38,"Mission objective: Mėta","1",0,"Papasakokit anekdotą Mėtai",1),
    Task(39,"Mission objective: Mėta","1",0,"Sušokti vieną MIF šokį",1),
    Task(40,"Mission objective: Ovidijus","1",0,"Raskit Ovidijų ir pasiūlykit jam tris LINKSMAS dainas",1),
    Task(41,"Mission objective: Monika","1",0,"Prajuokinkit Moniką",1),
    Task(42,"Mission objective: Monika","1",0,"Plojimais, trepsėjimu ir pan. sukurti ritmą ir jį atlikti organizatoriui",1),
    Task(43,"Mission objective: Monika","1",0,"Nufotografuoti visų komandos narių telefonų ekranus, kuriuose rodoma, kad visi seka  VU SA MIF instagramą",1),
    Task(44,"Mission objective: Gabriekė K.","1",0,"Pasakykit du pick-up lines Gabrielei",1),
    Task(45,"Mission objective: Vygintas","1",0,"Atspėti ir Vygintui pasakyti, kas yra vyriausias MIF'o pirmakursis",1),
    Task(46,"Mission objective: Gabija L.","1",0,"Per 7 sek. išvardinkit visas skirtingas šachmatų figūrėles",1),
    Task(47,"Mission objective: Gabija L.","1",0,"Sudarykit labiausiai MIF sielą atspindintį Spotify grojaraštį ir parodyti Gabijai",1),
    Task(48,"Mission objective: Gabija A.","1",0,"Sudėlioti dėlionę, kurioje pavaizduotas kažkas susijęs su MIF",1),
    Task(49,"Mission objective: Gabija A.","1",0,"Bent pusė komandos narių turi pasidaryti naujas šukuosenas (Parodyti prieš ir po nuotraukas)",1),
    Task(50,"Mission objective: Gabija A.","1",0,"Visa komandą turi sudainuoti dainą iš filmo/filmuko Gabijai, o ji turi atspėti koks čia filmas/filmukas",1),
    Task(51,"Mission objective: bet kuris organizatorius","1",0,"Nufotografuoti Organizatorių, jam nematant ir parodyti jam",1),
    Task(52,"Mission objective: bet kuris organizatorius","1",0,"Sugalvoti kaip ir apgauti organizatorių",1),
    Task(53,"Mission objective: bet kuris organizatorius","1",0,"Visai komandai garsiai sušukti „MIDI geriau nei FIDI“",1),
    Task(54,"Mission objective: bet kuris organizatorius","1",0,"Paduok puodelį vandens organizatoriui",1),
    Task(55,"Mission objective: bet kuris organizatorius","1",0,"Surasti organizatorių kuris nerūko",1),
    Task(56,"Mission objective: bet kuris organizatorius","1",0,"Sugalvoti originalų komandos šūkį ir garsiai jį sušukti",1),
    Task(57,"Mission objective: foto į Discord","1",0,"Visai komandai nusipiešti katės ūsus ir nosytes ant veido ir įkelti nuotrauką į discord",1),
    Task(58,"Mission objective: foto į Discord","1",0,"Visai komandai nusifotografuoti su kita komanda ir nuotrauką įkelti į discord",1),
    Task(59,"Mission objective: foto į Discord","1",0,"Iš komandos narių sudėti MIDI logotipą, nufotografuoti ir įkelti į discord",1),
    Task(60,"Mission objective: foto į Discord","1",0,"Padaryti ir įkelti į discord komandos nuotrauką, kurioje kiekvienas narys veido išraiška rodo skirtingą emoji",1),
    Task(61,"Mission objective: foto į Discord","1",0,"Surasti ir nusifotografuoti prie baseino įėjimo, nuotrauką įkelti į discord",1),
    Task(62,"Mission objective: foto į Discord","1",0,"Sukurti mįslę apie katiną",1),
    Task(63,"Mission objective: Vytenis","2",0,"Parodykit Vyteniui įdomų daiktą",2),
    Task(64,"Mission objective: Vytenis","2",0,"Laimeti stalo futbolo žaidimą prieš Vytenį",2),
    Task(65,"Mission objective: Vytenis","2",0,"Komandiškai išbūti kėdute 2 minutes",2),
    Task(66,"Mission objective: Gabrielė D.","2",0,"Šarados - trys žodžiai iš Gabrielės",2),
    Task(67,"Mission objective: Eglė","2",0,"Eglei pristatykit 4 žmones su tokiais pačiais vardais",2),
    Task(68,"Mission objective: Eglė","2",0,"Surasti studentą iš kito fakulteto ir pristatyti organizatoriui",2),
    Task(69,"Mission objective: Vaiva","2",0,"Laimėti rock paper scissors prieš Vaivą 5 kartus iš eilės",2),
    Task(70,"Mission objective: Vaiva","2",0,"Susikabinus rankomis su komandos nariais, persiųsti lanką nuo pirmo iki paskutinio žmogaus (per nustatytą laiką)",2),
    Task(71,"Mission objective: Vaiva","2",0,"Su kitos komandos atstovu/atstove sužaisti rock paper scissors, taškus gauna laimėjusi komanda",2),
    Task(72,"Mission objective: Barbora","2",0,"Visa komanda turi padaryti žmonių statulą",2),
    Task(73,"Mission objective: Barbora","2",0,"Vieni kitiems nupieškite tatuiruotes",2),
    Task(74,"Mission objective: Rokas","2",0,"Atspėkit žodį iš N raidės",2),
    Task(75,"Mission objective: Rokas","2",0,"Padarykit kuo aukštesnį bokštą iš aplinkiniu daiktų",2),
    Task(76,"Mission objective: Ugnė B.","2",0,"10 komandinių pritūpimų/atsilenkimų",2),
    Task(77,"Mission objective: Ugnė B.","2",0,"Komanda turi 90 sekundžių išstovėti ant vienos kojos užsimerkę",2),
    Task(78,"Mission objective: Simona U.","2",0,"Suskaičiuokit, kiek Didlaukio pastate yra auditorijų",2),
    Task(79,"Mission objective: Simona U.","2",0,"Nugalėti 3 kitos komandos atstovus rankos lenkime",2),
    Task(80,"Mission objective: Aistė","2",0,"Vieną iš komandos narių reikia pernešti laikant jį ore, kol jis “skrenda kaip supermenas”",2),
    Task(81,"Mission objective: Aistė","2",0,"Dainuojant dainą „Du gaideliai“, vaidinti dainos siužetą",2),
    Task(82,"Mission objective: Aistė","2",0,"Išspręsti sudoku",2),
    Task(83,"Mission objective: Danielius","2",0,"Išvardinkit dabartinio biuro narius",2),
    Task(84,"Mission objective: Danielius","2",0,"Pusė komandos turi kitą pusę pernešti iš vieno koridoriaus galo į kitą",2),
    Task(85,"Mission objective: Danielius","2",0,"Visi komandos nariai turi 45 sekundes daryti lentą",2),
    Task(86,"Mission objective: Danielius","2",0,"Visi komandos nariai turi pagauti monetą, mestą nuo tos pačios alkūnės",2),
    Task(87,"Mission objective: Danielius","2",0,"Kiekvienas komandos narys turi padaryti skirtingą jogos pozą",2),
    Task(88,"Mission objective: Mėta","2",0,"Mėtai paaiškinti kodėl DCEU > MCU",2),
    Task(89,"Mission objective: Ovidijus","2",0,"Ant lapo sukurti kodą, kuris išrašytų daugybos lentelę (iki 10x10) ir duoti patikrinti Ovidijui",2),
    Task(90,"Mission objective: Eidvilė","2",0,"Sukurkit kostiumą duota tema per 2 minutes",2),
    Task(91,"Mission objective: Eidvilė","2",0,"Nupieškit komandos nario portretą su burna",2),
    Task(92,"Mission objective: Monika","2",0,"Iš visos širdies sudainuoti 3 milijonus",2),
    Task(93,"Mission objective: Monika","2",0,"Nusifotografuoti su kiekvienu šio renginio srities vadovu ir parodyti Monikai",2),
    Task(94,"Mission objective: Lukas","2",0,"Komandai sudainuoti MIDI himną",2),
    Task(95,"Mission objective: Vygintas","2",0,"Organizatoriui išvardinti 20 pi skaitmenų po kablelio be telefono",2),
    Task(96,"Mission objective: Vygintas","2",0,"Beer pong'as be alkoholio. Kiekvienas komandos narys meta kamuoliuką lygiai vieną kartą, ir jei nors puse komandos narių pataiko, užduotis įvykdyta",2),
    Task(97,"Mission objective: Vygintas","2",0,"Perduoti kamuoliuką tik su šaukštais stovint eilute",2),
    Task(98,"Mission objective: Vygintas","2",0,"Vygintui pristatyti 10 žmonių iš skirtingų miestų",2),
    Task(99,"Mission objective: Gabija L.","2",0,"Papasakokit duoto filmo siužetą po vieną sakinį. Vienas komandos narys pasako vieną sakinį - po to kitas",2),
    Task(100,"Mission objective: Gabija A.","2",0,"Išspręsti kryžiažodį",2),
    Task(101,"Mission objective: Gabija A.","2",0,"Fakultete surasti ir nufotografuoti visos vaivorykštės spalvų daiktus",2),
    Task(102,"Mission objective: Gabija A.","2",0,"Bent pusė komandos narių turi specialiai apsiverkti, išspausti bent vieną ašarą",2),
    Task(103,"Mission objective: Ieva Marija","2",0,"Sugalvoti plana kaip pavogti dinozaurą nuo fizikų stogo ir pristatyti Ievai Marijai",2),
    Task(104,"Mission objective: Ieva Marija","2",0,"Kiekvienas komandos narys turi pasakyti Ievai Marijai, kodėl gaidelio sausainiai yra patys geriausi",2),
    Task(105,"Mission objective: foto į Discord","2",0,"Nufilmuokit kaip vienas iš komandos nariu daro a flip (galima padėti) ir įkelkit į discord",2),
    Task(106,"Mission objective: foto į Discord","2",0,"Komandos atstovui nusifotografuoti su laukiniu katinu kur nors Didlaukio teritorijoje ir įkelti nuotrauką į discord",2),
    Task(107,"Mission objective: foto į Discord","2",0,"Sukonstruoti katiną, naudojantis žmonėmis, nufotografuoti ir įkelti į discord",2),
    Task(108,"Mission objective: foto į Discord","2",0,"Komanda turi Didlaukio teritorijoje surasti ir pasidaryti nuotrauką su Miciaus mašina, ją įkelti į discord",2),
    Task(109,"Mission objective: foto į Discord","2",0,"Pastatyti piramidę iš komandos narių, nufotografuoti ir įkelti į discord",2),
    Task(110,"Mission objective: foto į Discord","2",0,"Iš grupėje turimų augintinių nuotraukų padaryti koliažą tema “Miciaus draugai” ir įkelti į discord",2),
    Task(111,"Mission objective: Vytenis","3",0,"Nugalėk Vytenį Tetris žaidime",3),
    Task(112,"Mission objective: Gabrielė D.","3",0,"Suvalgyti 4 gaidelius per minutę neužsigeriant",3),
    Task(113,"Mission objective: Gabrielė D.","3",0,"Išsiaiškinkit mystery kodą",3),
    Task(114,"Mission objective: Barbora","3",0,"Laimėkit šokių dvikovoje prieš kitą komandą",3),
    Task(115,"Mission objective: Barbora","3",0,"Kiekvienam komandos nariui reikia prisistatyti skirtinga kalba",3),
    Task(116,"Mission objective: Ugnė M.","3",0,"Išspręsti du loginius uždavinius, kol Ugnė palaiko spaudimą",3),
    Task(117,"Mission objective: Aistė","3",0,"Ant lapo, kuris yra ant kito komandos nario nugaros, kažką nupiešti ir tas komandos narys turi atspėti",3),
    Task(118,"Mission objective: Ovidijus","3",0,"Įrodykit Ovidijui kodėl assembler yra geriausia visų laikų programavimo kalba",3),
    Task(119,"Mission objective: Eidvilė","3",0,"Komandos atstovas turi apsirengti kuo daugiau sluoksnių drabužių",3),
    Task(120,"Mission objective: Gustas","3",0,"Nugalėti Gustą žaidime Typeracer",3),
    Task(121,"Mission objective: Vygintas","3",0,"Raskite ir Vygintui pristatykite 2 žmones gimusius vienos dienos skirtumu (back to back dienomis) (pvz. spalio 14 d. ir spalio 15 d.)",3),
    Task(122,"Mission objective: Gabija L.","3",0,"Parodykit magijos triuką",3),
    Task(123,"Mission objective: Gabija L.","3",0,"Raskit ir Gabijai pristatykit 5 žmones gimusius skirtingais metais",3),
    Task(124,"Mission objective: Gabija B.","3",0,"Paklausti Gabijos kelintais metais buvo pradėtos MIDI ir įrodyti, kad ji neteisi",3),
    Task(125,"Mission objective: bet kuris organizatorius","3",0,"Rasti organizatorių, auginantį šunį, ir įrodyti, jog katinai yra geriau",3),
    Task(126,"Mission objective: bet kuris organizatorius","3",0,"Įkalbinti organizatorių su visa komanda sušokti Tunaką",3),
    Task(127,"Mission objective: foto į Discord","3",0,"Padarykit juokingiausią memą ir įkelti į discord",3),
    Task(128,"Mission objective: foto į Discord","3",0,"Parašykit į discord originalų komplimentą ir padėką renginio organizatoriams",3),
    Task(129,"Mission objective: foto į Discord","3",0,"Nufilmuokit iki 2 minučių trukmės “žinių reportažą” apie renginį “Atgal į kateitį” ir įkelti į discord",3),
    Task(130,"Mission objective: foto į Discord","3", 0,"Nupieškit Micių ir nuotrauką įkelkit į discord,, geriausią piešinį išrinksime konkurso pabaigoje", 3),
    Task(131,"Mission objective: ???","3",0,"Fakultete paslėptas lobis, užuomina: QR",3),
    Task(132, "Mission objective: ???", "3", 0, "Susigrąžinti Miciaus galvą iš fizikų", 100000)

}

org_dict = {
    "1":
        {
            "tid": 0,
            "name": "Komandos atstovas turi paglostyti Vytenio galvą",
            "points": 1
        },
    "2":
        {
            "tid": 0,
            "name": "Mystery box",
            "points": 1
        },
    "3": {
            "tid": 0,
            "name": "Dviejų lyčių atstovai apsikeičia rūbais",
            "points": 1
        },
    "4": {
            "tid": 0,
            "name": "Išvardinti 10 programavimo kalbų",
            "points": 1
        },
    "5": {
            "tid": 0,
            "name": "Laimėti kryžiukus nuliukus prieš Gabrielę",
            "points": 1
        },

    "6": {
            "tid": 0,
            "name": "Konvertuoti dvejetaine arba šešioliktaine sistema parašytą skaičių į dešimtainę sistemą",
            "points": 1
        },
    "7": {
            "tid": 0,
            "name": "Visa komanda turi apkabinti Gabrielę",
            "points": 1
        },
    "8": {
            "tid": 0,
            "name": "Įrodykit, kad FIDI > MIDI",
            "points": 1
        },
    "9": {
            "tid": 0,
            "name": "Pateikit 10 faktų kodėl MIDI > KD",
            "points": 1
        },
    "10": {
            "tid": 0,
            "name": "Išvardinti tris matematikos teoremas ir jas paaiškinti",
            "points": 1
        },
    "11": {
            "tid": 0,
            "name": "Visi komandos nariai 1 minutę daro grupinį apsikabinimą",
            "points": 1
        },
    "12": {
            "tid": 0,
            "name": "Eglei pristatyti 3 žmones, kurie augina katinus",
            "points": 1
        },
    "13": {
            "tid": 0,
            "name": "Kiekvienam iš komandos pasibučiuoti su savo lyties žmogumi",
            "points": 1
        },
    "14": {
            "tid": 0,
            "name": "Atpasakokit visą “Back to the future” siužetą",
            "points": 1
        },
    "15": {
            "tid": 0,
            "name": "Apsukti delną nejudinant riešo",
            "points": 1
        },
    "16": {
            "tid": 0,
            "name": "Nufotografuokit penkias tatuiruotes ir parodykit Barborai",
            "points": 1
        },
    "17": {
            "tid": 0,
            "name": "Pataikyti popieriaus gabaliuką į šiukšlių dėžę kitam patalpos gale",
            "points": 1
        },
    "18": {
            "tid": 0,
            "name": "Sudainuokit Kunigundą Rokui",
            "points": 1
        },
    "19": {
            "tid": 0,
            "name": "Pasakykit juokingiausią “your mom” juokelį kurį žinai",
            "points": 1
        },
    "20": {
            "tid": 0,
            "name": "Komanda turi išvardinti visus 10 Elono Musko vaikų vardus",
            "points": 1
        },
    "21": {
            "tid": 0,
            "name": "Vienas komandos narys turi Rokui parodyti savo geriausią Joker impression",
            "points": 1
        },
    "22": {
            "tid": 0,
            "name": "Išspręsti Rubiko kubą",
            "points": 1
        },
     "23": {
            "tid": 0,
            "name": "Per nustatytą laiką, iš ant juosmens pritvirtintos dėžutės su skyle, iškratyti joje esančius kamuoliukus",
            "points": 1
        },
    "24": {
            "tid": 0,
            "name": "Išvardinkit 5 vardus iš nurodytos raidės per 5 sekundes",
            "points": 1
        },
    "25": {
            "tid": 0,
            "name": "Išvardinkit 7 katinų veisles per 15 sekundžių",
            "points": 1
        },
    "26": {
            "tid": 0,
            "name": "Komandai sušokti vieną just dance šokį",
            "points": 1
        },
    "27": {
            "tid": 0,
            "name": "Paklausti Ugnės kodėl ji atrodo tokia pikta ir bauginanti",
            "points": 1
        },
    "28": {
            "tid": 0,
            "name": "Išsiaiškinkit kiek exit ženklų yra fakultete",
            "points": 1
        },
    "29": {
            "tid": 0,
            "name": "Išvardinkit šešis veikėjus iš duoto filmo",
            "points": 1
        },
    "30": {
            "tid": 0,
            "name": "Bent pusė komandos turi atsistoti ant rankų (kiti gali prilaikyti)",
            "points": 1
        },
    "31": {
            "tid": 0,
            "name": "Išvardinkit 15 Marvel filmų iš atminties",
            "points": 1
        },
    "32": {
            "tid": 0,
            "name": "Komandos nariams susikibus už parankių į išorę, kiekvienas narys paeiliui turi ant buteliuko, kuris yra atsuktas, uždėti kamuoliuką",
            "points": 1
        },
    "33": {
            "tid": 0,
            "name": "Pasakykit ketureilį su duotu žodžiu",
            "points": 1
        },
    "34": {
            "tid": 0,
            "name": "Įkalbinkit Danielių kartu pašokti Macaren'ą",
            "points": 1
        },
    "35": {
            "tid": 0,
            "name": "Visa komanda iš vieno aukšto į kitą aukštą užlipti žąsele",
            "points": 1
        },
    "36": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "37": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "38": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "39": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "40": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "41": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "42": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "43": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "44": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "45": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "46": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "47": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "48": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "49": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "50": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "51": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "52": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "53": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "54": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "55": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "56": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "57": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "58": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "59": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "60": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "61": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "62": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "63": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "64": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "65": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "66": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "67": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "68": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "69": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "70": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "71": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "72": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "73": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "74": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "75": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "76": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "77": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "78": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "79": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "80": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "81": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "82": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "83": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },  
    "84": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },   
    "85": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        }, 
    "86": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "87": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "88": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "89": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "90": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "91": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "92": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "93": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "94": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "95": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "96": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "97": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "98": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "99": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "100": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "101": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "102": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "103": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "104": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "105": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "106": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "107": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "108": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "109": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "110": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "111": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "112": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "113": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "114": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "115": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "116": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "117": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "118": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "119": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "120": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "121": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "122": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "123": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "124": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "125": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "126": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "127": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "128": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "129": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "130": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "131": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        },
    "132": {
            "tid": 0,
            "name": "Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų",
            "points": 1
        }
}


# def check_answer(uid, answer):
#     kitten = functions.find_user(uid)
#     crib = functions.load_guild(kitten)
#     with open("tasks.json", "r") as t:
#         data = json.load(t)
#         if answer in data.keys():
#             task = Task(*data[answer].values())
#             if crib.currentTask == task.id:
#                 result = crib.add_points(task.reward)
#                 crib.give_next()
#                 functions.upload_guild(crib)
#                 if len(crib.completedTasks) >= 24:
#                     return "You have completed " + str(task.name) + "\nReward of " + str(task.reward) + " points has been given \n"
#                 if result:
#                     return "You have completed " + str(task.name) + "\nReward of " + str(task.reward) + " points has been given \nYour next task is"
#             else:
#                 return "This is not the correct answer"
#         else:
#             return "This is not the correct answer"

def skip_task(cid, diff):
    with open("cribChannels.json", "r") as f:
        data = json.load(f)
        if cid in data.keys():
            kitten = data[cid]
            crib = functions.load_guild(kitten)
            if diff == 1:
                crib.skip(1)
                functions.upload_guild(crib)
                return "Easy objective has been sucessfully skipped"
            elif diff == 2:
                crib.skip(2)
                functions.upload_guild(crib)
                return "Medium objective has been sucessfully skipped"
            elif diff == 3:
                crib.skip(3)
                functions.upload_guild(crib)
                return "Hard objective has been sucessfully skipped"

def org_give_points(uid, cid, Admin, diff):
    with open("cribChannels.json", "r") as f:
        data = json.load(f)
        if cid in data.keys():
            kitten = data[cid]
            crib = functions.load_guild(kitten)
            if diff == 1:
                tid, name, points = org_dict[str(crib.currentEasyTask)].values()
                if Admin == 1:
                    result = crib.add_points(points)
                    if result:
                        crib.give_next(1)
                        functions.upload_guild(crib)
                        if crib.currentEasyTask == -1:
                            return "You have completed " + str(name) + "\nReward of " + str(
                            points) + " points has been given \nYou have completed all easy tasks!"
                        else:
                            return "You have completed " + str(name) + "\nReward of " + str(
                                points) + " points has been given \nYour next task is"
                    return "Add Points"
                elif str(uid) == str(tid):
                    result = crib.add_points(points)
                    if result:
                        crib.give_next(1)
                        functions.upload_guild(crib)
                        if crib.currentEasyTask == -1:
                            return "You have completed " + str(name) + "\nReward of " + str(
                            points) + " points has been given \nYou have completed all easy tasks!"
                        else:
                            return "You have completed " + str(name) + "\nReward of " + str(
                                points) + " points has been given \nYour next task is"
                    return "Add Points"
                else:
                    return "Pachdon comrade, but you're not able to use this command"
            if diff == 2:
                tid, name, points = org_dict[str(crib.currentMediumTask)].values()
                if Admin == 1:
                    result = crib.add_points(points)
                    if result:
                        crib.give_next(2)
                        functions.upload_guild(crib)
                        if crib.currentMediumTask == -1:
                            return "You have completed " + str(name) + "\nReward of " + str(
                            points) + " points has been given \nYou have completed all medium tasks!"
                        else:
                            return "You have completed " + str(name) + "\nReward of " + str(
                                points) + " points has been given \nYour next task is"
                    return "Add Points"
                elif str(uid) == str(tid):
                    result = crib.add_points(points)
                    if result:
                        crib.give_next(2)
                        functions.upload_guild(crib)
                        if crib.currentMediumTask == -1:
                            return "You have completed " + str(name) + "\nReward of " + str(
                            points) + " points has been given \nYou have completed all medium tasks!"
                        else:
                            return "You have completed " + str(name) + "\nReward of " + str(
                                points) + " points has been given \nYour next task is"
                    return "Add Points"
                else:
                    return "Pachdon comrade, but you're not able to use this command"
            if diff == 3:
                tid, name, points = org_dict[str(crib.currentHardTask)].values()
                if Admin == 1:
                    result = crib.add_points(points)
                    if result:
                        crib.give_next(3)
                        functions.upload_guild(crib)
                        if crib.currentHardTask == -1:
                            return "You have completed " + str(name) + "\nReward of " + str(
                            points) + " points has been given \nYou have completed all hard tasks!"
                        else:
                            return "You have completed " + str(name) + "\nReward of " + str(
                                points) + " points has been given \nYour next task is"
                    return "Add Points"
                elif str(uid) == str(tid):
                    result = crib.add_points(points)
                    if result:
                        crib.give_next(3)
                        functions.upload_guild(crib)
                        if crib.currentHardTask == -1:
                            return "You have completed " + str(name) + "\nReward of " + str(
                            points) + " points has been given \nYou have completed all hard tasks!"
                        else:
                            return "You have completed " + str(name) + "\nReward of " + str(
                                points) + " points has been given \nYour next task is"
                    return "Add Points"
                else:
                    return "Pachdon comrade, but you're not able to use this command"
        else:
            print("something is wrong :)")


def get_task(currenttask):
    for t in task_dict:
        if t.id == currenttask:
            embed = discord.Embed(title=t.name, description=t.task)
            return embed
