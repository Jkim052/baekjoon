def solution(numer1, denom1, numer2, denom2):
    num = numer1 * denom2 + numer2 * denom1
    de = denom1 * denom2
    sso = 2
    num2 = num
    de2 = de
    while ((sso < num) and (sso < de)):
        while ((num2 % sso == 0) and (de2 % sso == 0 )):
            num2 = num2 // sso
            de2 = de2 // sso
        sso = sso + 1

    answer = [num2, de2]
    return answer