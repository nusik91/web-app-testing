import requests
import yaml
import logger

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger(name)
with open('config.yaml') as file:
    my_dict=yaml.safe_load(file)

url = my_dict['url']
url1 = my_dict['url1']
username = my_dict['username']
password = my_dict['password']

def token_auth(token):
    try:
        response=requests.get(url=url1, headers={'X-Auth-Token':token}, params={'owner':"notMe"})
        content_var = [item['content'] for item in response.json()['data']]
        return content_var
    except requests.exceptions.RequestException as e:
        logger.error("Error occurred in tokenauth: " + str(e))

def test_step2(login):
    try:
        assert 'content' in token_auth(login)
    except Exception as e:
        logger.error("Error occurred in teststep2: " + str(e))

