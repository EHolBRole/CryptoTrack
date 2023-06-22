import numpy as np
import json


def parse_data_for_graphic(rdata):
    data = json.loads(rdata)
    return [[i, float(data[i][2])] for i in range(0, len(data))]
