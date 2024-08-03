# FastAPI

## 1. Create Project:

```bash
poetry new project-fastapi
```
## 2. Change directory to project:

```bash
cd project-fastapi
```

## 3. Add dependecies:

```bash
poetry add fastapi "uvicorn[standard]"
poetry add --dev pytest
pip install httpx
```

## 4. Write code

Visit [`main.py`](/project_fastapi/main.py) to see code:

## 5. Run project in Poetry Envirnoment:

```bash
poetry run uvicorn project_fastapi.main:app --reload
```

## 6. Open in Browser:

```bash
http://0.0.0.0:8000/

http://0.0.0.0:8000/docs           # default page

http://0.0.0.0:8000/openapi.json   # default page
```

## 6. Testing

- Visit [`test_main.py`](/tests/test_main.py) to see testing code:

- Run these commands to see test results:

```bash
poetry run pytest
# OR
poetry run pytest -v  # (-v for extra info)
```
