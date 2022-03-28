def validate_cpf(x):
    x = x.zfill(11)
    try:
        mult = list(range(10,1,-1))
        sum_prod = 0
        for i in range(len(mult)):
            sum_prod += int(x[i]) * mult[i]
        assert sum_prod * 10 % 11 %10 == int(x[9])
        
        mult = list(range(11,1,-1))
        sum_prod = 0
        for i in range(len(mult)):
            sum_prod += int(x[i]) * mult[i]
        assert sum_prod * 10 % 11 %10 == int(x[10])
        
        return True, x
    
    except:
        return False, None
    
def validate_cnpj(x):
    x = x.zfill(14)
    try:
        mult = [5,4,3,2,9,8,7,6,5,4,3,2]
        sum_prod = 0
        for i in range(len(mult)):
            sum_prod += int(x[i]) * mult[i]
        digit = sum_prod % 11
        if digit < 2:
            assert int(x[12]) == 0
        else:
            assert int(x[12]) == 11 - digit
            
        mult = [6,5,4,3,2,9,8,7,6,5,4,3,2]
        sum_prod = 0
        for i in range(len(mult)):
            sum_prod += int(x[i]) * mult[i]
        digit = sum_prod % 11
        if digit < 2:
            assert int(x[13]) == 0
        else:
            assert int(x[13]) == 11 - digit
        
        return True, x
    except:
        return False, None
    
    
def transform_cpf_cnpj(x):
    is_cnpj, cnpj = validate_cnpj(x)
    if is_cnpj:
        return cnpj
    is_cpf, cpf = validate_cpf(x)
    if is_cpf:
        return cpf
    return None
