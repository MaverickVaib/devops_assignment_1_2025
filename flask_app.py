from flask import Flask, request, jsonify

app = Flask(__name__)
workouts = []

@app.get("/")
def home():
    return "ACEest Fitness API is running", 200

@app.get("/workouts")
def get_workouts():
    return jsonify(workouts), 200

@app.post("/add")
def add_workout():
    data = request.get_json(silent=True) or {}
    workout = data.get("workout")
    duration = data.get("duration")

    if not workout or not isinstance(duration, int):
        return jsonify({
            "error": "Invalid input. Send JSON like {\"workout\":\"Pushups\",\"duration\":15}"
        }), 400

    workouts.append({"workout": workout, "duration": duration})
    return jsonify({"message": f"{workout} added successfully!"}), 201

if __name__ == "__main__":
    # Host 0.0.0.0 so Docker can expose it later
    app.run(host="0.0.0.0", port=5000)
