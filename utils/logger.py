# utils/logger.py
import logging

def setup_logger():
    logging.basicConfig(filename='output/agent_logs.txt', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')
    return logging.getLogger('agent_logger')
