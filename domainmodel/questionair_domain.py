from pyelt.datalayers.database import Columns
from pyelt.datalayers.dv import *


class Test(HubEntity):

    class Default(Sat):
        test_id = Columns.TextColumn()
        test_label = Columns.TextColumn()
        label_sbg = Columns.TextColumn()
        label_sbg_total = Columns.TextColumn()
        description = Columns.TextColumn()
        description_large = Columns.TextColumn()
        description_copyright = Columns.TextColumn()
        description_report = Columns.TextColumn()
        normgroup_id = Columns.TextColumn()
        normgroup_label = Columns.TextColumn()
        # source_system = Columns.TextColumn()
        # insert_date = Columns.TextColumn


