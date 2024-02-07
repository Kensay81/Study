def is_valid_pin_codes(pin_codes):
    answer = False
    if len(pin_codes) > 0:
        check_set = set(pin_codes)
        if len(check_set) == len(pin_codes):
            for i in pin_codes:
                if i.isdigit() and len(i) == 4:
                    answer = True
                else:
                    answer = False
                    break
    return answer

             
