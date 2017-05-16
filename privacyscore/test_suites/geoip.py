import json
import os
import re

from subprocess import check_output

from django.conf import settings

from privacyscore.utils import get_raw_data_by_identifier


GEOIP_PATH = os.path.join(
    settings.SCAN_TEST_BASEPATH, 'geoip.rb')


def test(scan_pk: int, url: str, previous_results: dict) -> list:
    """Test the specified url with geoip."""
    # determine hostname
    pattern = re.compile(r'^(https|http)?(://)?([^/]*)/?.*?')
    hostname = pattern.match(url).group(3)

    raw = check_output([
        GEOIP_PATH,
        hostname
    ], timeout=20)

    return [({
        'data_type': 'application/json',
        'test': __name__,
        'identifier': 'jsonresult',
        'scan_pk': scan_pk,
    }, raw)]


def process(raw_data: list, previous_results: dict):
    """Process the raw data of the test."""
    result = json.loads(
        get_raw_data_by_identifier(raw_data, 'jsonresult').decode())

    return result