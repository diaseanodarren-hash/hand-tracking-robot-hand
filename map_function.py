class init:
    def map_range(input, in_min, in_max, out_min, out_max):
        input = max(in_min, min(in_max, input))
        return ((input-in_min)/(in_max-in_min)* (out_max - out_min))+out_min
