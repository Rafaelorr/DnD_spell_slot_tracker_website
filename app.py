from flask import Flask, render_template, request, redirect, url_for, jsonify
from spell_slot_data import full_caster_spell_slot_progression, half_caster_spell_slot_progression, full_casters, half_casters

app = Flask(__name__)

@app.route("/")
def home():
    # Tijdelijk: redirect naar spell_slot_tracker
    return redirect(url_for("spell_slot_tracker"))

@app.route("/spell_slot_tracker", methods=["GET", "POST"])
def spell_slot_tracker():
    if request.method == "POST":
        character_class = request.form.get("class")
        character_level = int(request.form.get("level"))


        if character_class in full_casters:
            beschikbare_spell_slots = full_caster_spell_slot_progression.get(character_level)
        elif character_class in half_casters:
            beschikbare_spell_slots = half_caster_spell_slot_progression.get(character_level)
        else:
            print("Je character is geen caster.")
            return render_template("spell_slot_tracker.html", track_spell_slots=False)

        # Haal spell slots op
        return render_template("spell_slot_tracker.html", track_spell_slots=True, **beschikbare_spell_slots)

    # Bij GET: toon de pagina zonder spell slots
    return render_template("spell_slot_tracker.html", track_spell_slots=False)

@app.route("/spell_slot_tracker_save_slots", methods=["POST"])
def spell_slot_tracker_save_slots():
    # Haal de spell slots op uit het formulier, met default 0
    levels = {}
    for i in range(1, 10):
        levels[f"level_{i}"] = int(request.form.get(f"level_{i}", 0) or 0)
    print(f"Received spell slots: {levels}")

    return render_template("spell_slot_tracker.html", track_spell_slots=True, **levels)

@app.route("/get_spell_slots")
def get_spell_slots():
    character_class = request.args.get("class")
    character_level = int(request.args.get("level"))

    # Bepaal beschikbare spell slots
    if character_class in full_casters:
        available_slots = full_caster_spell_slot_progression.get(character_level, {})
    elif character_class in half_casters:
        available_slots = half_caster_spell_slot_progression.get(character_level, {})
    else:
        # Geen caster: geef zeros terug
        available_slots = {f"level_{i}": 0 for i in range(1, 10)}

    # Stuur JSON response met spell slots
    return jsonify(available_slots)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)