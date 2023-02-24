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

# Please don't do it like this. This is a very bad practice.
# Use a json file instead. (Reuse one of the functions from functions.py that use json files)
# This is just hardcoded.
task_dict = {
    Task(47, "Mission objective: Vytenis", "1", 0, ":flag_lt: Komandos atstovas turi paglostyti Vytenio galvą\n:flag_gb: A representative of the team has to stroke Vytenis' head.", 1),
    Task(58, "Mission objective: Vytenis", "1", 0, ":flag_lt: Mystery box\n:flag_gb: Mystery box", 1),
    Task(32,"Mission objective: Gabrielė D.","1", 0, ":flag_lt: Dviejų lyčių atstovai apsikeičia rūbais\n:flag_gb: People of two different genders exchange clothes",1),
    Task(28,"Mission objective: Gabrielė D.","1",0,":flag_lt: Išvardinti 10 programavimo kalbų\n:flag_gb: List 10 programming languages", 1),
    Task(37,"Mission objective: Gabrielė D.","1",0, ":flag_lt: Laimėti kryžiukus nuliukus prieš Gabrielę\n:flag_gb: Win a game of criss cross against Gabrielė",1),
    Task(16,"Mission objective: Gabrielė D.","1",0, ":flag_lt: Konvertuoti dvejetaine arba šešioliktaine sistema parašytą skaičių į dešimtainę sistemą\n:flag_gb: Convert a number written in binary or hexadecimal to decimal",1),
    Task(53,"Mission objective: Gabrielė D.","1",0, ":flag_lt: Visa komanda turi apkabinti Gabrielę\n:flag_gb: The whole team has to hug Gabrielė",1),
    Task(30,"Mission objective: Eglė","1",0, ":flag_lt: Įrodykit, kad FIDI > MIDI\n:flag_gb: Prove that FIDI > MIDI",1),
    Task(24,"Mission objective: Eglė","1",0, ":flag_lt: Pateikit 10 faktų kodėl MIDI > KD\n:flag_gb: Present 10 facts as to why MIDI > KD",1),
    Task(4,"Mission objective: Eglė","1",0, ":flag_lt: Išvardinti tris matematikos teoremas ir jas paaiškinti\n:flag_gb: Name three math theorems and explain them",1),
    Task(1,"Mission objective: Eglė","1",0, ":flag_lt: Visi komandos nariai 1 minutę daro grupinį apsikabinimą\n:flag_gb: All team members do a group hug for one minute",1),
    Task(14,"Mission objective: Eglė","1",0, ":flag_lt: Eglei pristatyti 3 žmones, kurie augina katinus\n:flag_gb: Present Eglė with three people who have cats",1),
    Task(7,"Mission objective: Vaiva","1",0, ":flag_lt: Kiekvienam iš komandos pasibučiuoti su savo lyties žmogumi\n:flag_gb: Every team member has to kiss another member of the same gender",1),
    Task(3,"Mission objective: Vaiva","1",0, ":flag_lt: Atpasakokit visą “Back to the future” siužetą\n:flag_gb: Retell the whole plot of “Back to the future”",1),
    Task(5,"Mission objective: Vaiva","1",0,":flag_lt: Apsukti delną nejudinant riešo\n:flag_gb: Turn the palm around without moving the wrist",1),
    Task(60,"Mission objective: Barbora","1",0,":flag_lt: Nufotografuokit penkias tatuiruotes ir parodykit Barborai\n:flag_gb: Photograph five tattoos and show them to Barbora",1),
    Task(44,"Mission objective: Rokas","1",0,":flag_lt: Pataikyti popieriaus gabaliuką į šiukšlių dėžę kitam patalpos gale\n:flag_gb: Successfully throw a piece of paper into a bin across the room",1),
    Task(26,"Mission objective: Rokas","1",0,":flag_lt: Sudainuokit Kunigundą Rokui\n:flag_gb: Sing an annoying pop song to Rokas",1),
    Task(59,"Mission objective: Rokas","1",0,":flag_lt: Pasakykit juokingiausią “your mom” juokelį kurį žinai\n:flag_gb: Tell the funniest “your mom” joke you know",1),
    Task(49,"Mission objective: Rokas","1",0,":flag_lt: Komanda turi išvardinti visus 10 Elono Musko vaikų vardus\n:flag_gb: The team has to name all 10 of Elon Musk's children",1),
    Task(55,"Mission objective: Rokas","1",0,":flag_lt: Vienas komandos narys turi Rokui parodyti savo geriausią Joker impression\n:flag_gb: One team member has to show Rokas their best Joker impression",1),
    Task(39,"Mission objective: Rokas","1",0,":flag_lt: Išspręsti Rubiko kubą\n:flag_gb: Solve a Rubik's cube",1),
    Task(35,"Mission objective: Rokas","1",0,":flag_lt: Per nustatytą laiką, iš ant juosmens pritvirtintos dėžutės su skyle, iškratyti joje esančius kamuoliukus\n:flag_gb: In a set amount of time, shake out the balls out of a box with a hole that's secured to your waist",1),
    Task(45,"Mission objective: Ugnė B.","1",0,":flag_lt: Išvardinkit 5 vardus iš nurodytos raidės per 5 sekundes\n:flag_gb: List 5 names from the given letter in 5 seconds",1),
    Task(43,"Mission objective: Ugnė B.","1",0,":flag_lt: Išvardinkit 7 katinų veisles per 15 sekundžių\n:flag_gb: List 7 breeds of cats in 15 seconds",1),
    Task(36,"Mission objective: Ugnė B.","1",0,":flag_lt: Komandai sušokti vieną “Just dance” šokį\n:flag_gb: The team has to perform a “Just dance” dance",1),
    Task(41,"Mission objective: Ugnė M.","1",0,":flag_lt: Paklausti Ugnės kodėl ji atrodo tokia pikta ir bauginanti\n:flag_gb: Ask Ugnė why she looks so angry and scary",1),
    Task(33,"Mission objective: Simona U.","1",0,":flag_lt: Išsiaiškinkit kiek exit ženklų yra fakultete\n:flag_gb: Find out how many exit signs there are in the faculty",1),
    Task(6,"Mission objective: Aistė","1",0,":flag_lt: Išvardinkit šešis veikėjus iš duoto filmo\n:flag_gb: Name six characters from a given movie",1),
    Task(61,"Mission objective: Aistė","1",0,":flag_lt: Bent pusė komandos turi atsistoti ant rankų (kiti gali prilaikyti)\n:flag_gb: At least a half of the team members has to do a hand-stand (others can help them up)",1),
    Task(11,"Mission objective: Aistė","1",0,":flag_lt: Išvardinkit 15 Marvel filmų iš atminties\n:flag_gb: Name 15 Marvel movies from memory",1),
    Task(25,"Mission objective: Aistė","1",0,":flag_lt: Komandos nariams susikibus už parankių į išorę, kiekvienas narys paeiliui turi ant buteliuko, kuris yra atsuktas, uždėti kamuoliuką\n:flag_gb: With the team members crossing arms facing outward, each member in turn has to place a ball on the bottle, which is open",1),
    Task(19,"Mission objective: Akvilė","1",0,":flag_lt: Pasakykit ketureilį su duotu žodžiu\n:flag_gb: Recite a 4 line verse with the given word",1),
    Task(27,"Mission objective: Danielius","1",0,":flag_lt: Įkalbinkit Danielių kartu pašokti Macaren'ą\n:flag_gb: Convince Danielius to dance the Macarena with you",1),
    Task(29,"Mission objective: Danielius","1",0,":flag_lt: Visa komanda iš vieno aukšto į kitą aukštą užlipti žąsele\n:flag_gb: Go from one floor to another while ducking",1),
    Task(54,"Mission objective: Danielius","1",0,":flag_lt: Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų\n:flag_gb: Have each of your team members perform the swallow yoga pose",1),
    Task(57,"Mission objective: Mėta","1",0,":flag_lt: Papasakokit anekdotą Mėtai\n:flag_gb: Tell a joke to Mėta",1),
    Task(2,"Mission objective: Mėta","1",0,":flag_lt: Sušokti vieną MIF šokį\n:flag_gb: Perform one MIF dance",1),
    Task(51,"Mission objective: Ovidijus","1",0,":flag_lt: Raskit Ovidijų ir pasiūlykit jam tris LINKSMAS dainas\n:flag_gb: Find Ovidijus and suggest 3 happy songs",1),
    Task(18,"Mission objective: Monika","1",0,":flag_lt: Prajuokinkit Moniką\n:flag_gb: Make Monika laugh",1),
    Task(8,"Mission objective: Monika","1",0,":flag_lt: Plojimais, trepsėjimu ir pan. sukurti ritmą ir jį atlikti Monikai\n:flag_gb: Using claps, stomps and so on, create a rhythm and perform it to Monika",1),
    Task(52,"Mission objective: Monika","1",0,":flag_lt: Nufotografuoti visų komandos narių telefonų ekranus, kuriuose rodoma, kad visi seka  VU SA MIF instagramą\n:flag_gb: Take a photo of all the phone screens of the team members, in which it is shown that they follow VU SA MIF on instagram",1),
    Task(46,"Mission objective: Gabriekė K.","1",0,":flag_lt: Pasakykit du pick-up lines Gabrielei\n:flag_gb: Tell two pick-up lines to Gabrielė",1),
    Task(22,"Mission objective: Vygintas","1",0,":flag_lt: Atspėti ir Vygintui pasakyti, kas yra vyriausias MIF'o pirmakursis\n:flag_gb: Guess who the oldest MIF first-year student is and say their name to Vygintas",1),
    Task(17,"Mission objective: Gabija L.","1",0,":flag_lt: Per 7 sek. išvardinkit visas skirtingas šachmatų figūrėles\n:flag_gb: List all chess pieces in 7 seconds",1),
    Task(9,"Mission objective: Gabija L.","1",0,":flag_lt: Sudarykit labiausiai MIF sielą atspindintį Spotify grojaraštį ir parodyti Gabijai\n:flag_gb: Make the most MIF-themed Spotify playlist possible and show it to Gabija",1),
    Task(50,"Mission objective: Gabija A.","1",0,":flag_lt: Sudėlioti dėlionę, kurioje pavaizduotas kažkas susijęs su MIF\n:flag_gb: Solve a jigsaw puzzle of something related to MIF",1),
    Task(38,"Mission objective: Gabija A.","1",0,":flag_lt: Bent pusė komandos narių turi pasidaryti naujas šukuosenas (Parodyti prieš ir po nuotraukas)\n:flag_gb: Have at least half of your team get a new haircut (With before and after photos)",1),
    Task(10,"Mission objective: Gabija A.","1",0,":flag_lt: Visa komandą turi sudainuoti dainą iš filmo/filmuko Gabijai, o ji turi atspėti koks čia filmas/filmukas\n:flag_gb: Sing a song from a movie/cartoon to Gabija and have her guess which movie/catoon the song is from",1),
    Task(48,"Mission objective: :flag_lt: bet kuris organizatorius (:flag_gb: any organizer)","1",0,":flag_lt: Nufotografuoti Organizatorių, jam nematant ir parodyti jam\n:flag_gb: Take a photo of an organizer when they do not see and show the photo to them",1),
    Task(13,"Mission objective: :flag_lt: bet kuris organizatorius (:flag_gb: any organizer)","1",0,":flag_lt: Sugalvoti kaip ir apgauti organizatorių\n:flag_gb: Think of a way and trick an organizer",1),
    Task(23,"Mission objective: :flag_lt: bet kuris organizatorius (:flag_gb: any organizer)","1",0,":flag_lt: Visai komandai garsiai sušukti „MIDI geriau nei FIDI“\n:flag_gb: The entirety of the team loudly shouts “MIDI is better than FIDI”",1),
    Task(15,"Mission objective: :flag_lt: bet kuris organizatorius (:flag_gb: any organizer)","1",0,":flag_lt: Paduok puodelį vandens organizatoriui\n:flag_gb: Give a cup of water to an organizer",1),
    Task(34,"Mission objective: :flag_lt: bet kuris organizatorius (:flag_gb: any organizer)","1",0,":flag_lt: Surasti organizatorių kuris nerūko\n:flag_gb: Find an organizer who does not smoke",1),
    Task(21,"Mission objective: :flag_lt: bet kuris organizatorius (:flag_gb: any organizer)","1",0,":flag_lt: Sugalvoti originalų komandos šūkį ir garsiai jį sušukti\n:flag_gb: Create a clever team slogan and present it to an organizer",1),
    Task(56,"Mission objective: :flag_lt: foto į Discord (:flag_gb: photo to Discord)","1",0,":flag_lt: Visai komandai nusipiešti katės ūsus ir nosytes ant veido ir įkelti nuotrauką į discord\n:flag_gb: Have all of your team draw cat whiskers and noses on their faces and upload a picture to Discord",1),
    Task(40,"Mission objective: :flag_lt: foto į Discord (:flag_gb: photo to Discord)","1",0,":flag_lt: Visai komandai nusifotografuoti su kita komanda ir nuotrauką įkelti į discord\n:flag_gb: Take a photo with another team and upload the photo to Discord",1),
    Task(31,"Mission objective: :flag_lt: foto į Discord (:flag_gb: photo to Discord)","1",0,":flag_lt: Iš komandos narių sudėti MIDI logotipą, nufotografuoti ir įkelti į discord\n:flag_gb: Make a human-logo of MIDI, take a photo of it and upload it to Discord",1),
    Task(42,"Mission objective: :flag_lt: foto į Discord (:flag_gb: photo to Discord)","1",0,":flag_lt: Padaryti ir įkelti į discord komandos nuotrauką, kurioje kiekvienas narys veido išraiška rodo skirtingą emoji\n:flag_gb: ake a picture of your team where each team member represents a different emoji, upload it to Discord",1),
    Task(12,"Mission objective: :flag_lt: foto į Discord (:flag_gb: photo to Discord)","1",0,":flag_lt: Surasti ir nusifotografuoti prie baseino įėjimo, nuotrauką įkelti į discord\n:flag_gb: Find and take a photo at the pool entrance, upload it to Discord",1),
    Task(20,"Mission objective: :flag_lt: foto į Discord (:flag_gb: photo to Discord)","1",0,":flag_lt: Sukurti mįslę apie katiną\n:flag_gb: Create a riddle about a cat",1),

    Task(87,"Mission objective: Vytenis","2",0,":flag_lt: Parodykit Vyteniui įdomų daiktą\n:flag_gb: Show Vytenis an interesting item",3),
    Task(100,"Mission objective: Vytenis","2",0,":flag_lt: Laimeti stalo futbolo žaidimą prieš Vytenį\n:flag_gb: Win against Vytenis in a game of table football",3),
    Task(105,"Mission objective: Vytenis","2",0,":flag_lt: Komandiškai išbūti kėdute 2 minutes\n:flag_gb: Hold the chair position for 2 minutes as a team",3),
    Task(68,"Mission objective: Gabrielė D.","2",0,":flag_lt: Šarados - trys žodžiai iš Gabrielės\n:flag_gb: Charades - three words from Gabrielė",3),
    Task(108,"Mission objective: Eglė","2",0,":flag_lt: Eglei pristatykit 4 žmones su tokiais pačiais vardais\n:flag_gb: Present Egle with 4 people who have the same names",3),
    Task(79,"Mission objective: Eglė","2",0,":flag_lt: Surasti studentą iš kito fakulteto ir pristatyti organizatoriui\n:flag_gb: Find a student from a different faculty and present them to Eglė",3),
    Task(95,"Mission objective: Vaiva","2",0,":flag_lt: Laimėti rock paper scissors prieš Vaivą 5 kartus iš eilės\n:flag_gb: Win against Vaiva 5 times in a row in a game of rock paper scissors",3),
    Task(103,"Mission objective: Vaiva","2",0,":flag_lt: Susikabinus rankomis su komandos nariais, persiųsti lanką nuo pirmo iki paskutinio žmogaus (per nustatytą laiką)\n:flag_gb: Joining hands with the team members, pass the hoop from the first person to the last person (in a set time)",3),
    Task(67,"Mission objective: Vaiva","2",0,":flag_lt: Su kitos komandos atstovu/atstove sužaisti rock paper scissors, taškus gauna laimėjusi komanda\n:flag_gb: Play a game of rock paper scissors with another teams representative, the winning team gets the point",3),
    Task(64,"Mission objective: Barbora","2",0,":flag_lt: Visa komanda turi padaryti žmonių statulą\n:flag_gb: The whole team has to make a human statue",3),
    Task(74,"Mission objective: Barbora","2",0,":flag_lt: Vieni kitiems nupieškite tatuiruotes\n:flag_gb: Draw tattoos on each other",3),
    Task(78,"Mission objective: Rokas","2",0,":flag_lt: Atspėkit žodį iš N raidės\n:flag_gb: Guess a word which begins with the letter N",3),
    Task(81,"Mission objective: Rokas","2",0,":flag_lt: Padarykit kuo aukštesnį bokštą iš aplinkiniu daiktų\n:flag_gb: Make the biggest possible tower out of surrounding objects",3),
    Task(69,"Mission objective: Ugnė B.","2",0,":flag_lt: 10 komandinių pritūpimų/atsilenkimų\n:flag_gb: 10 team squats/sit-ups",3),
    Task(66,"Mission objective: Ugnė B.","2",0,":flag_lt: Komanda turi 90 sekundžių išstovėti ant vienos kojos užsimerkę\n:flag_gb: The team has to stand on one leg with closed eyes for 90 seconds",3),
    Task(109,"Mission objective: Simona U.","2",0,":flag_lt: Suskaičiuokit, kiek Didlaukio pastate yra auditorijų\n:flag_gb: Count how many auditoriums there are in the Didlaukis faculty",3),
    Task(97,"Mission objective: Simona U.","2",0,":flag_lt: Nugalėti 3 kitos komandos atstovus rankos lenkime\n:flag_gb: Win against 3 representatives of another team in arm wrestling",3),
    Task(92,"Mission objective: Aistė","2",0,":flag_lt: Vieną iš komandos narių reikia pernešti laikant jį ore, kol jis “skrenda kaip supermenas”\n:flag_gb: You have to carry one of the team members while they're “flying like Superman”",3),
    Task(86,"Mission objective: Aistė","2",0,":flag_lt: Dainuojant dainą „Du gaideliai“, vaidinti dainos siužetą\n:flag_gb: Act out the plot of a popular children's song while singing it",3),
    Task(91,"Mission objective: Akvilė","2",0,":flag_lt: Išspręsti sudoku\n:flag_gb: Solve a sudoku",3),
    Task(99,"Mission objective: Danielius","2",0,":flag_lt: Išvardinkit dabartinio biuro narius\n:flag_gb: List all current VU SA MIF office members",3),
    Task(93,"Mission objective: Danielius","2",0,":flag_lt: Pusė komandos turi kitą pusę pernešti iš vieno koridoriaus galo į kitą\n:flag_gb: Have half of your team carry the other half from one end of the corridor to the other",3),
    Task(98,"Mission objective: Danielius","2",0,":flag_lt: Visi komandos nariai turi 45 sekundes daryti lentą\n:flag_gb: Have your entire team hold the plank for 45 seconds",3),
    Task(101,"Mission objective: Danielius","2",0,":flag_lt: Visi komandos nariai turi pagauti monetą, mestą nuo tos pačios alkūnės\n:flag_gb: Have your team throw a coin off of their elbow and catch it with the same hand",3),
    Task(107,"Mission objective: Danielius","2",0,":flag_lt: Kiekvienas komandos narys turi padaryti skirtingą jogos pozą\n:flag_gb: Have each member of your team perform a different yoga pose",3),
    Task(102,"Mission objective: Mėta","2",0,":flag_lt: Mėtai paaiškinti kodėl DCEU > MCU\n:flag_gb: Explain to Mėta why DCEU > MCU",3),
    Task(83,"Mission objective: Ovidijus","2",0,":flag_lt: Ant lapo sukurti kodą, kuris išrašytų daugybos lentelę (iki 10x10) ir duoti patikrinti Ovidijui\n:flag_gb:Write a computer code on paper, which would print out the multiplication table (up to 10x10) and show it to Ovidijus",3),
    Task(71,"Mission objective: Eidvilė","2",0,":flag_lt: Sukurkit kostiumą duota tema per 2 minutes\n:flag_gb: Create a costume relating to a given topic in two minutes",3),
    Task(65,"Mission objective: Eidvilė","2",0,":flag_lt: Nupieškit komandos nario portretą su burna\n:flag_gb: Draw a portrait of a teammate with your mouth",3),
    Task(82,"Mission objective: Monika","2",0,":flag_lt: Iš visos širdies sudainuoti 3 milijonus\n:flag_gb: From the bottom of your heart sing “The Official EuroBasket 2011 Anthem of Lithuania”",3),
    Task(56,"Mission objective: Monika","2",0,":flag_lt: Nusifotografuoti su kiekvienu šio renginio srities vadovu ir parodyti Monikai\n:flag_gb: Take a photo with all the leading organizers of this event and show it to Monika. (There are 4 of them)",3),
    Task(80,"Mission objective: Lukas","2",0,":flag_lt: Komandai sudainuoti MIDI himną\n:flag_gb: Sing the MIDI anthem",3),
    Task(63,"Mission objective: Vygintas","2",0,":flag_lt: Organizatoriui išvardinti 20 pi skaitmenų po kablelio be telefono\n:flag_gb: List out 20 decimal digits of pi without any assistance to an organizer",3),
    Task(73,"Mission objective: Vygintas","2",0,":flag_lt: Beer pong'as be alkoholio. Kiekvienas komandos narys meta kamuoliuką lygiai vieną kartą, ir jei nors puse komandos narių pataiko, užduotis įvykdyta\n:flag_gb: Beer pong without alcohol. Each member tosses once, and for the task to be complete, at least half of the attempts must be hits",3),
    Task(104,"Mission objective: Vygintas","2",0,":flag_lt: Perduoti kamuoliuką tik su šaukštais stovint eilute\n:flag_gb: Pass a ball using spoons while standing in a line",3),
    Task(96,"Mission objective: Vygintas","2",0,":flag_lt: Vygintui pristatyti 10 žmonių iš skirtingų miestų\n:flag_gb: Show 10 people from different cities to Vygintas",3),
    Task(77,"Mission objective: Gabija L.","2",0,":flag_lt: Papasakokit duoto filmo siužetą po vieną sakinį. Vienas komandos narys pasako vieną sakinį - po to kitas\n:flag_gb: Recite the given movie scenario sentence by sentence. One sentence per member",2),
    Task(62,"Mission objective: Gabija A.","2",0,":flag_lt: Išspręsti kryžiažodį\n:flag_gb: Solve a crossword puzzle",3),
    Task(85,"Mission objective: Gabija A.","2",0,"Fakultete surasti ir nufotografuoti visos vaivorykštės spalvų daiktus\n:flag_gb: Find and take a photo of all rainbow-colored items in the faculty",3),
    Task(72,"Mission objective: Gabija A.","2",0,":flag_lt: Bent pusė komandos narių turi specialiai apsiverkti, išspausti bent vieną ašarą\n:flag_gb: Have at least half of your team cry at least one tear",3),
    Task(88,"Mission objective: Ieva Marija","2",0,":flag_lt: Sugalvoti plana kaip pavogti dinozaurą nuo fizikų stogo ir pristatyti Ievai Marijai\n:flag_gb: Create a plan detailing the theft of the dinosaur on top of the Faculty of Physics and tell it to Ieva Marija",3),
    Task(75,"Mission objective: Ieva Marija","2",0,":flag_lt: Kiekvienas komandos narys turi pasakyti Ievai Marijai, kodėl gaidelio sausainiai yra patys geriausi\n:flag_gb: Have each member of your team tell Ieva Marija why Gaidelis biscuits are the best",3),
    Task(90,"Mission objective: :flag_lt: foto į Discord (:flag_gb: photo to Discord)","2",0,":flag_lt: Nufilmuokit kaip vienas iš komandos nariu daro a flip (galima padėti) ir įkelkit į discord\n:flag_gb: Record one of your teammates doing a flip (can be assisted), and upload it to Discord",3),
    Task(94,"Mission objective: :flag_lt: foto į Discord (:flag_gb: photo to Discord)","2",0,":flag_lt: Komandos atstovui nusifotografuoti su laukiniu katinu kur nors Didlaukio teritorijoje ir įkelti nuotrauką į discord\n:flag_gb: Take a photo with a cat poster somewhere in the territory of Didlaukis and upload it to Discord",3),
    Task(76,"Mission objective: :flag_lt: foto į Discord (:flag_gb: photo to Discord)","2",0,":flag_lt: Sukonstruoti katiną, naudojantis žmonėmis, nufotografuoti ir įkelti į discord\n:flag_gb: Form a cat from people, take a photo of it and upload it to Discord",3),
    Task(70,"Mission objective: :flag_lt: foto į Discord (:flag_gb: photo to Discord)","2",0,":flag_lt: Komanda turi Didlaukio teritorijoje surasti ir pasidaryti nuotrauką su Miciaus mašina, ją įkelti į discord\n:flag_gb: Find the Micius car in the territory of Didlaukis and take a photo of it, upload it to Discord",3),
    Task(89,"Mission objective: :flag_lt: foto į Discord (:flag_gb: photo to Discord)","2",0,":flag_lt: Pastatyti piramidę iš komandos narių, nufotografuoti ir įkelti į discord\n:flag_gb: Make a team pyramid, take a photo if it and upload it to Discord",3),
    Task(84,"Mission objective: :flag_lt: foto į Discord (:flag_gb: photo to Discord)","2",0,":flag_lt: Iš grupėje turimų augintinių nuotraukų padaryti koliažą tema “Miciaus draugai” ir įkelti į discord\n:flag_gb: From photos you and your teammates have of pets create a collage themed “Friends of Micius” and upload it to Discord",3),

    Task(129,"Mission objective: Vytenis","3",0,":flag_lt: Nugalėk Vytenį Tetris žaidime\n:flag_gb: Win against Vytenis in a tetris game",7),
    Task(125,"Mission objective: Gabrielė D.","3",0,":flag_lt: Suvalgyti 4 gaidelius per minutę neužsigeriant\n:flag_gb: Eat 4 cookies in a minute without drinking them down with anything",7),
    Task(111,"Mission objective: Gabrielė D.","3",0,":flag_lt: Išsiaiškinkit mystery kodą - gsli;yrysd\n:flag_gb: Decipher the mystery code -  gsli;yrysd",7),
    Task(117,"Mission objective: Barbora","3",0,":flag_lt: Laimėkit šokių dvikovoje prieš kitą komandą\n:flag_gb: Win in a dance battle against a rival team",7),
    Task(131,"Mission objective: Barbora","3",0,":flag_lt: Kiekvienam komandos nariui reikia prisistatyti skirtinga kalba\n:flag_gb: Each team member has to introduce themselves in a different language",7),
    Task(115,"Mission objective: Ugnė M.","3",0,":flag_lt: Išspręsti du loginius uždavinius, kol Ugnė palaiko spaudimą\n:flag_gb: Solve two logic problems while Ugnė is keeping you under pressure",7),
    Task(122,"Mission objective: Aistė","3",0,":flag_lt: Ant lapo, kuris yra ant kito komandos nario nugaros, kažką nupiešti ir tas komandos narys turi atspėti\n:flag_gb: Draw something on a piece of paper that's on a teammates back and they try to guess it",7),
    Task(128,"Mission objective: Ovidijus","3",0,":flag_lt: Įrodykit Ovidijui kodėl assembler yra geriausia visų laikų programavimo kalba\n:flag_gb: Prove to Ovidijus why Assembler is the best programming language",7),
    Task(124,"Mission objective: Eidvilė","3",0,":flag_lt: Komandos atstovas turi apsirengti kuo daugiau sluoksnių drabužių\n:flag_gb: The team representative has to dress up in as many layers of clothes as possible",7),
    Task(119,"Mission objective: Gustas","3",0,":flag_lt: Nugalėti Gustą žaidime Typeracer\n:flag_gb: Win against Gustas in Typeracer",7),
    Task(118,"Mission objective: Vygintas","3",0,":flag_lt: Raskite ir Vygintui pristatykite 2 žmones gimusius vienos dienos skirtumu (back to back dienomis) (pvz. spalio 14 d. ir spalio 15 d.)\n:flag_gb: Find 2 people born on back-to-back days and show them to Vygintas (e.g. oct 14 and oct 15)",7),
    Task(121,"Mission objective: Gabija L.","3",0,":flag_lt: Parodykit magijos triuką\n:flag_gb: Show a magic trick",7),
    Task(116,"Mission objective: Gabija L.","3",0,":flag_lt: Raskit ir Gabijai pristatykit 5 žmones gimusius skirtingais metais\n:flag_gb: Find 5 people born in different years and show them to Gabija",7),
    Task(132,"Mission objective: Gabija B.","3",0,":flag_lt: Paklausti Gabijos kelintais metais buvo pradėtos MIDI ir įrodyti, kad ji neteisi\n:flag_gb: Ask Gabija when MIDI (the days of Mathematics and Informatics) first started and prove to her that she is wrong",7),
    Task(130,"Mission objective: :flag_lt: bet kuris organizatorius (:flag_gb: any organizer)","3",0,":flag_lt: Rasti organizatorių, auginantį šunį, ir įrodyti, jog katinai yra geriau\n:flag_gb: Find an organizer that has dogs and prove to him that cats are better",7),
    Task(126,"Mission objective: :flag_lt: bet kuris organizatorius (:flag_gb: any organizer)","3",0,":flag_lt: Įkalbinti organizatorių su visa komanda sušokti Tunaką\n:flag_gb: Invite an organizer to dance Tunak with the entire team",7),
    Task(110,"Mission objective: :flag_lt: foto į Discord (:flag_gb: photo to Discord)", "3", 0, ":flag_lt: Nufotografuokit kažką ir įkelkit į discord, konkurso pabaigoje bus išrinkta geriausia nuotrauka\n:flag_gb: Take a picture of something and upload it to Discord. The best photo will be picked at the end of the event", 0),
    Task(123,"Mission objective: :flag_lt: foto į Discord (:flag_gb: photo to Discord)","3",0,":flag_lt: Padarykit juokingiausią memą ir įkelti į discord, konkurso pabaigoje bus išrinkta geriausia nuotrauka\n:flag_gb: Make a funny meme and upload it to Discord. The best photo will be picked at the end of the event",0),
    Task(112,"Mission objective: :flag_lt: foto į Discord (:flag_gb: photo to Discord)","3",0,":flag_lt: Parašykit į discord originalų komplimentą ir padėką renginio organizatoriams\n:flag_gb: Post a creative compliment and a thank-you to the organizers of the event",7),
    Task(114,"Mission objective: :flag_lt: foto į Discord (:flag_gb: photo to Discord)","3",0,":flag_lt: Nufilmuokit iki 2 minučių trukmės “žinių reportažą” apie renginį “Atgal į kateitį” ir įkelti į discord\n:flag_gb: Film a two minute video report about the event “Atgal į Kateitį” and upload it to Discord",7),
    Task(113,"Mission objective: :flag_lt: foto į Discord (:flag_gb: photo to Discord)","3", 0,":flag_lt: Nupieškit Micių ir nuotrauką įkelkit į discord,, geriausią piešinį išrinksime konkurso pabaigoje\n:flag_gb: Draw Micius and take a photo of the drawing, upload it to Discord. Best drawing at the end of the contest wins", 0),
    Task(127,"Mission objective: ???","3",0,":flag_lt: Fakultete paslėptas lobis, užuomina: QR\n:flag_gb: A treasure is hidden in the faculty, hint: QR",14),
    Task(120,"Mission objective: ???","3",0,":flag_lt: Susigrąžinti Miciaus galvą iš fizikų\n:flag_gb: Bring back the head of Micius from FIDI",100000)

}

