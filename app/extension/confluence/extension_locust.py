from locustio.common_utils import init_logger, confluence_measure, fetch_by_re
from locustio.confluence.requests_params import confluence_datasets

confluence_dataset = confluence_datasets()
logger = init_logger(app_type='confluence')
confluence_dataset = confluence_datasets()



@confluence_measure("locust_app_specific_action")
def app_specific_action(locust):
    body = {"pageId": 41067214, "editorFormat": "<p>Page+edit+with+locust+ecruetvisb</p>"}  # include parsed variables to POST request body
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    r = locust.post(f'/rest/sourceeditor/1.0/convert/toStorageFormat', body, headers, catch_response=True)  # call app-specific GET endpoint

    content = r.content.decode('utf-8')   # decode response content

    if 'content' not in content:
        logger.error(f"'content' was not found in {content}")
    assert 'content' in content

    r = locust.post(f'/rest/sourceeditor/1.0/convert/toEditorFormat', body, headers, catch_response=True)  # call app-specific GET endpoint
    content = r.content.decode('utf-8')   # decode response content

    if 'content' not in content:
        logger.error(f"'content' was not found in {content}")
    assert 'content' in content