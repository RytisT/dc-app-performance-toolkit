import re
from locustio.common_utils import init_logger, confluence_measure

logger = init_logger(app_type='confluence')


@confluence_measure("locust_app_specific_action")
def app_specific_action(locust):
    r = locust.get(f'/rest/newsteaser/1.0/news/search?cql=(type%20IN%20(blogpost))&expand=body.view,body.view.webresource.uris.all,children.attachment,children.comment,space,version,metadata.likes,history', catch_response=True)  # call app-specific GET endpoint
    content = r.content.decode('utf-8')   # decode response content

    id_pattern_example = '"id":"(.+?)"'
    id = re.findall(id_pattern_example, content)    # get ID from response using regexp

    logger.locust_info(f'id: {id}')  # log information for debug when verbose is true in jira.yml file
    if 'results' not in content:
        logger.error(f"'results' was not found in {content}")
    assert 'results' in content
