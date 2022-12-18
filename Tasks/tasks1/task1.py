def ordering_info(info):

    clients = {}

    for n in range(0, len(info)):
        client = f'{info[n][2]} {info[n][3]}'
        if clients.get(client) is None:
            clients[client] = f'{info[n][0]} - {info[n][1]}'
        elif clients.get(client):
            a = clients.get(client) + " " + f'{info[n][0]} - {info[n][1]}'
            clients[client] = a
    for k, v in clients.items():
        gen_inform = k + ":" + " " + v
        return gen_inform