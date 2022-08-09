# python 3 headers, required if submitting to Ansible

from __future__ import (absolute_import, print_function)
__metaclass__ = type

import re
from ansible.utils.display import Display

display = Display()


class FilterModule(object):
    """
        Ansible file jinja2 tests
    """
    def filters(self):
        return {
            'victoriametrics_checksum_file': self.checksum_file,
            'victoriametrics_checksum': self.checksum,
        }

    def checksum_file(self, data, operation_system="linux", arch="amd64"):
        """
        """
        result = data.replace(".tar.gz", "_checksums.txt")

        display.v("= result: {}".format(result))

        return result


    def checksum(self, data, f):
        """
        """
        checksum = None

        if isinstance(data, list):
            # filter OS
            # linux = [x for x in data if re.search(r".*victoriametrics-.*.{}.*.tar.gz".format(operation_system), x)]
            # filter OS and ARCH
            checksum = [x for x in data if re.search(r".*{}".format(f), x)][0]

        if isinstance(checksum, str):
            checksum = checksum.split(" ")[0]

        display.v("= result: {}".format(checksum))

        return checksum