org_dict = {
    "47":{
            "name": ":flag_lt: Komandos atstovas turi paglostyti Vytenio galvą\n:flag_gb: A representative of the team has to stroke Vytenis' head.",
            "points": 1
        },
    "58":
        {
            "name": ":flag_lt: Mystery box\n:flag_gb: Mystery box",
            "points": 1
        },
    "32": {
            "name": ":flag_lt: Dviejų lyčių atstovai apsikeičia rūbais\n:flag_gb: People of two different genders exchange clothes",
            "points": 1
        },
    "28": {
            "name": ":flag_lt: Išvardinti 10 programavimo kalbų\n:flag_gb: List 10 programming languages",
            "points": 1
        },
    "37": {
            "name": ":flag_lt: Laimėti kryžiukus nuliukus prieš Gabrielę\n:flag_gb: Win a game of criss cross against Gabrielė",
            "points": 1
        },
    "16": {
            "name": ":flag_lt: Konvertuoti dvejetaine arba šešioliktaine sistema parašytą skaičių į dešimtainę sistemą\n:flag_gb: Convert a number written in binary or hexadecimal to decimal",
            "points": 1
        },
    "53": {
            "name": ":flag_lt: Visa komanda turi apkabinti Gabrielę\n:flag_gb: The whole team has to hug Gabrielė",
            "points": 1
        },
    "30": {
            "name": ":flag_lt: Įrodykit, kad FIDI > MIDI\n:flag_gb: Prove that FIDI > MIDI",
            "points": 1
        },
    "24": {
            "name": ":flag_lt: Pateikit 10 faktų kodėl MIDI > KD\n:flag_gb: Present 10 facts as to why MIDI > KD",
            "points": 1
        },
    "4": {
            "name": ":flag_lt: Išvardinti tris matematikos teoremas ir jas paaiškinti\n:flag_gb: Name three math theorems and explain them",
            "points": 1
        },
    "1": {
            "name": ":flag_lt: Visi komandos nariai 1 minutę daro grupinį apsikabinimą\n:flag_gb: All team members do a group hug for one minute",
            "points": 1
        },
    "14": {
            "name": ":flag_lt: Eglei pristatyti 3 žmones, kurie augina katinus\n:flag_gb: Present Eglė with three people who have cats",
            "points": 1
        },
    "7": {
            "name": ":flag_lt: Kiekvienam iš komandos pasibučiuoti su savo lyties žmogumi\n:flag_gb: Every team member has to kiss another member of the same gender",
            "points": 1
        },
    "3": {
            "name": ":flag_lt: Atpasakokit visą “Back to the future” siužetą\n:flag_gb: Retell the whole plot of “Back to the future”",
            "points": 1
        },
    "5": {
            "name": ":flag_lt: Apsukti delną nejudinant riešo\n:flag_gb: Turn the palm around without moving the wrist",
            "points": 1
        },
    "60": {
            "name": ":flag_lt: Nufotografuokit penkias tatuiruotes ir parodykit Barborai\n:flag_gb: Photograph five tattoos and show them to Barbora",
            "points": 1
        },
    "44": {
            "name": ":flag_lt: Pataikyti popieriaus gabaliuką į šiukšlių dėžę kitam patalpos gale\n:flag_gb: Successfully throw a piece of paper into a bin across the room",
            "points": 1
        },
    "26": {
            "name": ":flag_lt: Sudainuokit Kunigundą Rokui\n:flag_gb: Sing an annoying pop song to Rokas",
            "points": 1
        },
    "59": {
            "name": ":flag_lt: Pasakykit juokingiausią “your mom” juokelį kurį žinai\n:flag_gb: Tell the funniest “your mom” joke you know",
            "points": 1
        },
    "49": {
            "name": ":flag_lt: Komanda turi išvardinti visus 10 Elono Musko vaikų vardus\n:flag_gb: The team has to name all 10 of Elon Musk's children",
            "points": 1
        },
    "55": {
            "name": ":flag_lt: Vienas komandos narys turi Rokui parodyti savo geriausią Joker impression\n:flag_gb: One team member has to show Rokas their best Joker impression",
            "points": 1
        },
    "39": {
            "name": ":flag_lt: Išspręsti Rubiko kubą\n:flag_gb: Solve a Rubik's cube",
            "points": 1
        },
    "35": {
            "name": ":flag_lt: Per nustatytą laiką, iš ant juosmens pritvirtintos dėžutės su skyle, iškratyti joje esančius kamuoliukus\n:flag_gb: In a set amount of time, shake out the balls out of a box with a hole that's secured to your waist",
            "points": 1
        },
    "45": {
            "name": ":flag_lt: Išvardinkit 5 vardus iš nurodytos raidės per 5 sekundes\n:flag_gb: List 5 names from the given letter in 5 seconds",
            "points": 1
        },
    "43": {
            "name": ":flag_lt: Išvardinkit 7 katinų veisles per 15 sekundžių\n:flag_gb: List 7 breeds of cats in 15 seconds",
            "points": 1
        },
    "36": {
            "name": ":flag_lt: Komandai sušokti vieną “Just dance” šokį\n:flag_gb: The team has to perform a “Just dance” dance",
            "points": 1
        },
    "41": {
            "name": ":flag_lt: Paklausti Ugnės kodėl ji atrodo tokia pikta ir bauginanti\n:flag_gb: Ask Ugnė why she looks so angry and scary",
            "points": 1
        },
    "33": {
            "name": ":flag_lt: Išsiaiškinkit kiek exit ženklų yra fakultete\n:flag_gb: Find out how many exit signs there are in the faculty",
            "points": 1
        },
    "6": { 
            "name": ":flag_lt: Išvardinkit šešis veikėjus iš duoto filmo\n:flag_gb: Name six characters from a given movie",
            "points": 1
        },
    "61": {
            "name": ":flag_lt: Bent pusė komandos turi atsistoti ant rankų (kiti gali prilaikyti)\n:flag_gb: At least a half of the team members has to do a hand-stand (others can help them up)",
            "points": 1
        },
    "11": {
            "name": ":flag_lt: Išvardinkit 15 Marvel filmų iš atminties\n:flag_gb: Name 15 Marvel movies from memory",
            "points": 1
        },
    "25": {
            "name": ":flag_lt: Komandos nariams susikibus už parankių į išorę, kiekvienas narys paeiliui turi ant buteliuko, kuris yra atsuktas, uždėti kamuoliuką\n:flag_gb: With the team members crossing arms facing outward, each member in turn has to place a ball on the bottle, which is open",
            "points": 1
        },
    "19": {
            "name": ":flag_lt: Pasakykit ketureilį su duotu žodžiu\n:flag_gb: Recite a 4 line verse with the given word",
            "points": 1
        },
    "27": {
            "name": ":flag_lt: Įkalbinkit Danielių kartu pašokti Macaren'ą\n:flag_gb: Convince Danielius to dance the Macarena with you",
            "points": 1
        },
    "29": {
            "name": ":flag_lt: Visa komanda iš vieno aukšto į kitą aukštą užlipti žąsele\n:flag_gb: Go from one floor to another while ducking",
            "points": 1
        },
    "54": {
            "name": ":flag_lt: Vienas komandos narys turi padaryti kregždutę (atsistoti ant vienos kojos pasilenkti ir išskėsti rankas į šonus) ir atsistoti ant pirštų galų\n:flag_gb: Have each of your team members perform the swallow yoga pose",
            "points": 1
        },
    "57": {
            "name": ":flag_lt: Papasakokit anekdotą Mėtai\n:flag_gb: Tell a joke to Mėta",
            "points": 1
        },
    "2": {
            "name": ":flag_lt: Sušokti vieną MIF šokį\n:flag_gb: Perform one MIF dance",
            "points": 1
        },
    "51": {
            "name": ":flag_lt: Raskit Ovidijų ir pasiūlykit jam tris LINKSMAS dainas\n:flag_gb: Find Ovidijus and suggest 3 happy songs",
            "points": 1
        },
    "18": {
            "name": ":flag_lt: Prajuokinkit Moniką\n:flag_gb: Make Monika laugh",
            "points": 1
        },
    "8": {  
            "name": ":flag_lt: Plojimais, trepsėjimu ir pan. sukurti ritmą ir jį atlikti Monikai\n:flag_gb: Using claps, stomps and so on, create a rhythm and perform it to Monika",
            "points": 1
        },
    "52": {
            "name": ":flag_lt: Nufotografuoti visų komandos narių telefonų ekranus, kuriuose rodoma, kad visi seka  VU SA MIF instagramą\n:flag_gb: Take a photo of all the phone screens of the team members, in which it is shown that they follow VU SA MIF on instagram",
            "points": 1
        },
    "46": {
            "name": ":flag_lt: Pasakykit du pick-up lines Gabrielei\n:flag_gb: Tell two pick-up lines to Gabrielė",
            "points": 1
        },
    "22": {
            "name": ":flag_lt: Atspėti ir Vygintui pasakyti, kas yra vyriausias MIF'o pirmakursis\n:flag_gb: Guess who the oldest MIF first-year student is and say their name to Vygintas",
            "points": 1
        },
    "17": {
            "name": ":flag_lt: Per 7 sek. išvardinkit visas skirtingas šachmatų figūrėles\n:flag_gb: List all chess pieces in 7 seconds",
            "points": 1
        },
    "9": {
            "name": ":flag_lt: Sudarykit labiausiai MIF sielą atspindintį Spotify grojaraštį ir parodyti Gabijai\n:flag_gb: Make the most MIF-themed Spotify playlist possible and show it to Gabija",
            "points": 1
        },
    "50": {
            "name": ":flag_lt: Sudėlioti dėlionę, kurioje pavaizduotas kažkas susijęs su MIF\n:flag_gb: Solve a jigsaw puzzle of something related to MIF",
            "points": 1
        },
    "38": {
            "name": ":flag_lt: Bent pusė komandos narių turi pasidaryti naujas šukuosenas (Parodyti prieš ir po nuotraukas)\n:flag_gb: Have at least half of your team get a new haircut (With before and after photos)",
            "points": 1
        },
    "10": {
            "name": ":flag_lt: Visa komandą turi sudainuoti dainą iš filmo/filmuko Gabijai, o ji turi atspėti koks čia filmas/filmukas\n:flag_gb: Sing a song from a movie/cartoon to Gabija and have her guess which movie/catoon the song is from",
            "points": 1
        },
    "48": {
            "name": ":flag_lt: Nufotografuoti Organizatorių, jam nematant ir parodyti jam\n:flag_gb: Take a photo of an organizer when they do not see and show the photo to them",
            "points": 1
        },
    "13": {
            "name":":flag_lt: Sugalvoti kaip ir apgauti organizatorių\n:flag_gb: Think of a way and trick an organizer",
            "points": 1
        },
    "23": {
            "name": ":flag_lt: Visai komandai garsiai sušukti „MIDI geriau nei FIDI“\n:flag_gb: The entirety of the team loudly shouts “MIDI is better than FIDI”",
            "points": 1
        },
    "15": {
            "name": ":flag_lt: Paduok puodelį vandens organizatoriui\n:flag_gb: Give a cup of water to an organizer",
            "points": 1
        },
    "34": {
            "name": ":flag_lt: Surasti organizatorių kuris nerūko\n:flag_gb: Find an organizer who does not smoke",
            "points": 1
        },
    "21": {
            "name": ":flag_lt: Sugalvoti originalų komandos šūkį ir garsiai jį sušukti\n:flag_gb: Create a clever team slogan and present it to an organizer",
            "points": 1
        },
    "56": {
            "name": ":flag_lt: Visai komandai nusipiešti katės ūsus ir nosytes ant veido ir įkelti nuotrauką į discord\n:flag_gb: Have all of your team draw cat whiskers and noses on their faces and upload a picture to Discord",
            "points": 1
        },
    "40": {
            "name": ":flag_lt: Visai komandai nusifotografuoti su kita komanda ir nuotrauką įkelti į discord\n:flag_gb: Take a photo with another team and upload the photo to Discord",
            "points": 1
        },
    "31": {
            "name": ":flag_lt: Iš komandos narių sudėti MIDI logotipą, nufotografuoti ir įkelti į discord\n:flag_gb: Make a human-logo of MIDI, take a photo of it and upload it to Discord",
            "points": 1
        },
    "42": {
            "name": ":flag_lt: Padaryti ir įkelti į discord komandos nuotrauką, kurioje kiekvienas narys veido išraiška rodo skirtingą emoji\n:flag_gb: ake a picture of your team where each team member represents a different emoji, upload it to Discord",
            "points": 1
        },
    "12": {
            "name": ":flag_lt: Surasti ir nusifotografuoti prie baseino įėjimo, nuotrauką įkelti į discord\n:flag_gb: Find and take a photo at the pool entrance, upload it to Discord",
            "points": 1
        },
    "20": {
            "name": ":flag_lt: Sukurti mįslę apie katiną\n:flag_gb: Create a riddle about a cat",
            "points": 1
        },


    "87": {
            "name": ":flag_lt: Parodykit Vyteniui įdomų daiktą\n:flag_gb: Show Vytenis an interesting item",
            "points": 3
        },
    "100": {
            "name": ":flag_lt: Laimeti stalo futbolo žaidimą prieš Vytenį\n:flag_gb: Win against Vytenis in a game of table football",
            "points": 3
        },
    "105": {
            "name": ":flag_lt: Komandiškai išbūti kėdute 2 minutes\n:flag_gb: Hold the chair position for 2 minutes as a team",
            "points": 3
        },
    "68": {
            "name": ":flag_lt: Šarados - trys žodžiai iš Gabrielės\n:flag_gb: Charades - three words from Gabrielė",
            "points": 3
        },
    "108": {
            "name": ":flag_lt: Eglei pristatykit 4 žmones su tokiais pačiais vardais\n:flag_gb: Present Egle with 4 people who have the same names",
            "points": 3
        },
    "79": {
            "name": ":flag_lt: Surasti studentą iš kito fakulteto ir pristatyti organizatoriui\n:flag_gb: Find a student from a different faculty and present them to Eglė",
            "points": 3
        },
    "95": {
            "name": ":flag_lt: Laimėti rock paper scissors prieš Vaivą 5 kartus iš eilės\n:flag_gb: Win against Vaiva 5 times in a row in a game of rock paper scissors",
            "points": 3
        },
    "103": {
            "name": ":flag_lt: Susikabinus rankomis su komandos nariais, persiųsti lanką nuo pirmo iki paskutinio žmogaus (per nustatytą laiką)\n:flag_gb: Joining hands with the team members, pass the hoop from the first person to the last person (in a set time)",
            "points": 3
        },
    "67": {
            "name": ":flag_lt: Su kitos komandos atstovu/atstove sužaisti rock paper scissors, taškus gauna laimėjusi komanda\n:flag_gb: Play a game of rock paper scissors with another teams representative, the winning team gets the point",
            "points": 3
        },
    "64": {
            "name": ":flag_lt: Visa komanda turi padaryti žmonių statulą\n:flag_gb: The whole team has to make a human statue",
            "points": 3
        },
    "74": {
            "name": ":flag_lt: Vieni kitiems nupieškite tatuiruotes\n:flag_gb: Draw tattoos on each other",
            "points": 3
        },
    "78": {
            "name": ":flag_lt: Atspėkit žodį iš N raidės\n:flag_gb: Guess a word which begins with the letter N",
            "points": 3
        },
    "81": {
            "name": ":flag_lt: Padarykit kuo aukštesnį bokštą iš aplinkiniu daiktų\n:flag_gb: Make the biggest possible tower out of surrounding objects",
            "points": 3
        },
    "69": {
            "name": ":flag_lt: 10 komandinių pritūpimų/atsilenkimų\n:flag_gb: 10 team squats/sit-ups",
            "points": 3
        },
    "66": {
            "name": ":flag_lt: Komanda turi 90 sekundžių išstovėti ant vienos kojos užsimerkę\n:flag_gb: The team has to stand on one leg with closed eyes for 90 seconds",
            "points": 3
        },
    "109": {
            "name": ":flag_lt: Suskaičiuokit, kiek Didlaukio pastate yra auditorijų\n:flag_gb: Count how many auditoriums there are in the Didlaukis faculty",
            "points": 3
        },
    "97": {
            "name": ":flag_lt: Nugalėti 3 kitos komandos atstovus rankos lenkime\n:flag_gb: Win against 3 representatives of another team in arm wrestling",
            "points": 3
        },
    "92": {
            "name": ":flag_lt: Vieną iš komandos narių reikia pernešti laikant jį ore, kol jis “skrenda kaip supermenas”\n:flag_gb: You have to carry one of the team members while they're “flying like Superman”",
            "points": 3
        },
    "86": {
            "name": ":flag_lt: Dainuojant dainą „Du gaideliai“, vaidinti dainos siužetą\n:flag_gb: Act out the plot of a popular children's song while singing it",
            "points": 3
        },
    "91": {
            "name": ":flag_lt: Išspręsti sudoku\n:flag_gb: Solve a sudoku",
            "points": 3
        },
    "99": {
            "name": ":flag_lt: Išvardinkit dabartinio biuro narius\n:flag_gb: List all current VU SA MIF office members",
            "points": 3
        },
    "93": {
            "name": ":flag_lt: Pusė komandos turi kitą pusę pernešti iš vieno koridoriaus galo į kitą\n:flag_gb: Have half of your team carry the other half from one end of the corridor to the other",
            "points": 3
        },  
    "98": {
            "name": ":flag_lt: Visi komandos nariai turi 45 sekundes daryti lentą\n:flag_gb: Have your entire team hold the plank for 45 seconds",
            "points": 3
        },   
    "101": {
            "name": ":flag_lt: Visi komandos nariai turi pagauti monetą, mestą nuo tos pačios alkūnės\n:flag_gb: Have your team throw a coin off of their elbow and catch it with the same hand",
            "points": 3
        }, 
    "107": {
            "name": ":flag_lt: Kiekvienas komandos narys turi padaryti skirtingą jogos pozą\n:flag_gb: Have each member of your team perform a different yoga pose",
            "points": 3
        },
    "102": {
            "name": ":flag_lt: Mėtai paaiškinti kodėl DCEU > MCU\n:flag_gb: Explain to Mėta why DCEU > MCU",
            "points": 3
        },
    "83": {
            "name": ":flag_lt: Ant lapo sukurti kodą, kuris išrašytų daugybos lentelę (iki 10x10) ir duoti patikrinti Ovidijui\n:flag_gb:Write a computer code on paper, which would print out the multiplication table (up to 10x10) and show it to Ovidijus",
            "points": 3
        },
    "71": {
            "name": ":flag_lt: Sukurkit kostiumą duota tema per 2 minutes\n:flag_gb: Create a costume relating to a given topic in two minutes",
            "points": 3
        },
    "65": {
            "name": ":flag_lt: Nupieškit komandos nario portretą su burna\n:flag_gb: Draw a portrait of a teammate with your mouth",
            "points": 3
        },
    "82": {
            "name": ":flag_lt: Iš visos širdies sudainuoti 3 milijonus\n:flag_gb: From the bottom of your heart sing “The Official EuroBasket 2011 Anthem of Lithuania”",
            "points": 3
        },
    "56": {
            "name": ":flag_lt: Nusifotografuoti su kiekvienu šio renginio srities vadovu ir parodyti Monikai\n:flag_gb: Take a photo with all the leading organizers of this event and show it to Monika. (There are 4 of them)",
            "points": 3
        },
    "80": {
            "name": ":flag_lt: Komandai sudainuoti MIDI himną\n:flag_gb: Sing the MIDI anthem",
            "points": 3
        },
    "63": {
            "name": ":flag_lt: Organizatoriui išvardinti 20 pi skaitmenų po kablelio be telefono\n:flag_gb: List out 20 decimal digits of pi without any assistance to an organizer",
            "points": 3
        },
    "73": {
            "name": ":flag_lt: Beer pong'as be alkoholio. Kiekvienas komandos narys meta kamuoliuką lygiai vieną kartą, ir jei nors puse komandos narių pataiko, užduotis įvykdyta\n:flag_gb: Beer pong without alcohol. Each member tosses once, and for the task to be complete, at least half of the attempts must be hits",
            "points": 3
        },
    "104": {
            "name": ":flag_lt: Perduoti kamuoliuką tik su šaukštais stovint eilute\n:flag_gb: Pass a ball using spoons while standing in a line",
            "points": 3
        },
    "96": {
            "name": ":flag_lt: Vygintui pristatyti 10 žmonių iš skirtingų miestų\n:flag_gb: Show 10 people from different cities to Vygintas",
            "points": 3
        },
    "77": {
            "name": ":flag_lt: Papasakokit duoto filmo siužetą po vieną sakinį. Vienas komandos narys pasako vieną sakinį - po to kitas\n:flag_gb: Recite the given movie scenario sentence by sentence. One sentence per member",
            "points": 3
        },
    "62": {
            "name": ":flag_lt: Išspręsti kryžiažodį\n:flag_gb: Solve a crossword puzzle",
            "points": 3
        },
    "85": {
            "name": "Fakultete surasti ir nufotografuoti visos vaivorykštės spalvų daiktus\n:flag_gb: Find and take a photo of all rainbow-colored items in the faculty",
            "points": 3
        },
    "72": {
            "name": ":flag_lt: Bent pusė komandos narių turi specialiai apsiverkti, išspausti bent vieną ašarą\n:flag_gb: Have at least half of your team cry at least one tear",
            "points": 3
        },
    "88": {
            "name": ":flag_lt: Sugalvoti plana kaip pavogti dinozaurą nuo fizikų stogo ir pristatyti Ievai Marijai\n:flag_gb: Create a plan detailing the theft of the dinosaur on top of the Faculty of Physics and tell it to Ieva Marija",
            "points": 3
        },
    "75": {
            "name": ":flag_lt: Kiekvienas komandos narys turi pasakyti Ievai Marijai, kodėl gaidelio sausainiai yra patys geriausi\n:flag_gb: Have each member of your team tell Ieva Marija why Gaidelis biscuits are the best",
            "points": 3
        },
    "90": {
            "name": ":flag_lt: Nufilmuokit kaip vienas iš komandos nariu daro a flip (galima padėti) ir įkelkit į discord\n:flag_gb: Record one of your teammates doing a flip (can be assisted), and upload it to Discord",
            "points": 3
        },
    "94": {
            "name": ":flag_lt: Komandos atstovui nusifotografuoti su laukiniu katinu kur nors Didlaukio teritorijoje ir įkelti nuotrauką į discord\n:flag_gb: Take a photo with a cat poster somewhere in the territory of Didlaukis and upload it to Discord",
            "points": 3
        },
    "76": {
            "name": ":flag_lt: Sukonstruoti katiną, naudojantis žmonėmis, nufotografuoti ir įkelti į discord\n:flag_gb: Form a cat from people, take a photo of it and upload it to Discord",
            "points": 3
        },
    "70": {
            "name": ":flag_lt: Komanda turi Didlaukio teritorijoje surasti ir pasidaryti nuotrauką su Miciaus mašina, ją įkelti į discord\n:flag_gb: Find the Micius car in the territory of Didlaukis and take a photo of it, upload it to Discord",
            "points": 3
        },
    "89": {
            "name": ":flag_lt: Pastatyti piramidę iš komandos narių, nufotografuoti ir įkelti į discord\n:flag_gb: Make a team pyramid, take a photo if it and upload it to Discord",
            "points": 3
        },
    "84": {
            "name": ":flag_lt: Iš grupėje turimų augintinių nuotraukų padaryti koliažą tema “Miciaus draugai” ir įkelti į discord\n:flag_gb: From photos you and your teammates have of pets create a collage themed “Friends of Micius” and upload it to Discord",
            "points": 3
        },


    "129": {
            "name": ":flag_lt: Nugalėk Vytenį Tetris žaidime\n:flag_gb: Win against Vytenis in a tetris game",
            "points": 7
        },
    "125": {
            "name": ":flag_lt: Suvalgyti 4 gaidelius per minutę neužsigeriant\n:flag_gb: Eat 4 cookies in a minute without drinking them down with anything",
            "points": 7
        },
    "111": {
            "name": ":flag_lt: Išsiaiškinkit mystery kodą - gsli;yrysd\n:flag_gb: Decipher the mystery code -  gsli;yrysd",
            "points": 7
        },
    "117": {
            "name": ":flag_lt: Laimėkit šokių dvikovoje prieš kitą komandą\n:flag_gb: Win in a dance battle against a rival team",
            "points": 7
        },
    "131": {
            "name": ":flag_lt: Kiekvienam komandos nariui reikia prisistatyti skirtinga kalba\n:flag_gb: Each team member has to introduce themselves in a different language",
            "points": 7
        },
    "115": {
            "name": ":flag_lt: Išspręsti du loginius uždavinius, kol Ugnė palaiko spaudimą\n:flag_gb: Solve two logic problems while Ugnė is keeping you under pressure",
            "points": 7
        },
    "122": {
            "name": ":flag_lt: Ant lapo, kuris yra ant kito komandos nario nugaros, kažką nupiešti ir tas komandos narys turi atspėti\n:flag_gb: Draw something on a piece of paper that's on a teammates back and they try to guess it",
            "points": 7
        },
    "128": {
            "name": ":flag_lt: Įrodykit Ovidijui kodėl assembler yra geriausia visų laikų programavimo kalba\n:flag_gb: Prove to Ovidijus why Assembler is the best programming language",
            "points": 7
        },
    "124": {
            "name": ":flag_lt: Komandos atstovas turi apsirengti kuo daugiau sluoksnių drabužių\n:flag_gb: The team representative has to dress up in as many layers of clothes as possible",
            "points": 7
        },
    "119": {
            "name": ":flag_lt: Nugalėti Gustą žaidime Typeracer\n:flag_gb: Win against Gustas in Typeracer",
            "points": 7
        },
    "118": {
            "name": ":flag_lt: Raskite ir Vygintui pristatykite 2 žmones gimusius vienos dienos skirtumu (back to back dienomis) (pvz. spalio 14 d. ir spalio 15 d.)\n:flag_gb: Find 2 people born on back-to-back days and show them to Vygintas (e.g. oct 14 and oct 15)",
            "points": 7
        },
    "121": {
            "name": ":flag_lt: Parodykit magijos triuką\n:flag_gb: Show a magic trick",
            "points": 7
        },
    "116": {
            "name": ":flag_lt: Raskit ir Gabijai pristatykit 5 žmones gimusius skirtingais metais\n:flag_gb: Find 5 people born in different years and show them to Gabija",
            "points": 7
        },
    "132": {
            "name": ":flag_lt: Paklausti Gabijos kelintais metais buvo pradėtos MIDI ir įrodyti, kad ji neteisi\n:flag_gb: Ask Gabija when MIDI (the days of Mathematics and Informatics) first started and prove to her that she is wrong",
            "points": 7
        },
    "130": {
            "name": ":flag_lt: Rasti organizatorių, auginantį šunį, ir įrodyti, jog katinai yra geriau\n:flag_gb: Find an organizer that has dogs and prove to him that cats are better",
            "points": 7
        },
    "126": {
            "name": ":flag_lt: Įkalbinti organizatorių su visa komanda sušokti Tunaką\n:flag_gb: Invite an organizer to dance Tunak with the entire team",
            "points": 7
        },
    "110": {
            "name": ":flag_lt: Nufotografuokit kažką ir įkelkit į discord, konkurso pabaigoje bus išrinkta geriausia nuotrauka\n:flag_gb: Take a picture of something and upload it to Discord. The best photo will be picked at the end of the event",
            "points": 0
        },
    "123": {
            "name": ":flag_lt: Padarykit juokingiausią memą ir įkelti į discord\n:flag_gb: Make a funny meme and upload it to Discord",
            "points": 0
        },
    "112": {
            "name": ":flag_lt: Parašykit į discord originalų komplimentą ir padėką renginio organizatoriams\n:flag_gb: Post a creative compliment and a thank-you to the organizers of the event",
            "points": 7
        },
    "114": {
            "name": ":flag_lt: Nufilmuokit iki 2 minučių trukmės “žinių reportažą” apie renginį “Atgal į kateitį” ir įkelti į discord\n:flag_gb: Film a two minute video report about the event “Atgal į Kateitį” and upload it to Discord",
            "points": 7
        },
    "113": {
            "name": ":flag_lt: Nupieškit Micių ir nuotrauką įkelkit į discord,, geriausią piešinį išrinksime konkurso pabaigoje\n:flag_gb: Draw Micius and take a photo of the drawing, upload it to Discord. Best drawing at the end of the contest wins",
            "points": 0
        },
    "127": {
            "name": ":flag_lt: Fakultete paslėptas lobis, užuomina: QR\n:flag_gb: A treasure is hidden in the faculty, hint: QR",
            "points": 14
        },
    "120": {
            "name": ":flag_lt: Susigrąžinti Miciaus galvą iš fizikų\n:flag_gb: Bring back the head of Micius from FIDI",
            "points": 100000
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

# Modifies json file after task skip
def skip_task(cid, diff):
    with open("cribChannels.json", "r") as f:           # Loads json file
        data = json.load(f)
        if cid in data.keys():                          # Checks if channel is in json file
            kitten = data[cid]                          # Loads guild id
            crib = functions.load_guild(kitten)
            if diff == 1:                               
                crib.skip(1)                            # Skips task
                functions.upload_guild(crib)            # Uploads changes to json file
                return "Easy objective has been sucessfully skipped"
            elif diff == 2:
                crib.skip(2)
                functions.upload_guild(crib)
                return "Medium objective has been sucessfully skipped"
            elif diff == 3:
                crib.skip(3)
                functions.upload_guild(crib)
                return "Hard objective has been sucessfully skipped"

# Modifies json file after task finish (adds points)
def org_give_points(uid, cid, Admin, diff):
    with open("cribChannels.json", "r") as f:
        data = json.load(f)
        if cid in data.keys():
            kitten = data[cid]
            crib = functions.load_guild(kitten)
            if diff == 1:
                name, points = org_dict[str(crib.currentEasyTask)].values()     # Loads task name and reward
                if Admin == 1:
                    result = crib.add_points(points)                            # Adds points to guild
                    if result:
                        crib.give_next(1)                                       # Gives next task
                        functions.upload_guild(crib)
                        if crib.currentEasyTask == -1:                          # Checks if all tasks are completed
                            # embed = discord.Embed(title="Congratulations! :tada::tada:", 
                            # description="You have completed:\n" + str(name) + "\nReward of "
                            #  + str(points) + " points has been given!\nYou have completed all easy tasks!")
                            # return embed
                            embed = discord.Embed(title="Congratulations! :tada::tada:", 
                            description="You have completed:\n" + str(name) + "\n:checkered_flag:Reward of :one:"
                            + " points has been given!\nYou have completed all easy tasks!")
                            return embed
                            # return "You have completed " + str(name) + "\nReward of " + str(
                            # points) + " points has been given \nYou have completed all hard tasks!"
                        else:
                            embed = discord.Embed(title="Congratulations! :tada::tada:", 
                            description="You have completed:\n" + str(name) + "\n:checkered_flag:Reward of :one:"
                            + " points has been given!")
                            return embed
                    else:
                        return "Add Points"
                # elif str(uid) == str(tid):
                #     result = crib.add_points(points)
                #     if result:
                #         crib.give_next(1)
                #         functions.upload_guild(crib)
                #         if crib.currentEasyTask == -1:
                #             return "You have completed " + str(name) + "\nReward of " + str(
                #             points) + " points has been given \nYou have completed all easy tasks!"
                #         else:
                #             return "You have completed " + str(name) + "\nReward of " + str(
                #                 points) + " points has been given \nYour next task is"
                #     return "Add Points"
                else:
                    return "Pachdon comrade, but you're not able to use this command"
            if diff == 2:
                name, points = org_dict[str(crib.currentMediumTask)].values()
                if Admin == 1:
                    result = crib.add_points(points)
                    if result:
                        crib.give_next(2)
                        functions.upload_guild(crib)
                        if crib.currentMediumTask == -1:
                            embed = discord.Embed(title="Congratulations! :tada::tada:", 
                            description="You have completed:\n" + str(name) + "\n:checkered_flag:Reward of :three:"
                            + " points has been given!\nYou have completed all medium tasks!")
                            return embed
                            # return "You have completed " + str(name) + "\nReward of " + str(
                            # points) + " points has been given \nYou have completed all hard tasks!"
                        else:
                            embed = discord.Embed(title="Congratulations! :tada::tada:", 
                            description="You have completed:\n" + str(name) + "\n:checkered_flag:Reward of :three:"
                            + " points has been given!")
                            return embed
                    return "Add Points"
                # elif str(uid) == str(tid):
                #     result = crib.add_points(points)
                #     if result:
                #         crib.give_next(2)
                #         functions.upload_guild(crib)
                #         if crib.currentMediumTask == -1:
                #             return "You have completed " + str(name) + "\nReward of " + str(
                #             points) + " points has been given \nYou have completed all medium tasks!"
                #         else:
                #             return "You have completed " + str(name) + "\nReward of " + str(
                #                 points) + " points has been given \nYour next task is"
                #     return "Add Points"
                else:
                    return "Pachdon comrade, but you're not able to use this command"
            if diff == 3:
                name, points = org_dict[str(crib.currentHardTask)].values()
                if Admin == 1:
                    result = crib.add_points(points)
                    if result:
                        crib.give_next(3)
                        functions.upload_guild(crib)
                        if crib.currentHardTask == -1:
                            embed = discord.Embed(title="Congratulations! :tada::tada:", 
                            description="You have completed:\n" + str(name) + "\n:checkered_flag:Reward of :seven:"
                            + " points has been given!\nYou have completed all hard tasks!")
                            return embed
                            # return "You have completed " + str(name) + "\nReward of " + str(
                            # points) + " points has been given \nYou have completed all hard tasks!"
                        else:
                            embed = discord.Embed(title="Congratulations! :tada::tada:", 
                            description="You have completed:\n" + str(name) + "\n:checkered_flag:Reward of :seven:"
                             + " points has been given!")
                            return embed
                            # return "You have completed " + str(name) + "\nReward of " + str(
                            #     points) + " points has been given \nYour next task is"
                    return "Add Points"
                # elif str(uid) == str(tid):
                #     result = crib.add_points(points)
                #     if result:
                #         crib.give_next(3)
                #         functions.upload_guild(crib)
                #         if crib.currentHardTask == -1:
                #             return "You have completed " + str(name) + "\nReward of " + str(
                #             points) + " points has been given \nYou have completed all hard tasks!"
                #         else:
                #             return "You have completed " + str(name) + "\nReward of " + str(
                #                 points) + " points has been given \nYour next task is"
                #     return "Add Points"
                else:
                    return "Pachdon comrade, but you're not able to use this command"
        else:
            print("something is wrong :)")


def get_task(currenttask):
    for t in task_dict:
        if t.id == currenttask:
            embed = discord.Embed(title=t.name, description=t.task)
            return embed
