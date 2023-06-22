def parse_data_for_graphic(rdata):
    answer = object
    answer.type = "graphic" 
    import json
    data = json.loads(rdata)
    answer.price = [[i, float(data[i][2])] for i in range(0, len(data))]
    answer.max = max(answer.price)
    return answer

def parse_data_for_table(rdata): # Cost Changes request
    answer = object
    answer.type = "table" 
    import json
    data = json.loads(rdata)
    answer.change = data[1];
    answer.symbol = data[0];
    return answer

