#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
(c) ECOLE POLYTECHNIQUE FEDERALE DE LAUSANNE, Switzerland, VPSI, 2018.
"""

from pysnow_change_epfl.change_utils import check_sciper, check_pwd, \
                                            get_changelog_info, \
                                            create_change

# Verification before create change
try:
    check_sciper()
    check_pwd()
    # ** Warning: To use the get_changelog_info(..) util function below,
    # the format of version titles in the CHANGELOG file should start
    # with ### and the version number X.Y.Z should precede the date! **
    version_number, description, impact_category = get_changelog_info(
        '<path_to_CHANGELOG.md>')
except Exception as exc:
    print exc
    exit(1)

# Create change
print create_change(service_id='SVC0016',
                    snow_group='SI_NEWS',
                    impact_category=impact_category,
                    short_description="Actu - {}".format(version_number),
                    description=description)
