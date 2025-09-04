ACEest Fitness — DevOps Assignment

This project demonstrates DevOps fundamentals using a minimal Flask API for a fitness/gym use case.  
It covers version control, testing, containerization, and CI/CD automation.

## Tech Stack
- Python 3.10
- Flask
- Pytest
- Docker
- GitHub Actions

## How to Run Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/MaverickVaib/devops_assignment_1_2025.git
   cd devops_assignment_1_2025
   ```


2. Create a virtual environment and install dependencies:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
3. Start the application:

   ```bash
   python flask_app.py
   ```
4. Visit the app at `http://127.0.0.1:5000`.

## API Endpoints

* `GET /` → Health check (returns text)
* `POST /add` → Add a workout (JSON body: `{"workout":"Pushups","duration":15}`)
* `GET /workouts` → Returns all logged workouts

## Running Tests Locally

Use pytest to run unit tests:

```bash
pytest -v
```

## Docker Usage

Build and run the container:

```bash
docker build -t aceest-fitness:latest .
docker run --rm -p 8080:5000 aceest-fitness:latest
```

Test it:

```bash
curl -i http://127.0.0.1:8080/
curl -s -X POST http://127.0.0.1:8080/add -H "Content-Type: application/json" -d '{"workout":"Pushups","duration":15}'
curl -s http://127.0.0.1:8080/workouts
```

## CI/CD with GitHub Actions

* Workflow file: `.github/workflows/ci.yml`
* Trigger: every push or pull request to `main`
* Steps:

  1. Build Docker image
  2. Run `pytest` inside the container

You can view workflow runs and logs under the **Actions** tab of this repository.

```
