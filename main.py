import uvicorn
from app import logger, HOST, PORT
from app.main import app
import app.src.tools.newsletter_service as ns


def start_server():
    logger.info("Server is running in port 8000")
    uvicorn.run(app, host=HOST, port=PORT, debug=True)


if __name__ == "__main__":
    ns.run_service()
    # start_server()
