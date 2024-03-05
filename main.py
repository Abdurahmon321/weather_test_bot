from bot import start_bot_polling


if __name__ == "__main__":
    start_bot_polling()

byt = bytearray()
while True:
    name = input("ism kiriting: ")
    if name == "stop":
        break
    lastname = input("familiya kiriting: ")
    yoshi = input("yosh: ")
    byt.extend(bytes(f'ismi: {name} familiyasi: {lastname} yoshi: {yoshi}'.encode('utf-8')))
    print(byt)
