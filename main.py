from langserve import RemoteRunnable

# ngrok remote 주소 설정

chain = RemoteRunnable("relieved-mule-amazingly.ngrok-free.app/prompt/")
# chain = RemoteRunnable("relieved-mule-amazingly.ngrok-free.app/prompt/")
# chain = RemoteRunnable("https://poodle-deep-marmot.ngrok-free.app/prompt/")
# chain = RemoteRunnable("http://0.0.0.0:8000/prompt/")

