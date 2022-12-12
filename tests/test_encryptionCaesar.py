from app.main import encryptionCaesar


def test_encryptionCaesar():
    cipher = encryptionCaesar('за императора', shift=3)
    cipher2 = encryptionCaesar('я', shift=3)
    cipher3 = encryptionCaesar('', shift=3)
    cipher4 = encryptionCaesar('ю', shift=3)
    cipher5 = encryptionCaesar(' ', shift=3)
    assert cipher == "кг лптзугхсуг"
    assert cipher2 == 'в'
    assert cipher3 == ""
    assert cipher4 == 'б'
    assert cipher5 == ' '
