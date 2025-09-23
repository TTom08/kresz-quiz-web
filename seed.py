from app import app, db
from models import Question, Answer

with app.app_context():
    questions_data = [
        {
            "text": "Mekkora a megengedett legnagyobb sebesség lakott területen belül személygépkocsival?",
            "image_path": None,
            "answers": [
                {"text": "60 km/h", "is_correct": False, "image_path": None},
                {"text": "50 km/h", "is_correct": True, "image_path": None},
                {"text": "70 km/h", "is_correct": False, "image_path": None},
                {"text": "80 km/h", "is_correct": False, "image_path": None}
            ]
        },
        {
            "text": "Melyik jelzés tiltja a 'megállást és a várakozást'?",
            "image_path": None,
            "answers": [
                {"text": "Piros kör, áthúzott P-vel", "is_correct": False, "image_path": None},
                {"text": "Sárga rombusz", "is_correct": False, "image_path": None},
                {"text": "Fekete nyilak a körben", "is_correct": False, "image_path": None},
                {"text": "Piros kör, áthúzott X-szel", "is_correct": True, "image_path": None},
            ]
        },
        {
            "text": "Hol közlekedhet a gyalogos, ha az úton nincs járda, de van leállósáv?",
            "image_path": None,
            "answers": [
                {"text": "A leállósávon", "is_correct": True, "image_path": None},
                {"text": "Az úttest bal szélén", "is_correct": False, "image_path": None},
                {"text": "Az úttest jobb szélén", "is_correct": False, "image_path": None},
                {"text": "Az úttest szélén, de csak ha nincs forgalom", "is_correct": False, "image_path": None}
            ]
        },
        {
            "text": "Melyik oldalon kell elhaladni a szigetcsoport előtt?",
            "image_path": None,
            "answers": [
                {"text": "Jobb oldalon", "is_correct": True, "image_path": None},
                {"text": "Bal oldalon", "is_correct": False, "image_path": None},
                {"text": "Bármelyik oldalon", "is_correct": False, "image_path": None},
                {"text": "A legszélesebb úton", "is_correct": False, "image_path": None}
            ]
        },
        {
            "text": "Melyik a 'Főútvonal' jelzés?",
            "image_path": None,
            "answers": [
                {"text": "Sárga rombusz fehér kerettel", "is_correct": True, "image_path": None},
                {"text": "Sárga kör piros kerettel", "is_correct": False, "image_path": None},
                {"text": "Fehér rombusz sárga kerettel", "is_correct": False, "image_path": None},
                {"text": "Fekete kör fehér kerettel", "is_correct": False, "image_path": None}
            ]
        },
        {
            "text": "Mit jelez a 'Gyermekek' jelzőtábla?",
            "image_path": None,
            "answers": [
                {"text": "Iskolaút", "is_correct": False, "image_path": None},
                {"text": "Gyalogosok átkelőhelye", "is_correct": False, "image_path": None},
                {"text": "Gyermekek tartózkodása", "is_correct": True, "image_path": None},
                {"text": "Iskolánál lassíts", "is_correct": False, "image_path": None}
            ]
        },
        {
            "text": "Mi az autóút?",
            "image_path": None,
            "answers": [
                {"text": "Jelzőtáblával autóútként megjelölt út", "is_correct": True, "image_path": None},
                {"text": "Minden osztott pályás út", "is_correct": False, "image_path": None},
                {"text": "Minden lakott területen kívüli párhuzamos közlekedésre alkalmas út", "is_correct": False, "image_path": None},
                {"text": "Minden lakott területen kívüli osztott pályás út", "is_correct": False, "image_path": None}
            ]
        },
        {
            "text": "Mi a teendő, ha valamely közúti jelzés a rendőr jelzésével ellentétes?",
            "image_path": None,
            "answers": [
                {"text": "A rendőr jelzésének megfelelő módon kell eljárni", "is_correct": True, "image_path": None},
                {"text": "Meg kell állni", "is_correct": False, "image_path": None},
                {"text": "Meg kell várni, amíg a helyzet tisztázódik", "is_correct": False, "image_path": None},
                {"text": "A közúti jelzésnek megfelelő módon kell eljárni", "is_correct": False, "image_path": None}
            ]
        },
        {
            "text": "Mely esetben kell irányjelzést adni az alábbiak közül?",
            "image_path": None,
            "answers": [
                {"text": "Útkanyarulatban", "is_correct": False, "image_path": None},
                {"text": "Útpadkára való lehúzódáskor", "is_correct": True, "image_path": None},
                {"text": "Körforgalmú útra történő bekanyarodáskor", "is_correct": False, "image_path": None},
                {"text": "Veszélyes útkanyarulatban", "is_correct": False, "image_path": None}
            ]
        },
        {
            "text": "Mire hívja fel a figyelmet a járda szegélyén levő folytonos sárga vonal?",
            "image_path": None,
            "answers": [
                {"text": "A várakozás tilalmára", "is_correct": False, "image_path": None},
                {"text": "A megállás tilalmára", "is_correct": True, "image_path": None},
                {"text": "A megállás helyét jelzi", "is_correct": False, "image_path": None},
                {"text": "A járdán való várakozás tilalmára", "is_correct": False, "image_path": None}
            ]
        },
        {
            "text": "Miről ismerhető fel a veszélyes anyagot szállító jármű?",
            "image_path": None,
            "answers": [
                {"text": "Figyelmeztető jelzést adó készülékkel van felszerelve", "is_correct": False, "image_path": None},
                {"text": "Az elején és a hátulján narancssárga alapszínű, felirat nélküli vagy felirattal ellátott táblával van megjelölve", "is_correct": True, "image_path": None},
                {"text": "A figyelmeztető jelzést adó berendezését működtetik", "is_correct": False, "image_path": None},
                {"text": "Az elején és a hátulján 'veszélyes anyag szállítás' feliratú táblával van megjelölve", "is_correct": False, "image_path": None}
            ]
        },
        {
            "text": "Melyik gépjármű az alábbiak közül?",
            "image_path": None,
            "answers": [
                {"text": "A villamos", "is_correct": False, "image_path": None},
                {"text": "A motorkerékpár", "is_correct": True, "image_path": None},
                {"text": "A mezőgazdasági vontató", "is_correct": False, "image_path": None},
                {"text": "A segédmotoros kerékpár", "is_correct": False, "image_path": None}
            ]
        },
        # --- 10 KÉPES KÉRDÉS ---
        {
            "text": "Melyik jelzés a 'Megállni tilos'?",
            "image_path": None,
            "answers": [
                {"text": None, "is_correct": True, "image_path": "/static/images/tablak/Megallni_tilos.jpg"},
                {"text": None, "is_correct": False, "image_path": "/static/images/tablak/kotelezo-haladasi-kikerulesi-irany-egy-iranyba.jpg"},
                {"text": None, "is_correct": False, "image_path": "/static/images/tablak/Kotelezo_haladasi_irany_egyenesen_es_balra.jpg"},
                {"text": None, "is_correct": False, "image_path": "/static/images/tablak/mindket_iranybol_behajtani_tilos.png"}
            ]
        },
        {
            "text": "Melyik jelzés a 'Kötelező haladási irány' tábla?",
            "image_path": None,
            "answers": [
                {"text": None, "is_correct": False, "image_path": "/static/images/tablak/jobbra_kanyarodni_tilos.png"},
                {"text": None, "is_correct": True, "image_path": "/static/images/tablak/kotelezo-haladasi-kikerulesi-irany-egy-iranyba.jpg"},
                {"text": None, "is_correct": False, "image_path": "/static/images/tablak/autobusz_megallohely.png"},
                {"text": None, "is_correct": False, "image_path": "/static/images/tablak/korforgalom.png"}
            ]
        },
        {
            "text": "Melyik jelzés a 'Vigyázat, gyermekek'?",
            "image_path": None,
            "answers": [
                {"text": None, "is_correct": False, "image_path": "/static/images/tablak/stop.png"},
                {"text": None, "is_correct": True, "image_path": "/static/images/tablak/gyermekek_tabla.png"},
                {"text": None, "is_correct": False, "image_path": "/static/images/tablak/varakozni_tilos.jpg"},
                {"text": None, "is_correct": False, "image_path": "/static/images/tablak/gyalogosok_atkelohelye.png"}
            ]
        },
        {
            "text": "Melyik jelzés a 'Főútvonal vége' tábla?",
            "image_path": None,
            "answers": [
                {"text": None, "is_correct": False, "image_path": "/static/images/tablak/foutvonal_vonalvezetese.png"},
                {"text": None, "is_correct": True, "image_path": "/static/images/tablak/foutvonal_vege.png"},
                {"text": None, "is_correct": False, "image_path": "/static/images/tablak/kerekparsav.png"},
                {"text": None, "is_correct": False, "image_path": "/static/images/tablak/korforgalom_elorejelzes.png"}
            ]
        },
        {
            "text": "Melyik jelzés a 'Kikerülési irány'?",
            "image_path": None,
            "answers": [
                {"text": None, "is_correct": True, "image_path": "/static/images/tablak/kikerulesi_irany.png"},
                {"text": None, "is_correct": False, "image_path": "/static/images/tablak/ketiranyu_forgalom.png"},
                {"text": None, "is_correct": False, "image_path": "/static/images/tablak/behajtani_tilos.jpg"},
                {"text": None, "is_correct": False, "image_path": "/static/images/tablak/Megallni_tilos.jpg"}
            ]
        },
        {
            "text": "Melyik jelzés a 'Vigyázat, vasúti átjáró sorompóval'?",
            "image_path": None,
            "answers": [
                {"text": None, "is_correct": True, "image_path": "/static/images/tablak/sorompoval_biztositott_vasuti_atjaro.png"},
                {"text": None, "is_correct": False, "image_path": "/static/images/tablak/Kotelezo_haladasi_irany_egyenesen_es_balra.jpg"},
                {"text": None, "is_correct": False, "image_path": "/static/images/tablak/kerekparsav.png"},
                {"text": None, "is_correct": False, "image_path": "/static/images/tablak/gyalogosok_atkelohelye.png"}
            ]
        },
        {
            "text": "Melyik jelzés a 'Kétirányú forgalom'?",
            "image_path": None,
            "answers": [
                {"text": None, "is_correct": False, "image_path": "/static/images/tablak/kikerulesi_irany.png"},
                {"text": None, "is_correct": True, "image_path": "/static/images/tablak/ketiranyu_forgalom.png"},
                {"text": None, "is_correct": False, "image_path": "/static/images/tablak/egyiranyu_forgalom.png"},
                {"text": None, "is_correct": False, "image_path": "/static/images/tablak/kerulo_utiranyt_jelzo_tabla.png"}
            ]
        },
        {
            "text": "Melyik jelzés a 'Jobbra kanyarodni tilos'?",
            "image_path": None,
            "answers": [
                {"text": None, "is_correct": True, "image_path": "/static/images/tablak/jobbra_kanyarodni_tilos.png"},
                {"text": None, "is_correct": False, "image_path": "/static/images/tablak/kerekpar_ut.png"},
                {"text": None, "is_correct": False, "image_path": "/static/images/tablak/csuszos_uttest.png"},
                {"text": None, "is_correct": False, "image_path": "/static/images/tablak/egymas_utani_veszelyes_utkanyarulatok.png"}
            ]
        },
        {
            "text": "Melyik jelzés a 'Kerékpár út'?",
            "image_path": None,
            "answers": [
                {"text": None, "is_correct": False, "image_path": "/static/images/tablak/kerekparsav.png"},
                {"text": None, "is_correct": True, "image_path": "/static/images/tablak/kerekpar_ut.png"},
                {"text": None, "is_correct": False, "image_path": "/static/images/tablak/korforgalom.png"},
                {"text": None, "is_correct": False, "image_path": "/static/images/tablak/gyermekek_tabla.png"}
            ]
        },
        {
            "text": "Melyik jelzés a 'Stop'?",
            "image_path": None,
            "answers": [
                {"text": None, "is_correct": True, "image_path": "/static/images/tablak/stop.png"},
                {"text": None, "is_correct": False, "image_path": "/static/images/tablak/szukulo_ut.png"},
                {"text": None, "is_correct": False, "image_path": "/static/images/tablak/varakozni_tilos.jpg"},
                {"text": None, "is_correct": False, "image_path": "/static/images/tablak/gyalogosok_atkelohelye.png"}
            ]
        }
    ]

    for question_data in questions_data:
        answers_data = question_data.pop("answers")
        question = Question(**question_data)
        db.session.add(question)
        db.session.flush()

        for answer_data in answers_data:
            answer = Answer(question_id=question.id, **answer_data)
            db.session.add(answer)

    db.session.commit()
    print("Minden kérdés sikeresen hozzáadva az adatbázishoz.")