import serial
from sqlite3 import connect

con = connect('altimetrs.db')
cur = con.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS Altim (id INTEGER, name string)')
if cur.execute('SELECT COUNT(*) FROM Altim') != 0:
    print('Таблица не пуста! Стереть? [y/N]')
    answ = input()
    if 'y' in answ.lower():
        cur.execute('DELETE FROM Altim')
        print('Таблица удалены')
    else:
        quit(0)



ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

i = 1

while i:
    line = ser.readline()
    if line != b'':
        cur.execute('INSERT INTO Altim (id) VALUES(?)', [line])
        print(f'Запись датчика {line} в базу. Продолжаем поиск [y/N]?')
        answ = input()
        if 'n' in answ.lower():
            i = 0
            cur.close()
            print('Поиск остановлен.')

con.commit()
con.close()

