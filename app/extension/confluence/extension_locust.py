import re
import random

from locustio.common_utils import init_logger, confluence_measure
from locustio.confluence.requests_params import confluence_datasets

confluence_dataset = confluence_datasets()
logger = init_logger(app_type='confluence')
confluence_dataset = confluence_datasets()



@confluence_measure("locust_app_specific_action")
def app_specific_action(locust):
    page = random.choice(confluence_dataset["pages"])
    page_id = page[0]
    space_key = page[1]

    body = {"reverse": "false", "spaceCategoryNames": "", "includeArchivedSpaces": "false", "currentPageId": page_id, "currentSpaceKey": space_key, "currentSpaceTitle": ""}  # include parsed variables to POST request body
    headers = {'content-type': 'application/json'}
    r = locust.post(f'/rest/spacetree/1.0/spaces', body, headers, catch_response=True)  # call app-specific POST endpoint
    content = r.content.decode('utf-8')
    if 'spaceCategories' not in content:
        logger.error(f"'assertion string after successful POST request' was not found in {content}")
    assert 'spaceCategories' in content  # assertion after POST request