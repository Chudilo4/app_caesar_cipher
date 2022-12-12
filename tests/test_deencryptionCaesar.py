from app.main import decryptionCaesar


def test_decryptionCaesar():
    cipher = decryptionCaesar("кг лптзугхсуг", shift=3)
    cipher2 = decryptionCaesar('а', shift=3)
    cipher3 = decryptionCaesar('', shift=3)
    cipher4 = decryptionCaesar('в', shift=3)
    cipher5 = decryptionCaesar(' ', shift=30)
    cipher6 = decryptionCaesar('ю', shift=120)
    cipher7 = decryptionCaesar('r', 1)
    assert cipher == 'за императора'
    assert cipher2 == 'э'
    assert cipher3 == ''
    assert cipher4 == 'я'
    assert cipher6 == 'й'
    assert cipher5 == ' '
    assert cipher7 == ''
