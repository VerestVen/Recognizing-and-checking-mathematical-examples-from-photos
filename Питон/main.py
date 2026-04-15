import easyocr
import numexpr as ne

def text_recognition(file_path):
    reader = easyocr.Reader(["ru"])
    result = reader.readtext(file_path)

    return result

def estimat(a):
    if a >= 80:
        return 5
    if 80 > a >= 65:
        return 4
    if 65 > a >= 50:
        return 3
    if 50 > a :
        return 2

def main():
    file_path = input("Фото: ")
    Examp = (text_recognition(file_path=file_path)[0][1])
    Examp = Examp.replace('X', '*')
    Examp = Examp.replace('x', '*')
    Examp = Examp.replace('Х', '*')
    Examp = Examp.replace('х', '*')
    Examp = Examp.replace(':', '/')
    Examp = Examp.replace(';', '/')
    Examp = Examp.replace(" ", "")

    id_ravno = Examp.find("=")
    res = Examp[:id_ravno]
    Otvet = Examp[id_ravno+1:]
    check = ['+', '-', '*', '(', ')', '/']


    val_error = []
    for val in res:
        if val not in check:
            try:
                check_val = int(val)
            except ValueError:
                val_error.append(val)
    if len(val_error) == 0:
        try:
            resultat = ne.evaluate(res)

            print("Ваш пример: ", Examp)
            print("Правильный пример: ", res, "=", resultat)

            a = 0
            if resultat == int(Otvet):
                a = 1

            b = 100
            if a == 0:
                b = 0

            ex = estimat(b)


            print(f"Правильно решено примеров: {a}/1, {b}% - оценка {ex}")

        except SyntaxError as err:
            p = err.offset
            print('Вы ввели недопустимые символы: {}"{}"'.format(res[:p - 1], res[p - 1]))

    else:
        print('Вы ввели недопустимые символы: "{}"'.format(val_error))






if __name__ == "__main__":
    main()
