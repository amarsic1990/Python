def pos_test(p0,p1,p2):
    """ Probability of disease
    Args:
        p0 probability of disease
        p1 sensitivity
        p2 specificity

    Returns:
        Probability of disease given tht the test was positive
    """
    return p0*p1 / (p0*p1 + (1-p0) * (1-p2))


def neg_test(p0,p1,p2):
    """ Probability of disease
    Args:
        p0 probability of disease
        p1 sensitivity
        p2 specificity

    Returns:
        Probability of disease given tht the test was negative
    """
    return p0 * (1-p1) / (p0 * (1-p1) + (1-p0) * p2)

print(pos_test(0.01,0.9,0.9))# 0.08333333333333336
print(neg_test(0.01,0.9,0.9))# 0.0011210762331838563
print(pos_test(0.1,0.95,0.8))# 0.3454545454545455
print(pos_test(0.1,0.7,0.8))# 0.28
print(pos_test(0.1,0.7,0.95))# 0.6086956521739129
print(pos_test(0.1,0.7,0.5))# 0.1346153846153846
