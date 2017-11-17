#! /usr/bin/python
# -*- coding:utf-8 -*-

import logging
import json

logging.basicConfig(level=logging.INFO,
    format="%(message)s",
    filename="./log/status.log"
)
logger = logging.getLogger(__name__)

def log_toilet_status(status):
    json_status = json.dumps(status)
    logger.info(json_status)
    pass

if __name__ == "__main__":
    status={"name": "toilet", "distance": "5.23cm"}
    status1={"name": "toilet2", "distance": "15.23cm"}
    log_toilet_status(status)
    log_toilet_status(status1)


