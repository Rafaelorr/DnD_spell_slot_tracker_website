from flask import Flask, render_template, request, redirect, url_for
from spell_slot_data import full_caster_spell_slot_progression, half_caster_spell_slot_progression, \
full_casters, half_casters

app = Flask(__name__)

@app.route("/")
def home():
    # Dit is tijdelijk zodat ik dit in de toekomst gemakkelijker kan koppelen aan andere tools
    return redirect(url_for("spell_slot_tracker"))

@app.route("/spell_slot_tracker", methods=["GET", "POST"])
def spell_slot_tracker():
    if request.method == "POST":
        character_class :str = request.form.get("class")
        character_level :int = int(request.form.get("level"))
        print(character_class + " " + str (character_level))

        if character_class in full_casters:
            print("Je character is een full caster.")
            beschikbare_spell_slots = full_caster_spell_slot_progression[character_level]
            print(beschikbare_spell_slots)
        elif character_class in half_casters:
            print("Je character is een half caster.")
            beschikbare_spell_slots = half_caster_spell_slot_progression[character_level]
            print(beschikbare_spell_slots)
        else:
            print("Je character is geen caster.")
            return render_template("spell_slot_tracker.html")
        
        level_1 = beschikbare_spell_slots["level_1"]
        level_2 = beschikbare_spell_slots["level_2"]
        level_3 = beschikbare_spell_slots["level_3"]
        level_4 = beschikbare_spell_slots["level_4"]
        level_5 = beschikbare_spell_slots["level_5"]
        level_6 = beschikbare_spell_slots["level_6"]
        level_7 = beschikbare_spell_slots["level_7"]
        level_8 = beschikbare_spell_slots["level_8"]
        level_9 = beschikbare_spell_slots["level_9"]

        return render_template("spell_slot_tracker.html", track_spell_slots=True, level_1=level_1, level_2=level_2, level_3=level_3, level_4=level_4, \
                               level_5=level_5, level_6=level_6, level_7=level_7, level_8=level_8, level_9=level_9)

    return render_template("spell_slot_tracker.html", track_spell_slots=False)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)