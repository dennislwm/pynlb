import json
import logging
import pytest
import yaml

@pytest.fixture
def config(logger):
  with open('config.yml', mode='r') as f:
    y=yaml.safe_load(f)
    j=json.dumps(y, indent=2)
    logger.info(f"config.json: {j}")
    f.close()
  return j

@pytest.fixture
def logger():
  return logging.getLogger(__name__)