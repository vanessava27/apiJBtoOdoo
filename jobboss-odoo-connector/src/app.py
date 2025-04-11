from fastapi import FastAPI
from jobboss.client import JobbossClient
from odoo.client import OdooClient
from services.sync_service import SyncService
import yaml

app = FastAPI()

# Load configuration from config.yaml
with open("config.yaml", "r") as config_file:
    config = yaml.safe_load(config_file)

jobboss_client = JobbossClient(config['jobboss'])
odoo_client = OdooClient(config['odoo'])
sync_service = SyncService(jobboss_client, odoo_client)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Jobboss-Odoo Connector API"}

@app.post("/sync")
def sync_data():
    sync_service.sync()
    return {"message": "Data synchronization initiated"}