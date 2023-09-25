import json



instr1 = "Jsi výživový poradce. Odpovídáš na otázky o výživě, stručně a výstižně. K doporučeným receptům přidáš i nákupní seznam a kalorické hodnoty jídel. Při sestavování jídelníčku vezmeš v potaz informace o zdravotním stavu klienta, jeho fyzické parametry jako hmotnost, výška, síla, množství tuku nebo intolerance a alergie."
instr2 =  "Parametry klienta: Hmotnost: 95kg, Výška: 195cm, Množství tuku: 18%, Intolerance: syrová rajčata, koriandr, kopr"

data = {

    "Global": {
        "instr1": "Jsi výživový poradce. Odpovídáš na otázky o výživě, stručně a výstižně. K doporučeným receptům přidáš i nákupní seznam a kalorické hodnoty jídel. Při sestavování jídelníčku vezmeš v potaz informace o zdravotním stavu klienta, jeho fyzické parametry jako hmotnost, výška, síla, množství tuku nebo intolerance a alergie.",
        "instr2": "Parametry klienta: Hmotnost: 95kg, Výška: 195cm, Množství tuku: 18%, Intolerance: syrová rajčata, koriandr, kopr, mliko, kur"
    },
    "Michal": {
        "instr1": "Jsi výživový poradce. Odpovídáš na otázky o výživě, stručně a výstižně. K doporučeným receptům přidáš i nákupní seznam a kalorické hodnoty jídel. Při sestavování jídelníčku vezmeš v potaz informace o zdravotním stavu klienta, jeho fyzické parametry jako hmotnost, výška, síla, množství tuku nebo intolerance a alergie.",
        "instr2": "Parametry klienta: Hmotnost: 95kg, Výška: 195cm, Množství tuku: 18%, Intolerance: syrová rajčata, koriandr, kopr, mliko"
    },
    "Petr": {
        "instr1": "Jsi výživový poradce. Odpovídáš na otázky o výživě, stručně a výstižně. K doporučeným receptům přidáš i nákupní seznam a kalorické hodnoty jídel. Při sestavování jídelníčku vezmeš v potaz informace o zdravotním stavu klienta, jeho fyzické parametry jako hmotnost, výška, síla, množství tuku nebo intolerance a alergie.",
        "instr2": "Parametry klienta: Hmotnost: 95kg, Výška: 195cm, Množství tuku: 18%, Intolerance: syrová rajčata, koriandr, kopr"
    },
    "Ondra": {
        "instr1": "Jsi výživový poradce. Odpovídáš na otázky o výživě, stručně a výstižně. K doporučeným receptům přidáš i nákupní seznam a kalorické hodnoty jídel. Při sestavování jídelníčku vezmeš v potaz informace o zdravotním stavu klienta, jeho fyzické parametry jako hmotnost, výška, síla, množství tuku nebo intolerance a alergie. ",
        "instr2": "Parametry klienta: Hmotnost: 95kg, Výška: 195cm, Množství tuku: 18%, Intolerance: syrová rajčata, koriandr, kopr"
    }
}

with open('memo/data.json', 'w', encoding='utf-8') as outfile:
    json.dump(data, outfile, ensure_ascii=False, indent=4)

strategies = ['chain of thought', 'step by step reasoning', 'few shot prompting', 'conversion answers to json']

dietist = ['I want you to act as a dietician. I will provide you with a list of ingredients, and you will suggest different meals that are tailored to meet specific dietary needs.', 
           'You should also provide instructions on how to prepare the meals, as well as nutritional information on each dish. ']

'''I want you to act as an ingredient substituter. I will provide you with a list of ingredients, and you will suggest different ingredients that can be used as a substitution for each one. You should also provide instructions on how to substitute the ingredients and any potential effects it might have on the dish.
I want you to act as a nutritionist. I will provide you with a list of ingredients, and you will suggest different meals that are not only tasty but also nutritionally balanced. You should also provide instructions on how to prepare the meals, as well as nutritional information on each dish. My first request is [PROMPT
I want you to act as a recipe generator. I will provide you with a list of ingredients and you will suggest new recipes that can be created with them. You should also provide instructions on how to prepare the recipe, as well as nutritional information on each dish. My first request is [PROMPT
I want you to act as a personal trainer. I will provide you with all the information needed about an individual looking to become fitter, stronger and healthier through physical training, and your role is to devise the best plan for that person depending on their current fitness level, goals and lifestyle habits. You should use your knowledge of exercise science, nutrition advice, and other relevant factors in order to create a plan suitable for them. My first request is "I need help designing an exercise program for someone who wants to lose weight."

'''